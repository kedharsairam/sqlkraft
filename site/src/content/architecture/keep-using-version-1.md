---
title: "Keep using version 1"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Similarly, any Full-Text population on a version 1 index fails to find the filter binaries on disk

after upgrade:

Output

Rebuild your indexes to use version 2 components.

To upgrade individual indexes without rebuilding the entire catalog, drop and recreate the

indexes.

If you need to use version 1 for application compatibility, first set

to avoid an unintended upgrade on rebuild.

）

Important

Version 1 is deprecated for SQL Server on Linux. In SQL Server 2025 (17.x) and later

versions, the

package doesn't include version 1 binaries. Attempting to

install mismatched versions of the

and

packages is

unsupported, and results in full-text failures.

Next, copy the legacy word breaker and filter binaries from an older instance to the target

instance's

folder.

TDS 8.0

Deprecated Database Engine features in SQL Server 2019 (15.x)

Discontinued Database Engine functionality in SQL Server

Last updated on 01/12/2026

Related content

```sql
FULLTEXT_INDEX_VERSION = 1
```

```sql
Warning: No appropriate filter was found during full-text index population for table or indexed view '[db].[dbo].[table_name]' (table or indexed view ID '901578250',
database ID '5'), full-text key value '1'. Some columns of the row were not indexed.
```

```sql
-- Verify value = 2
SELECT
*
FROM sys.database_scoped_configurations
WHERE
[
name
] =
'FULLTEXT_INDEX_VERSION'
;
-- Per catalog upgrade
ALTER
FULLTEXT
CATALOG
[FtCatalog]
REBUILD
;
```

```sql
mssql-server-fts
```

```sql
mssql-server-fts
```

```sql
mssql-server
```

```sql
ALTER
DATABASE
SCOPED CONFIGURATION
SET
FULLTEXT_INDEX_VERSION = 1;
```

`Binn`
