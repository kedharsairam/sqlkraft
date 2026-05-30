---
title: "Option: Use a GUID as the leading key column of the index"
topic: "index-architecture"
description: "The following table definition can be used to generate a modulo that aligns to the number of"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

SQL

The following table definition can be used to generate a modulo that aligns to the number of

CPUs,

is generated using the sequentially increasing value

to ensure

a uniform distribution across the B-Tree:

SQL

If there's no natural separator, then a GUID column can be used as a leading key column of the

index to ensure uniform distribution of inserts. While using the GUID as the leading column in

Ensure that you thoroughly test any changes in a test environment before running in a

production environment.

```sql
HashValue
```

```sql
TransactionID
```

```sql
CREATE
TABLE
table1
(
TransactionID
BIGINT
NOT
NULL
,
UserID
INT
NOT
NULL
,
SomeInt
INT
NOT
NULL
);
GO
ALTER
TABLE
table1
ADD
CONSTRAINT
pk_table1 PRIMARY
KEY
CLUSTERED (UserID, TransactionID);
GO
CREATE
TABLE
table1
(
TransactionID
BIGINT
NOT
NULL
,
UserID
INT
NOT
NULL
,
SomeInt
INT
NOT
NULL
);
GO
-- Consider using bulk loading techniques to speed it up
ALTER
TABLE
table1
ADD
[HashValue]
AS
(
CONVERT
(
TINYINT
,
ABS
([TransactionID]) % (32))) PERSISTED
NOT
NULL
;
ALTER
TABLE
table1
ADD
CONSTRAINT
pk_table1 PRIMARY
KEY
CLUSTERED (HashValue, TransactionID,
UserID);
GO
```
