---
title: "Performance considerations for indexes with included columns"
topic: "index-architecture"
description: "Regardless of the presence of included columns, index key columns must follow the"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

Regardless of the presence of included columns, index key columns must follow the

existing index size restrictions of 16 key columns maximum, and a total index key size of

900 bytes.

Consider redesigning nonclustered indexes with a large index key size so that only columns

used in query predicates, aggregations, and sorts are key columns. Make all other columns that

cover the query included nonkey columns. In this way, you have all columns needed to cover

the query, but the index key itself is small and efficient.

For example, assume that you want to design an index to cover the following query.

SQL

To cover the query, each column must be defined in the index. Although you could define all

columns as key columns, the key size would be 334 bytes. Because the only column used as

search criteria is the

column, having a length of 30 bytes, a better index design

would define

as the key column and include all other columns as nonkey columns.

The following statement creates an index with included columns to cover the query.

SQL

To validate that the index covers the query, create the index, then

display the estimated

execution plan

. If the execution plan shows an

operator for the

index, the query is covered by the index.

Avoid creating indexes with a very large number of included columns. Even though the index

might be covering for more queries, its performance benefit is decreased because:

### varchar(max)

### nvarchar(max)

### varbinary(max)

### xml

```sql
PostalCode
```

```sql
PostalCode
```

```sql
IX_Address_PostalCode
```

```sql
SELECT
AddressLine1,
AddressLine2,
City,
StateProvinceID,
PostalCode
FROM
Person.Address
WHERE
PostalCode
BETWEEN
N
'98000'
AND
N
'99999'
;
CREATE
INDEX
IX_Address_PostalCode
ON
Person.Address (PostalCode)
INCLUDE
(AddressLine1, AddressLine2, City, StateProvinceID);
```
