---
name: 'sys.fn_listextendedproperty'
title: 'sys.fn_listextendedproperty'
category: 'text-image'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

## A. Displaying extended properties on a database

If the value for

property_name

is NULL or default, fn_listextendedproperty returns all the

properties for the specified object.

When the object type is specified and the value of the corresponding object name is NULL or

default, fn_listextendedproperty returns all extended properties for all objects of the type

specified.

The objects are distinguished according to levels, with level 0 as the highest and level 2 the

lowest. If a lower-level object, level 1 or 2, type and name are specified, the parent object type

and name should be given values that are not NULL or default. Otherwise, the function returns

an empty result set.

is fixed as Latin1_General_CI_AI. However you can workaround this by overriding

collation in comparison.


## Permissions to list extended properties of objects vary by object type.
The following example displays all extended properties set on the database object itself.

## B. Displaying extended properties on all columns in a table

## C. Displaying extended properties on all tables in a schema

Here's the result set.

The following example lists extended properties for columns in the

table. This is

contained in the schema

.

Here's the result set.

The following example lists extended properties for all tables contained in the

schema.

sp_addextendedproperty (Transact-SQL)

sp_dropextendedproperty (Transact-SQL)

sp_updateextendedproperty (Transact-SQL)

sys.extended_properties (Transact-SQL)

Last updated on 11/18/2025

See Also

```sql
SELECT o.[object_id] AS 'table_id', o.[name] 'table_name',
0 AS 'column_order', NULL AS 'column_name', NULL AS 'column_datatype',
NULL AS 'column_length', Cast(e.value AS varchar(500)) AS 'column_description'
FROM AdventureWorks.sys.objects AS o
LEFT JOIN sys.fn_listextendedproperty(N'MS_Description',
N'user',N'HumanResources',N'table', N'Employee', null, default) AS e
ON o.name = e.objname COLLATE SQL_Latin1_General_CP1_CI_AS
WHERE o.name = 'Employee';
```

```sql
USE AdventureWorks2022;
GO
SELECT objtype, objname, name, value
FROM fn_listextendedproperty(default, default, default, default, default, default,
default);
GO
```

```sql
objtype objname name value
--------- --------- ----------- ----------------------------
NULL NULL MS_Description AdventureWorks2008 Sample OLTP Database
(1 row(s) affected)
```

```sql
ScrapReason
```

```sql
Production
```

```sql
objtype objname name value
------- ----------- ------------- ------------------------
COLUMN ScrapReasonID MS_Description Primary key for ScrapReason records.
COLUMN Name MS_Description Failure description.
COLUMN ModifiedDate MS_Description Date the record was last updated.
(3 row(s) affected)
```

```sql
Sales
```

```sql
USE AdventureWorks2022;
GO
SELECT objtype, objname, name, value
FROM fn_listextendedproperty (NULL, 'schema', 'Production', 'table', 'ScrapReason',
'column', default);
GO
```

```sql
USE AdventureWorks2022;
GO
```

```sql
SELECT objtype, objname, name, value
FROM fn_listextendedproperty (NULL, 'schema', 'Sales', 'table', default, NULL,
NULL);
GO
```
