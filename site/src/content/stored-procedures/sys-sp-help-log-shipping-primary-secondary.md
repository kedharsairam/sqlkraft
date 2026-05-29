---
name: "sys.sp_help_log_shipping_primary_secondary"
title: "sp_help_log_shipping_primary_secondary"
category: "general"
description: "This stored procedure returns information regarding all the secondary databases for a given Transact-SQL syntax conventions The name of the database on the primary server. The name of the secondary instance of the SQL Server Database Engine in the log"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_log_shipping_primary_secondary
  [ @primary_database = ]
  N
  'primary_database'
  [ ; ]
---

## Description

This stored procedure returns information regarding all the secondary databases for a given Transact-SQL syntax conventions The name of the database on the primary server. The name of the secondary instance of the SQL Server Database Engine in the log

## Syntax

```sql
sp_help_log_shipping_primary_secondary
[ @primary_database = ]
N
'primary_database'
[ ; ]
```

## Examples

### Example 1

```sql
secondary_database
```

### Example 2

```sql
sp_help_log_shipping_primary_secondary
```

### Example 3

```sql
master
```

### Example 4

```sql
sp_help_log_shipping_primary_secondary
```

### Example 5

```sql
AdventureWorks2022
```

### Example 6

```sql
EXECUTE
master.dbo.sp_help_log_shipping_primary_secondary @primary_database =
N
'AdventureWorks'
;
GO
```
