---
name: "sys.sp_unbindrule"
title: "sp_unbindrule"
category: "general"
description: "Unbinds a rule from a column or an alias data type in the current database."
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

Unbinds a rule from a column or an alias data type in the current database.

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

_(. and 30 more examples)_
