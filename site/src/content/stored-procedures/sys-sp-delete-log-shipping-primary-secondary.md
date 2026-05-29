---
name: 'sys.sp_delete_log_shipping_primary_secondary'
title: 'sp_delete_log_shipping_primary_secondary'
category: 'general'
description: 'Removes the entry for a secondary database on the primary server. Transact-SQL syntax conventions The name of the database on the primary server. The name of the secondary server. The name of the secondary database.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_log_shipping_primary_secondary
  [ @primary_database = ]
  N
  'primary_database'
  , [ @secondary_server = ]
  N
  'secondary_server'
  , [ @secondary_database = ]
  N
  'secondary_database'
  [ ; ]
---

## Description

Removes the entry for a secondary database on the primary server. Transact-SQL syntax conventions The name of the database on the primary server. The name of the secondary server. The name of the secondary database.

## Syntax

```sql
sp_delete_log_shipping_primary_secondary
[ @primary_database = ]
N
'primary_database'
, [ @secondary_server = ]
N
'secondary_server'
, [ @secondary_database = ]
N
'secondary_database'
[ ; ]
```

## Examples

### Example 1

```sql
sp_delete_log_shipping_primary_secondary
```

### Example 2

```sql
master
```

### Example 3

```sql
log_shipping_primary_secondaries
```

### Example 4

```sql
sp_delete_log_shipping_primary_secondary
```

### Example 5

```sql
LogShipAdventureWorks
```

### Example 6

```sql
FLATIRON
```

### Example 7

```sql
EXECUTE
master.dbo.sp_delete_log_shipping_primary_secondary
@primary_database = N
'AdventureWorks'
,
@secondary_server = N
'FLATIRON'
,
@secondary_database = N
'LogShipAdventureWorks'
;
GO
```
