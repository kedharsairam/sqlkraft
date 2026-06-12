---
name: "FOR BROWSE"
title: "FOR BROWSE"
category: "statements"
description: "Specifies that updates are allowed while viewing the data in a DB-Library browse mode cursor."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## BROWSE

Specifies that updates are allowed while viewing the data in a DB-Library browse mode cursor.

You can browse a table in an application if the table includes a

column, the table

has a unique index, and the

option is at the end of the

statements sent to

an instance of SQL Server.

can't appear in

statements that the

operator joins.

The browse mode lets you scan the rows in your SQL Server table and update the data in your

table one row at a time. To access a SQL Server table in your application in the browse mode,

you must use one of the following two options:

The

statement that you use to access the data from your SQL Server table must

end with the keywords. When you turn on the

option to use

browse mode, temporary tables are created.

You must run the following Transact-SQL statement to turn on the browse mode by using

the

option:

７

Note

You can't use the

in a

statement that includes the

option.

７

Note

When the unique index key columns of a table are nullable, and the table is on the inner

side of an outer join, browse mode doesn't support the index.

When you turn on the

option, all the

statements behave as if the

option is appended to the statements. However, the

option

doesn't create the temporary tables that the

option generally uses to send

the results to your application.

When you try to access the data from SQL Server tables in browse mode by using a

query that involves an

statement, and when a unique index is defined on the table

that's present on the inner side of an

statement, the browse mode doesn't support

the unique index. The browse mode supports the unique index only when all unique index key

columns can accept

values. The browse mode doesn't support the unique index if the

following conditions are true:

You try to access the data from SQL Server tables in browse mode by using a

query that involves an

statement.

A unique index is defined on the table that's present on the inner side of an

statement.

To reproduce this behavior in the browse mode, follow these steps:

1. In SQL Server Management Studio, create a database named.

2. In the

database, create a

table and a

table that both contain a

single column named. Define a unique index on the

column in the

table,

and set the column to accept

values. To do this, run the following Transact-SQL

statements in an appropriate query window:

3. Insert several values in the

table and the

table. Make sure that you insert a

value in the

table. To do this, run the following Transact-SQL statements in

the query window:

### Results

4. Turn on the

option. To do this, run the following Transact-SQL statements

in the query window:

5. Access the data in the

table and the

table by using an outer join statement

in the

query. Make sure that the

table is on the inner side of the outer join

statement. To do this, run the following Transact-SQL statements in the query window:

Notice the following output in the

pane:

Output

After you run the

query to access the tables in the browse mode, the result set of the

query contains two

values for the

column in the

table because of the

definition of the

statement. Therefore, in the result set, you can't distinguish

between the

values that came from the table and the

values that the

statement introduced. You might receive incorrect results if the query must ignore the

values from the result set.

７

Note

```sql
FOR BROWSE
```

`SELECT`

```sql
FOR BROWSE
```

`SELECT`

`UNION`

`SELECT`

```sql
FOR BROWSE
```

```sql
FOR BROWSE
```

`NO_BROWSETABLE`

```sql
{
AUTO
|
PATH
}
[
[ ,
ROOT
[ (
'RootName'
) ] ]
[ ,
INCLUDE
_
NULL
_
VALUES
]
[ ,
WITHOUT
_
ARRAY
_
WRAPPER
]
]
}
```

```sql
<lock_hint> HOLDLOCK
```

`SELECT`

```sql
FOR
BROWSE
```

`NO_BROWSETABLE`

`SELECT`

```sql
FOR BROWSE
```

`NO_BROWSETABLE`

```sql
FOR BROWSE
```

`SELECT`

```sql
OUTER JOIN
```

```sql
OUTER JOIN
```

`NULL`

`SELECT`

```sql
OUTER JOIN
```

```sql
OUTER JOIN
```

`SampleDB`

`SampleDB`

`tleft`

`tright`

`c1`

`c1`

`tleft`

`NULL`

`tleft`

`tright`

`NULL`

`tleft`

```sql
SET
NO_BROWSETABLE
ON
;
CREATE
TABLE tleft (c1
INT
NULL
UNIQUE
);
GO
CREATE
TABLE tright (c1
INT
NULL
);
GO
```

`NO_BROWSETABLE`

`tleft`

`tright`

`SELECT`

`tleft`

`SELECT`

`SELECT`

`NULL`

`c1`

`tleft`

```sql
RIGHT OUTER JOIN
```

`NULL`

`NULL`

```sql
RIGHT OUTER
JOIN
```

`NULL`

```sql
INSERT
INTO tleft
VALUES (2);
INSERT
INTO tleft
VALUES (
NULL
);
INSERT
INTO tright
VALUES (1);
INSERT
INTO tright
VALUES (3);
INSERT
INTO tright
VALUES (
NULL
);
SET
NO_BROWSETABLE
ON
;
SELECT tleft.c1
FROM tleft
RIGHT
OUTER
JOIN tright
ON tleft.c1 = tright.c1
WHERE tright.c1 <> 2;
c1
---
NULL
NULL
```
