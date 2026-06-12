---
title: "Automatic Page Repair"
topic: "high-availability"
description: "Automatic page repair is supported by database mirroring and by Always On availability groups."
tags: ["high-availability","automatic-page-repair"]
pubDate: "2025-12-01"
---

Automatic page repair is supported by database mirroring and by Always On availability

groups. After certain types of errors corrupt a page, making it unreadable, a database mirroring

partner (principal or mirror) or an availability replica (primary or secondary) attempts to

automatically recover the page. The partner/replica that cannot read the page requests a fresh

copy of the page from its partner or from another replica. If this request succeeds, the

unreadable page is replaced by the readable copy, and this usually resolves the error.

Generally speaking, database mirroring and Always On availability groups handle I/O errors in

equivalent ways. The few differences are explicitly called out here.

Error types that cause an automatic page-repair attempt

Page types that cannot be automatically repaired

Handling i/o errors on the principal/primary database

Handling i/o errors on the mirror/secondary database

Developer best practice

How to: view automatic page-repair attempts

Database mirroring automatic page repair tries to repair only pages in a data file on which an

operation has failed for one of the errors listed in the following table.

７

Note

Automatic page repair differs from DBCC repair. All of the data is preserved by an

automatic page repair. In contrast, correcting errors by using the DBCC

REPAIR_ALLOW_DATA_LOSS option might require that some pages, and therefore data, be

deleted.
