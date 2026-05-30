---
name: "Convert binary and varbinary data"
title: "Convert binary and varbinary data"
category: "data-types"
description: "Azure SQL Managed Instance"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Binary data types of either fixed length or variable length.

Fixed-length binary data with a length of

n

bytes, where

n

is a value from 1 through 8,000. The

storage size is

n

bytes.

Variable-length binary data.

n

can be a value from 1 through 8,000.

indicates that the

maximum storage size is 2^31-1 bytes. The storage size is the actual length of the data entered

- 2 bytes. The data that is entered can be 0 bytes in length. The ANSI SQL synonym for

is

.

The default length is 1 when

n

isn't specified in a data definition or variable declaration

statement. When

n

isn't specified with the

function, the default length is 30.

the sizes of the column data entries are consistent.

the sizes of the column data entries vary considerably.

the column data entries exceed 8,000 bytes.

When converting data from a string data type to a

or

data type of unequal

length, SQL Server pads or truncates the data on the right. These string data types are:



Expand table

### char

### varchar

### nchar

### nvarchar

### binary

### varbinary

### text

### ntext

### image

### binary

### varbinary

### binary

### varbinary

### binary

### int

### smallint

### tinyint

### binary

### varbinary

### binary

### binary

When other data types are converted to

or

, the data is padded or truncated

on the left. Padding is achieved by using hexadecimal zeros.

Converting data to the

and

data types is useful if

data is the easiest

way to move around data. At some point, you might convert a value type to a binary value of

large enough size and then convert it back. This conversion always results in the same value if

both conversions are taking place on the same version of SQL Server. The binary

representation of a value might change from version to version of SQL Server.

You can convert

,

, and

to

or

. If you convert the

value back to an integer value, this value is different from the original integer value if

truncation occurred. For example, the following SELECT statement shows that the integer value

is stored as a binary

:

SQL

However, the following

statement shows that if the

target is too small to hold

the entire value, the leading digits are silently truncated so that the same number is stored as

:

SQL

The following batch shows that this silent truncation can affect arithmetic operations without

raising an error:

SQL

### binary

The final result is

, not

.

CAST and CONVERT (Transact-SQL)

Data Type Conversion (Database Engine)

Data Types (Transact-SQL)

Last updated on 11/21/2025

７

Note

Conversions between any data type and the

data types are not guaranteed to be

the same between versions of SQL Server.

Related content

```sql
CAST
```

```sql
123456
```

```sql
0x0001e240
```

```sql
SELECT
```

```sql
0xe240
```

```sql
SELECT
CAST
( 123456
AS
BINARY
(4) );
SELECT
CAST
( 123456
AS
BINARY
(2) );
DECLARE
@BinaryVariable2
BINARY
(2);
SET
@BinaryVariable2 = 123456;
```

```sql
57921
```

```sql
123457
```

```sql
SET
@BinaryVariable2 = @BinaryVariable2 + 1;
SELECT
CAST
( @BinaryVariable2
AS
INT
);
GO
```
