---
name: "sys.filegroups"
title: "sys.filegroups"
category: "databases-files"
description: "Contains a row for each data space that is a filegroup. For a list of columns that this view inherits, see Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. In SQL Server, the value SQL Server 2016 (13.x) and later versions. 1 = When a file in the filegroup meets the autogrow threshold"
tags: ["databases-files","catalog-view"]
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
ID (
'filegroup_name'
)
```

## Permissions

## Examples

### Example 1

`FILEGROUP_ID`

### Example 2

`PRIMARY`

### Example 3

```sql
FILEGROUP
_
ID (
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
1 (1 row(s) affected)
```

### Example 6

`FILEGROUP_NAME`

### Example 7

```sql
1
```

### Example 8

```sql
FILEGROUP
_
NAME ( filegroup_id )
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

`IsDefault`

_(. and 4 more examples)_
