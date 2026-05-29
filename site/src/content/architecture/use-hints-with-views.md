---
title: 'Use hints with views'
topic: 'query-processing'
description: 'Hints that are placed on views in a query might conflict with other hints that are discovered'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Hints that are placed on views in a query might conflict with other hints that are discovered

when the view is expanded to access its base tables. When this occurs, the query returns an

error. For example, consider the following view that contains a table hint in its definition:

SQL

Now suppose you enter this query:

SQL

The query fails, because the hint

that is applied on view

in the

query is propagated to both tables

and

in the view

when it is expanded. However, expanding the view also reveals the

hint on

. Because the

and

hints conflict, the resulting query is

incorrect.

The

,

,

,

, or

table hints conflict with each other, as do

the

,

,

,

,

table hints.

Hints can propagate through levels of nested views. For example, suppose a query applies the

hint on a view

. When

is expanded, we find that view

is part of its definition.

's definition includes a

hint on one of its base tables. But this table also inherits the

hint from the query on view

. Because the

and

hints conflict, the

query fails.

When the

hint is used in a query that contains a view, the join order of the tables

within the view is determined by the position of the view in the ordered construct. For example,

the following query selects from three tables and a view:

SQL

```sql
SERIALIZABLE
```

```sql
Person.AddrState
```

```sql
Person.Address
```

```sql
Person.StateProvince
```

```sql
NOLOCK
```

```sql
Person.Address
```

```sql
SERIALIZABLE
```

```sql
NOLOCK
```

```sql
PAGLOCK
```

```sql
NOLOCK
```

```sql
ROWLOCK
```

```sql
TABLOCK
```

```sql
TABLOCKX
```

```sql
HOLDLOCK
```

```sql
NOLOCK
```

```sql
READCOMMITTED
```

```sql
REPEATABLEREAD
```

```sql
SERIALIZABLE
```

```sql
HOLDLOCK
```

```sql
v1
```

```sql
v1
```

```sql
v2
```

```sql
v2
```

```sql
NOLOCK
```

```sql
HOLDLOCK
```

```sql
v1
```

```sql
NOLOCK
```

```sql
HOLDLOCK
```

```sql
FORCE ORDER
```

```sql
USE
AdventureWorks2022;
GO
CREATE
VIEW
Person.AddrState
WITH
SCHEMABINDING
AS
SELECT
a.AddressID, a.AddressLine1,
s.StateProvinceCode, s.CountryRegionCode
FROM
Person.Address a
WITH
(NOLOCK), Person.StateProvince s
WHERE
a.StateProvinceID = s.StateProvinceID;
SELECT
AddressID, AddressLine1, StateProvinceCode, CountryRegionCode
FROM
Person.AddrState
WITH
(
SERIALIZABLE
)
WHERE
StateProvinceCode =
'WA'
;
```
