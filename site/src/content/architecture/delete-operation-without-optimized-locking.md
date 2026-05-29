---
title: 'Delete operation without optimized locking'
topic: 'locking'
description: 'ensures that no new names beginning with the letter'
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

for

ensures that no new names beginning with the letter

can be added after

, such

as

.

If a query within a transaction attempts to select a row that doesn't exist, issuing the query at a

later point within the same transaction has to return the same result. No other transaction can be

allowed to insert that nonexistent row. For example, given this query:

SQL

A key-range lock is placed on the index entry corresponding to the name range from

to

because the name

would be inserted between these two adjacent index entries. The

mode key-range lock is placed on the index entry

. This prevents any other

transaction from inserting values, such as

, between the index entries

and

.

When deleting a row within a transaction, the range the row falls into doesn't have to be locked

for the duration of the transaction performing the delete operation. Locking the deleted key

value until the end of the transaction is sufficient to maintain serializability. For example, given

this

statement:

SQL

An exclusive (

) lock is placed on the index entry corresponding to the name

. Other

transactions can insert or delete values before or after the row with the value

that's being

deleted. However, any transaction that attempts to read, insert, or delete rows matching the

value

is blocked until the deleting transaction either commits or rolls back. (The

７

Note

The number of

locks held is

n

+1, where

n

is the number of rows that satisfy the

query.

```sql
Dale
```

```sql
C
```

```sql
Carlos
```

```sql
Clive
```

```sql
Ben
```

```sql
Bing
```

```sql
Bill
```

```sql
RangeS-S
```

```sql
Bing
```

```sql
Bill
```

```sql
Ben
```

```sql
Bing
```

```sql
DELETE
```

```sql
X
```

```sql
Bob
```

```sql
Bob
```

```sql
Bob
```

```sql
RangeS-S
```

```sql
SELECT
name
FROM
mytable
WHERE
name
=
'Bill'
;
```

```sql
DELETE
mytable
WHERE
name
=
'Bob'
;
```
