---
name: 'UNPIVOT example'
title: 'UNPIVOT example'
category: 'queries'
description: 'carries out almost the reverse operation of'
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

carries out almost the reverse operation of

, by rotating columns into rows.

Suppose the table produced in the previous example is stored in the database as

, and you

want to rotate the column identifiers

,

,

,

, and

into row values that

correspond to a particular vendor. As such, you must identify two extra columns.

The column that contains the column values that you're rotating (

,

, and so on) is

called

, and the column that holds the values that currently exist under the columns

being rotated, is called

. These columns correspond to the

pivot_column

and

value_column

, respectively, in the Transact-SQL definition. Here's the query.

SQL

When aggregate functions are used with

, the presence of any null values in the

value column aren't considered when computing an aggregation.

#### Output

### Object Explorer

### Views

### Script View

### as

Here's a partial result set.

isn't the exact reverse of

.

carries out an aggregation and merges possible

multiple rows into a single row in the output.

doesn't reproduce the original table-

valued expression result, because rows have been merged. Also,

values in the input of

disappear in the output. When the values disappear, it shows that there might have

been original

values in the input before the

operation.

The

view in the

sample database

uses

to return the total sales for each salesperson, for each fiscal year. To script the view

in SQL Server Management Studio, in

, locate the view under the

folder

for the

database. Right-click the view name, and then select

.

FROM clause (Transact-SQL)

CASE (Transact-SQL)

Last updated on 02/25/2026

Related content

```sql
UNPIVOT
```

```sql
PIVOT
```

```sql
pvt
```

```sql
Emp1
```

```sql
Emp2
```

```sql
Emp3
```

```sql
Emp4
```

```sql
Emp5
```

```sql
Emp1
```

```sql
Emp2
```

```sql
Employee
```

```sql
Orders
```

```sql
PIVOT
```

```sql
-- Create the table and insert values as portrayed in the previous example.
CREATE
TABLE
pvt (
VendorID
INT
,
Emp1
INT
,
Emp2
INT
,
Emp3
INT
,
Emp4
INT
,
Emp5
INT
);
GO
INSERT
INTO
pvt
VALUES
(1, 4, 3, 5, 4, 4);
INSERT
INTO
pvt
VALUES
(2, 4, 1, 5, 5, 5);
INSERT
INTO
pvt
VALUES
(3, 4, 3, 5, 4, 4);
INSERT
INTO
pvt
VALUES
(4, 4, 2, 5, 5, 4);
INSERT
INTO
pvt
VALUES
(5, 5, 1, 5, 5, 5);
GO
-- Unpivot the table.
SELECT
VendorID, Employee, Orders
FROM
(
SELECT
VendorID, Emp1, Emp2, Emp3, Emp4, Emp5
FROM
pvt
```

```sql
UNPIVOT
```

```sql
PIVOT
```

```sql
PIVOT
```

```sql
UNPIVOT
```

```sql
NULL
```

```sql
UNPIVOT
```

```sql
NULL
```

```sql
PIVOT
```

```sql
Sales.vSalesPersonSalesByFiscalYears
```

```sql
AdventureWorks2025
```

```sql
PIVOT
```

```sql
AdventureWorks2025
```

```sql
) p
UNPIVOT
(
Orders
FOR
Employee
IN
(Emp1, Emp2, Emp3, Emp4, Emp5)
)
AS
unpvt;
GO
VendorID    Employee    Orders
----------- ----------- ------
1            Emp1       4
1            Emp2       3
1            Emp3       5
1            Emp4       4
1            Emp5       4
2            Emp1       4
2            Emp2       1
2            Emp3       5
2            Emp4       5
2            Emp5       5
```
