---
name: 'Result value'
title: 'Result value'
category: 'statements'
description: 'Azure SQL Managed Instance'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Compares a scalar value with a single-column set of values. SOME and ANY are equivalent.

Transact-SQL syntax conventions


## syntaxsql
scalar_expression

Is any valid

expression

.

{ = | <> | != | > | >= | !> | < | <= | !< }

Is any valid comparison operator.

Specifies that a comparison should be made.

Is a subquery that has a result set of one column. The data type of the column returned must

be the same data type as

scalar_expression

.

### TRUE

### FALSE

```sql
scalar_expression { = |
<>
| != | > | >= | !> |
< | <= | !< }
{ SOME | ANY } ( subquery )
```
