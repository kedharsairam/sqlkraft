---
name: 'sys.sp_helpconstraint'
title: 'sp_helpconstraint'
category: 'general'
description: 'SQL database in Microsoft Fabric Returns a list of all constraint types, their user-defined or system-supplied name, the columns on which they''re defined, and the expression that defines the constraint (for Transact-SQL syntax conventions Specifies the table for which the constraint information is returned. , with no default. The table specified must be local to the current database. An optional p'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpconstraint
  [ @objname = ]
  N
  'objname'
  [ , [ @nomsg = ]
  'nomsg'
  ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Returns a list of all constraint types, their user-defined or system-supplied name, the columns on which they're defined, and the expression that defines the constraint (for Transact-SQL syntax conventions Specifies the table for which the constraint information is returned. , with no default. The table specified must be local to the current database. An optional parameter that prints the table name.

## Syntax

```sql
sp_helpconstraint
[ @objname = ]
N
'objname'
[ , [ @nomsg = ]
'nomsg'
]
[ ; ]
```

## Examples

### Example 1

```sql
sp_help <table>
```

### Example 2

```sql
sp_helpconstraint
```

### Example 3

```sql
AdventureWorks2025
```

### Example 4

```sql
AdventureWorksDW2025
```

### Example 5

```sql
Product.Product
```

### Example 6

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sp_helpconstraint
'Production.Product'
;
```
