---
title: "Range scan query"
topic: "query-processing"
description: "To ensure a range scan query is serializable, the same query should return the same results each"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

To ensure a range scan query is serializable, the same query should return the same results each

time it's executed within the same transaction. New rows must not be inserted within the range

scan query by other transactions; otherwise, these become phantom inserts. For example, the

following query uses the table and index in the previous illustration:

Key-range locks are placed on the index entries corresponding to the range of rows where the

name is between the values

and

, preventing new rows qualifying in the previous query

from being added or deleted. Although the first name in this range is

, the

mode

key-range lock on this index entry ensures that no new names beginning with the letter

can be

added before

, such as

. Similarly, the

key-range lock on the index entry



`Adam`

`Dale`

`Adam`

```sql
RangeS-S
```

```sql
A
```

`Adam`

`Abigail`

```sql
RangeS-S
```

```sql
SELECT name
FROM mytable
WHERE name
BETWEEN
'A'
AND
'C'
;
```
