---
name: "= (Assignment Operator)"
title: "= (Assignment Operator)"
category: "operators"
description: ""
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

The equal sign (=) is the only Transact-SQL assignment operator. In the following example, the

variable is created, and then the assignment operator sets

to a value

returned by an expression.

The assignment operator can also be used to establish the relationship between a column

heading and the expression that defines the values for the column. The following example

displays the column headings

and. The string

is

displayed in the

column heading for all rows. Then, each product ID from

the

table is listed in the

column heading.

Operators (Transact-SQL)

Compound Operators (Transact-SQL)

Expressions (Transact-SQL)

See Also

```sql
@MyCounter
```

```sql
@MyCounter
```

`FirstColumnHeading`

`SecondColumnHeading`

`xyz`

`FirstColumnHeading`

`Product`

`SecondColumnHeading`

```sql
DECLARE
@MyCounter
INT
;
SET
@MyCounter = 1;
-- Uses AdventureWorks
SELECT
FirstColumnHeading =
'xyz'
,
SecondColumnHeading = ProductID
FROM
Production.Product;
GO
```
