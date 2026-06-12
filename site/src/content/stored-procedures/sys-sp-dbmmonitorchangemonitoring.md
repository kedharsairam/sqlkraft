---
name: "sys.sp_dbmmonitorchangemonitoring"
title: "sp_dbmmonitorchangemonitoring"
category: "general"
description: "Changes the value of a database mirroring monitoring parameter. Specifies the identifier of the parameter to be changed. Currently, only the following parameter is available: The number of minutes between updates to the database mirroring status table. The default Specifies the new value for the parameter that is being changed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbmmonitorchangemonitoring
  [ @parameter_id = ] parameter_id
  , [ @value = ] value
  [ ; ]
---

## Description

Changes the value of a database mirroring monitoring parameter. Specifies the identifier of the parameter to be changed. Currently, only the following parameter is available: The number of minutes between updates to the database mirroring status table. The default Specifies the new value for the parameter that is being changed.

## Syntax

```sql
sp_dbmmonitorchangemonitoring
[ @parameter_id = ] parameter_id
, [ @value = ] value
[ ; ]
```

## Examples

### Example 1

```sql
1
```

### Example 2

```sql
EXECUTE sp_dbmmonitorchangemonitoring 1, 5;
```

### Example 3

```sql
EXECUTE sp_dbmmonitordropmonitoring;
```

### Example 4

```sql
EXECUTE sp_dbmmonitorhelpalert AdventureWorks2022;
```
