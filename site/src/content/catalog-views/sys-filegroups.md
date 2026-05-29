---
name: 'sys.filegroups'
title: 'sys.filegroups'
category: 'databases-files'
description: 'Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each data space that is a filegroup. For a list of columns that this view inherits, see Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. In SQL Server, the value SQL Server 2016 (13.x) and later versions. 1 = When a file in the filegroup meets the autogrow threshold'
tags: ["databases-files", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  FILEGROUP
  _
  ID
  (
  'filegroup_name'
  )
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each data space that is a filegroup. For a list of columns that this view inherits, see Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. In SQL Server, the value SQL Server 2016 (13.x) and later versions. 1 = When a file in the filegroup meets the autogrow threshold,

## Syntax

```sql
FILEGROUP
_
ID
(
'filegroup_name'
)
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains a row for each data space that is a filegroup. Description -- For a list of columns that this view inherits, see sys.data_spaces (Transact-SQL) . GUID for the filegroup. NULL = PRIMARY filegroup Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. In SQL Server, the value is NULL. 1 = Filegroup is read-only. 0 = Filegroup is read/write. Applies to: SQL Server 2016 (13.x) and later versions. 1 = When a file in the filegroup meets the autogrow threshold, all files in the filegroup grow. 0 = When a file in the filegroup meets the autogrow threshold, only that file grows. This is the default. Requires membership in the role. For more information, see Metadata Visibility Configuration . Catalog Views (Transact-SQL) Data Spaces (Transact-SQL) ﾉ Expand table See Also sys.objects sys.key_constraints sys.filegroups sys.partition_schemes Querying the SQL Server System Catalog FAQ In-Memory OLTP overview and usage scenarios Last updated on 11/24/2025 sys.database_files (Transact-SQL) sys.filegroups (Transact-SQL) sys.master_files (Transact-SQL) System stored procedures (Transact-SQL) sys.filegroups (Transact-SQL) System stored procedures (Transact-SQL) Database files and filegroups

## Examples

### Example 1

```sql
FILEGROUP_ID
```

### Example 2

```sql
PRIMARY
```

### Example 3

```sql
FILEGROUP
_
ID
(
'filegroup_name'
)
```

### Example 4

```sql
SELECT
FILEGROUP_ID(
'PRIMARY'
)
AS
[Filegroup
ID
];
GO
```

### Example 5

```sql
Filegroup ID
------------
1
(1 row(s) affected)
```

### Example 6

```sql
FILEGROUP_NAME
```

### Example 7

```sql
1
```

### Example 8

```sql
FILEGROUP
_
NAME
( filegroup_id )
```

### Example 9

```sql
SELECT
FILEGROUP_NAME(1)
AS
[Filegroup
Name
];
GO
```

### Example 10

```sql
IsDefault
```


*(... and 4 more examples)*
