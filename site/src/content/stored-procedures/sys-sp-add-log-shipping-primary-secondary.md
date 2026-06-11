---
name: "sys.sp_add_log_shipping_primary_secondary"
title: "sp_add_log_shipping_primary_secondary"
category: "general"
description: "This stored procedure adds an entry for a secondary database on the primary server. Transact-SQL syntax conventions The name of the database on the primary server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_log_shipping_primary_secondary
  [ @primary_database = ]
  'primary_database'
  ,
  [ @secondary_server = ]
  'secondary_server'
  ,
  [ @secondary_database = ]
  'secondary_database'
  [ ; ]
---

## Description

This stored procedure adds an entry for a secondary database on the primary server. Transact-SQL syntax conventions The name of the database on the primary server. The name of the secondary server. The name of the secondary database.

## Syntax

```sql
sp_add_log_shipping_primary_secondary
[ @primary_database = ]
'primary_database'
,
[ @secondary_server = ]
'secondary_server'
,
[ @secondary_database = ]
'secondary_database'
[ ; ]
```

## Examples

### Example 1

`sp_add_log_shipping_primary_secondary`

### Example 2

`master`

### Example 3

`sp_add_log_shipping_primary_secondary`

### Example 4

`LogShipAdventureWorks`

### Example 5

`FLATIRON`

### Example 6

```sql
EXECUTE master.dbo.sp_add_log_shipping_primary_secondary
@primary_database = N
'AdventureWorks'
,
@secondary_server = N
'flatiron'
,
@secondary_database = N
'LogShipAdventureWorks'
;
GO
```
