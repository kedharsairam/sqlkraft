---
title: "FILE_FLAG_WRITE_THROUGH"
topic: "query-processing"
description: "data modification statements generate logical page writes."
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

data modification statements generate logical page writes. You can picture this

stream of writes as going to two places: the log and the database itself. For performance reasons,

defers writes to the database through its own cache buffer system. The system only

momentarily defers writes to the log until

time. It doesn't cache these writes in the same

way as data writes. Because log writes for a given page always come before the page's data

writes, the log is sometimes referred to as a

write-ahead log

(WAL).

maintains the

atomicity, consistency, isolation, and durability (ACID) properties of

transactions

through the WAL protocol.

The term

protocol

is an excellent way to describe WAL. The WAL used by SQL Server is known as

ARIES (Algorithm for Recovery and Isolation Exploiting Semantics). For more information, see

Manage accelerated database recovery.

It's a specific and defined set of implementation steps necessary to ensure that data is stored and

exchanged properly and can be recovered to a known state in the event of a failure. Just as a

network contains a defined protocol to exchange data in a consistent and protected manner, so

too does the WAL describe the protocol to protect data. All versions of SQL Server open the log

and data files using the Win32

function. The

member includes

the

option when opened by SQL Server.

creates its database files using the

flag. This option instructs

the system to write through any intermediate cache and go directly to storage. The system can

still cache write operations, but it can't lazily flush them. For more information, see

CreateFileA.

The

option ensures that when a write operation returns successful

completion, the data is correctly stored in stable storage. This feature aligns with the Write-

Ahead Logging (WAL) protocol specification to ensure data integrity. Many storage devices

(NVMe, PCIe, SATA, ATA, SCSI, and IDE-based) contain onboard caches of 512 KB, 1 MB, and

larger. Storage caches usually rely on a capacitor and not a battery-backed solution. These

Don't rely on an external UPS alone. Faults unrelated to power, such as firmware bugs or

hardware failure, can still lead to cache loss.

`COMMIT`

`CreateFile`

`dwFlagsAndAttributes`

`FILE_FLAG_WRITE_THROUGH`

`FILE_FLAG_WRITE_THROUGH`

`FILE_FLAG_WRITE_THROUGH`
