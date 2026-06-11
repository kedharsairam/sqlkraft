---
name: "sys.sp_unbindrule"
title: "sp_unbindrule"
category: "general"
description: "Unbinds a rule from a column or an alias data type in the current database. Transact-SQL syntax conventions The name of the table and column or the alias data type from which the rule is unbound. , with no default. SQL Server attempts to resolve two-part identifiers to column names first, then to alias data types."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_unbindrule
  [ @objname = ]
  N
  'objname'
  [ , [ @futureonly = ]
  'futureonly'
  ]
  [ ; ]
---

## Description

Unbinds a rule from a column or an alias data type in the current database. Transact-SQL syntax conventions The name of the table and column or the alias data type from which the rule is unbound. , with no default. SQL Server attempts to resolve two-part identifiers to column names first, then to alias data types. When unbinding a rule from an alias data type, any columns of the data type that have the same rule are also unbound. Columns of

## Syntax

```sql
sp_unbindrule
[ @objname = ]
N
'objname'
[ , [ @futureonly = ]
'futureonly'
]
[ ; ]
```

## Examples

### Example 1

`sp_unbindrule`

### Example 2

```sql
DROP RULE
```

### Example 3

```sql
DROP RULE
```

### Example 4

`CHECK`

### Example 5

`CHECK`

### Example 6

```sql
DROP RULE
```

### Example 7

`ALTER`

### Example 8

`VendorID_rule`

### Example 9

```sql
EXEC sp_unbindrule 'Production.ProductVendor.VendorID';
DROP
RULE VendorID_rule;
```

### Example 10

```sql
CREATE RULE
DROP RULE sp_bindrule sp_unbindrule
CHECK
```

_(... and 30 more examples)_
