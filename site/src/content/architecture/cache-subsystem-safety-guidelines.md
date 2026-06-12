---
title: "Cache subsystem safety guidelines"
topic: "query-processing"
description: "Use of a write caching (also called write-back caching) storage controller can improve SQL Server"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Use of a write caching (also called write-back caching) storage controller can improve SQL Server

performance. Write caching controllers and storage subsystems are safe for SQL Server, if they're

designed for use in a data-critical transactional database management system (DBMS)

environment. These design features must preserve cached data if a system failure occurs. Using

an external uninterruptible power supply (UPS) to achieve this protection is generally not

sufficient, because failure modes that are unrelated to power can occur.

Caching controllers and storage subsystems can be safe for use by SQL Server. Most new

purpose-built server platforms that incorporate these controllers are safe. However, you should

check with your hardware vendor to be sure that the storage subsystem was tested and approved

for use in a data-critical transactional relational database management system (RDBMS)

environment.

Write-back caching controllers can improve performance if they meet specific safety

requirements:

Include battery-backed cache or nonvolatile memory, such as NVDIMM or super-capacitor-

backed flash.

Be certified by the vendor for data-critical OLTP database environments.

Provide protection that covers all failure conditions, not just power loss.

Some storage vendors use persistent memory (PMEM) as storage rather than a cache, which

can improve overall performance. For more information, see

and.

）

Important

depends on

guaranteed delivery to stable media

for transactional integrity and

recovery. Unsafe caching that doesn't ensure preservation of data across failures can corrupt

databases, regardless of the consistency of transaction log writes. Always verify that any

write-caching mechanism provides full durability guarantees.

）

Important
