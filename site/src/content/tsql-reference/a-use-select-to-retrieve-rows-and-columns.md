---
name: "A. Use SELECT to retrieve rows and columns"
title: "A. Use SELECT to retrieve rows and columns"
category: "statements"
description: "Azure SQL Managed Instance"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This article provides examples of using the

SELECT

statement.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

The following example shows three code examples. The first code example returns all rows (no

clause is specified) and all columns (using the

) from the

table in the

database.

SQL

This example returns all rows (no

clause is specified), and only a subset of the columns

(

,

,

) from the

table in the

database.

Additionally, a column heading is added.

SQL

```sql
AdventureWorks2025
```

```sql
AdventureWorksDW2025
```

```sql
WHERE
```

```sql
*
```

```sql
Product
```

```sql
AdventureWorks2025
```

```sql
WHERE
```

```sql
Name
```

```sql
ProductNumber
```

```sql
ListPrice
```

```sql
Product
```

```sql
AdventureWorks2025
```

```sql
USE
AdventureWorks2025;
GO
SELECT
*
FROM
Production.Product
ORDER
BY
Name
ASC
;
-- Alternate way.
USE
AdventureWorks2025;
GO
SELECT
p.*
FROM
Production.Product
AS
p
ORDER
BY
Name
ASC
;
GO
USE
AdventureWorks2025;
GO
SELECT
Name
,
ProductNumber,
ListPrice
AS
Price
```
