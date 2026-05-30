---
title: "databases?"
topic: "query-processing"
description: "In the previous query example, only table"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

In the previous query example, only table

is affected by the locking hint, while

can still

benefit from optimized locking.

SQL

In the previous query example, only table

uses the

isolation level and hold

locks until the end of the transaction. Other updates to

can still benefit from optimized

locking. The same applies to the

hint.

In Azure SQL Database, Azure SQL Managed Instance

, and SQL database in Microsoft

Fabric, yes. In SQL Server 2025 (17.x) optimized locking is disabled by default but can be

enabled on any user database that has accelerated database recovery enabled.

AUTD

```sql
t6
```

```sql
t5
```

```sql
t5
```

```sql
REPEATABLE READ
```

```sql
t5
```

```sql
HOLDLOCK
```

```sql
CREATE
TABLE
t5
(
a
int
NOT
NULL
,
b
int
NOT
NULL
);
CREATE
TABLE
t6
(
a
int
NOT
NULL
,
b
int
NOT
NULL
);
GO
INSERT
INTO
t5
VALUES
(1,10),(2,20),(3,30);
INSERT
INTO
t6
VALUES
(1,10),(2,20),(3,30);
GO
UPDATE
t5
SET
t5.b = t6.b
FROM
t5
INNER
JOIN
t6
WITH
(UPDLOCK)
ON
t5.a = t6.a;
UPDATE
t5
SET
t5.b = t6.b
FROM
t5
WITH
(REPEATABLEREAD)
INNER
JOIN
t6
ON
t5.a = t6.a;
```
