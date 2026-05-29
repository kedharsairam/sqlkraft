---
name: 'wildcard character'
title: 'wildcard character'
category: 'statements'
description: 'symbol is specified, the Database Engine searches for the number'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

If the

symbol is specified, the Database Engine searches for the number

followed

by any string of zero or more characters.

For example, the following query shows all dynamic management views in the

database, because they all start with the letters

.

SQL

To see all objects that aren't dynamic management views, use

. If you have a

total of 32 objects and

finds 13 names that match the pattern,

finds the 19

７

Note

comparisons are affected by collation. For more information, see

SQL)

.

#### Symbol

#### Meaning

```sql
LIKE '5%'
```

```sql
5
```

```sql
AdventureWorks2025
```

```sql
dm
```

```sql
NOT LIKE 'dm%'
```

```sql
LIKE
```

```sql
NOT LIKE
```

```sql
VALUES
(
'Robert King'
);
SELECT
*
FROM
t
WHERE
col1
LIKE
'% King'
;
-- returns 1 row
-- Unicode pattern matching with nchar column
CREATE
TABLE
t (col1
NCHAR
(30));
INSERT
INTO
t
VALUES
(
'Robert King'
);
SELECT
*
FROM
t
WHERE
col1
LIKE
'% King'
;
-- no rows returned
-- Unicode pattern matching with nchar column and RTRIM
CREATE
TABLE
t (col1
NCHAR
(30));
INSERT
INTO
t
VALUES
(
'Robert King'
);
SELECT
*
FROM
t
WHERE
RTRIM
(col1)
LIKE
'% King'
;
-- returns 1 row
```

```sql
LIKE
```

```sql
-- Uses AdventureWorks
SELECT
Name
FROM
sys.system_views
WHERE
Name
LIKE
'dm%'
;
GO
```
