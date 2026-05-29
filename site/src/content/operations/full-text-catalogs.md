---
title: "Full-Text Catalogs"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  To mirror a database that has a full-text catalog, use backup as usual to create a full database

  backup of the principal database, and then restore th
tags:
  - "high-availability"
  - "full-text-catalogs"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

To mirror a database that has a full-text catalog, use backup as usual to create a full database

backup of the principal database, and then restore the backup to copy the database to the

mirror server. For more information, see

Prepare a Mirror Database for Mirroring (SQL Server)

.

In a newly created mirror database, the full-text catalog is the same as when the database was

backed up. After database mirroring starts, any catalog-level changes that were made by DDL

statements (CREATE FULLTEXT CATALOG, ALTER FULLTEXT CATALOG, DROP FULLTEXT

CATALOG) are logged and sent to the mirror server to be replayed on the mirror database.

However, index-level changes are not reproduced on the mirror database because it is not

logged on to the principal server. Therefore, as the contents of the full-text catalog change on

the principal database, the contents of the full-text catalog on the mirror database are

unsynchronized.

After a failover, a full crawl of a full-text index on the new principal server might be required or

useful in the following situations:

If change-tracking is turned OFF on a full text index, you must start a full crawl on that

index by using the following statement:

ALTER FULLTEXT INDEX ON

table_name

START FULL POPULATION

If a full-text index is configured for automatic change tracking, the full-text index is

automatically synchronized. However, synchronization slows full-text performance

somewhat. If performance is too slow, you can cause a full crawl by setting change

tracking off and then resetting it to automatic:

To set change tracking off:

ALTER FULLTEXT INDEX ON

table_name

SET CHANGE_TRACKING OFF

To set on automatic change tracking to automatic:
