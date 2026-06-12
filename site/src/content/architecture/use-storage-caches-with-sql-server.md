---
title: "Use storage caches with SQL Server"
topic: "query-processing"
description: "Most storage device caching controllers perform write caching."
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Most storage device caching controllers perform write caching. You can't always disable the write

caching function.

Even if the server uses a UPS, the device doesn't guarantee the security of the cached writes.

Many types of system failures can occur that a UPS doesn't address. For example, a memory

parity error, an operating system (OS) trap, or a hardware glitch that causes a system reset can

produce an uncontrolled system interruption. A memory failure in the hardware write cache can

also result in the loss of vital log information.

Another possible problem related to a write-caching controller can occur at system shutdown. It's

not uncommon to

cycle

the OS or restart the system during configuration changes. Even if a

careful operator follows the OS recommendation to wait until all storage activity ceases before

restarting the system, cached writes can still be present in the controller. When the

-

-

key combination is pressed, or a hardware reset button is pressed, cached writes

can be discarded, potentially damaging the database.

It's possible to design a hardware write cache that takes into account all possible causes of

discarding dirty cache data, which makes it safe for use by a database server. Some of these

design features include intercepting the RST (reset) bus signal to avoid uncontrolled reset of the

caching controller, on-board battery backup, and mirrored or error checking and correcting (ECC)

memory. Check with your hardware vendor to ensure that the write cache includes these and any

other features necessary to avoid data loss.

A database system is primarily responsible for the accurate storage and retrieval of data, even

during unexpected system failures.

The system must guarantee the atomicity and durability of transactions while accounting for

current execution, multiple transactions, and various failure points. This property is often referred

to as the ACID (Atomicity, Consistency, Isolation, and Durability) properties.

This section addresses the implications of storage caches. For more information on caching and

alternate failure mode discussions, see:

86903 SQL Server and caching disk controllers

## Description of logging and data storage algorithms that extend data reliability in SQL Server

`Ctrl`

`Alt`

`Del`
