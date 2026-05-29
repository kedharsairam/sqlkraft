---
title: "Unique index design guidelines"
topic: "index-architecture"
description: "Fewer index rows fit on a page. This increases disk I/O and reduces cache efficiency."
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

Fewer index rows fit on a page. This increases disk I/O and reduces cache efficiency.

More disk space is required to store the index. In particular, adding

,

,

, or

data types in included columns can significantly

increase disk space requirements. This is because the column values are copied into the

index leaf level. Therefore, they reside in both the index and the base table.

Data modification performance decreases because many columns must be modified both

in the based table and in the nonclustered index.

You have to determine whether the gains in query performance outweigh the decrease in data

modification performance and the increase in disk space requirements.

A unique index guarantees that the index key contains no duplicate values. Creating a unique

index is only possible when uniqueness is a characteristic of the data itself. For example, if you

want to make sure that the values in the

column in the

table are unique, when the primary key is

, create a

constraint on the

column. The constraint rejects any attempt to

introduce rows with duplicate national ID numbers.

With multicolumn unique indexes, the index guarantees that each combination of values in the

index key is unique. For example, if a unique index is created on a combination of

,

, and

columns, no two rows in the table could have the same values for

these columns.

Both clustered and nonclustered indexes can be unique. You can create a unique clustered

index and multiple unique nonclustered indexes on the same table.

The benefits of unique indexes include:

Business rules that require data uniqueness are enforced.

Additional information helpful to the query optimizer is provided.

Creating a

or

constraint automatically creates a unique index on the

specified columns. There are no significant differences between creating a

constraint

and creating a unique index independent of a constraint. Data validation occurs in the same

manner and the query optimizer doesn't differentiate between a unique index created by a

constraint or manually created. However, you should create a

or

constraint

on the column when the enforcement of business rules is the goal. By doing this, the objective

of the index is clear.

### Improved query performance and plan quality

### Reduced index update costs

```sql
NationalIDNumber
```

```sql
HumanResources.Employee
```

```sql
EmployeeID
```

```sql
UNIQUE
```

```sql
NationalIDNumber
```

```sql
LastName
```

```sql
FirstName
```

```sql
MiddleName
```

```sql
PRIMARY KEY
```

```sql
UNIQUE
```

```sql
UNIQUE
```

```sql
UNIQUE
```

```sql
PRIMARY KEY
```
