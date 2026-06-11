---
title: "Memory pressure detection"
topic: "memory-management"
description: ""
tags: ["memory-management", "architecture"]
pubDate: 2026-05-29
---

The buffer manager is

non-uniform memory access (NUMA)

aware. Buffer cache pages are

distributed across hardware NUMA nodes, which allows a thread to access a buffer page

that is allocated on the local NUMA node rather than from foreign memory.

The buffer manager supports

Hot Add Memory

, which allows users to add physical

memory without restarting the server.

The buffer manager supports

large pages

on 64-bit platforms. The page size is specific to

the version of Windows.

The buffer manager provides extra diagnostics that are exposed through dynamic

management views. You can use these views to monitor various operating system

resources that are specific to SQL Server. For example, you can use the

sys.dm_os_buffer_descriptors

view to monitor the pages in the buffer cache.

Memory pressure is a condition resulting from memory shortage, and can result in:

Extra I/Os (such as very active lazy writer background thread)

Higher recompile ratio

Longer running queries (if memory grant waits exist)

Extra CPU cycles

This situation can be triggered by external or internal causes. External causes include:

Available physical memory (RAM) is low. This causes the system to trim working sets of

currently running processes, which can result in overall slowdown. SQL Server can reduce

the commit target of the buffer pool and start trimming internal caches more often.

Overall available system memory (which includes the system page file) is low. This can

cause the system to fail memory allocations, as it's unable to page out currently allocated

memory.

Internal causes include:

Responding to the external memory pressure, when the SQL Server Database Engine sets

lower memory usage caps.

７

Note

Prior to SQL Server 2012 (11.x), enabling large pages in SQL Server requires

.

Memory settings were manually lowered by reducing the

max server memory

configuration.

Changes in memory distribution of internal components between the several caches.

The SQL Server Database Engine implements a framework dedicated to detecting and handling

memory pressure, as part of its dynamic memory management. This framework includes the

background task called Resource Monitor. The Resource Monitor task monitors the state of

external and internal memory indicators. Once one of these indicators changes status, it

calculates the corresponding notification and it broadcasts it. These notifications are internal

messages from each of the engine components, and stored in ring buffers.

Two ring buffers hold information relevant to dynamic memory management:

The Resource Monitor ring buffer, which tracks Resource Monitor activity like was

memory pressure signaled or not. This ring buffer has status information depending on

the current condition of

,

,

, or

.

The Memory Broker ring buffer, which contains records of memory notifications for each

Resource Governor resource pool. As internal memory pressure is detected, low memory

notification is turned on for components that allocate memory, to trigger actions meant

to balance the memory between caches.

Memory brokers monitor the demand consumption of memory by each component and then

based on the information collected, it calculates and optimal value of memory for each of

these components. There's a set of brokers for each Resource Governor resource pool. This

information is then broadcast to each of the components, which grow or shrink their usage as

required.

For more information about memory brokers, see

sys.dm_os_memory_brokers

.

Database pages can use one of two optional mechanisms that help ensure the integrity of the

page, from the time it's written to disk, until it's read again:

torn page protection

and

checksum

protection

. These mechanisms allow an independent method of verifying the correctness of not

only the data storage, but hardware components such as controllers, drivers, cables, and even

the operating system. The protection is added to the page just before writing it to disk, and

verified after it's read from disk.

SQL Server retries any read that fails with a checksum, torn page, or other I/O error four times.

If the read is successful in any one of the retry attempts, a message is written to the error log

`RESOURCE_MEMPHYSICAL_HIGH`

`RESOURCE_MEMPHYSICAL_LOW`

`RESOURCE_MEMPHYSICAL_STEADY`

`RESOURCE_MEMVIRTUAL_LOW`
