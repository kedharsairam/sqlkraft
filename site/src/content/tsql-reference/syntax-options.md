---
name: "Syntax options"
title: "Syntax options"
category: "statements"
description: "Azure SQL Managed Instance"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Common syntax

## Full syntax

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Creates a new table in the database.

Transact-SQL syntax conventions

Simple CREATE TABLE syntax (common if not using options):

## syntaxsql

Disk-based CREATE TABLE syntax:

## syntaxsql

７

Note

For reference to Warehouse in Microsoft Fabric, visit

. For reference to Azure Synapse Analytics and Analytics Platform System

(PDW), visit

.

## Syntax for memory optimized tables

Memory optimized CREATE TABLE syntax:

## syntaxsql

```sql
CREATE
TABLE
{ database_name.schema_name.table_name | schema_name.table_name | table_name }
( {
<column_definition>
} [ ,... n ] )
[ ; ]
```

```sql
CREATE
TABLE
{ database_name.schema_name.table_name | schema_name.table_name | table_name }
[
AS
F
ile
T
able ]
( {
<column_definition>
|
<computed_column_definition>
|
<column_set_definition>
| [
<table_constraint>
] [ ,... n ]
| [
<table_index>
] }
[ ,... n ]
[
PERIOD
FOR
SYSTEM
_
TIME
( system_start_time_column_name
```

```sql
, system_end_time_column_name ) ]
)
[
ON
{ partition_scheme_name ( partition_column_name )
| filegroup
|
"default"
} ]
[
TEXTIMAGE
_
ON
{ filegroup |
"default"
} ]
[
FILESTREAM
_
ON
{ partition_scheme_name
| filegroup
|
"default"
} ]
[
WITH
(
<table_option>
[ ,... n ] ) ]
[ ; ]
<column_definition>
::=
column_name
<data_type>
[
FILESTREAM
]
[
COLLATE
collation_name ]
[
SPARSE
]
[
MASKED
WITH
(
FUNCTION
=
'mask_function'
) ]
[ [
CONSTRAINT
constraint_name ]
DEFAULT
constant_expression ]
[
IDENTITY
[ ( seed , increment ) ] ]
[
NOT
FOR
REPLICATION
]
[
GENERATED
ALWAYS
AS
{
ROW
|
TRANSACTION
_
ID
|
SEQUENCE
_
NUMBER
} {
START
|
END
}
[
HIDDEN
] ]
[ [
CONSTRAINT
constraint_name ] {
NULL
|
NOT
NULL
} ]
[
ROWGUIDCOL
]
[
ENCRYPTED
WITH
(
COLUMN
_
ENCRYPTION
_
KEY
= key_name ,
ENCRYPTION
_
TYPE
= {
DETERMINISTIC
|
RANDOMIZED
} ,
ALGORITHM
=
'AEAD_AES_256_CBC_HMAC_SHA_256'
) ]
[
<column_constraint>
[ ,... n ] ]
[
<column_index>
]
<data_type>
::=
[ type_schema_name. ] type_name
[ ( precision [ , scale ] | max |
[ {
CONTENT
|
DOCUMENT
} ] xml_schema_collection ) ]
<column_constraint>
::=
[
CONSTRAINT
constraint_name ]
{
{
PRIMARY
KEY
|
UNIQUE
}
[
CLUSTERED
|
NONCLUSTERED
]
[ (
<column_name>
[ ,... n ] ) ]
[
WITH
FILLFACTOR
= fillfactor
|
WITH
(
<index_option>
[ ,... n ] )
]
[
ON
{ partition_scheme_name ( partition_column_name )
| filegroup |
"default"
} ]
| [
FOREIGN
KEY
]
REFERENCES
[ schema_name. ] referenced_table_name [ ( ref_column ) ]
[
ON
DELETE
{
NO
ACTION
|
CASCADE
|
SET
NULL
|
SET
DEFAULT
} ]
[
ON
UPDATE
{
NO
ACTION
|
CASCADE
|
SET
NULL
|
SET
DEFAULT
} ]
```

```sql
[
NOT
FOR
REPLICATION
]
|
CHECK
[
NOT
FOR
REPLICATION
] ( logical_expression )
}
<column_index>
::=
INDEX
index_name [
CLUSTERED
|
NONCLUSTERED
]
[
WITH
(
<index_option>
[ ,... n ] ) ]
[
ON
{ partition_scheme_name ( column_name )
| filegroup_name
| default
}
]
[
FILESTREAM
_
ON
{ filestream_filegroup_name | partition_scheme_name |
"NULL"
} ]
<computed_column_definition>
::=
column_name
AS
computed_column_expression
[
PERSISTED
[
NOT
NULL
] ]
[
[
CONSTRAINT
constraint_name ]
{
PRIMARY
KEY
|
UNIQUE
}
[
CLUSTERED
|
NONCLUSTERED
]
[
WITH
FILLFACTOR
= fillfactor
|
WITH
(
<index_option>
[ ,... n ] )
]
[
ON
{ partition_scheme_name ( partition_column_name )
| filegroup |
"default"
} ]
| [
FOREIGN
KEY
]
REFERENCES
referenced_table_name [ ( ref_column ) ]
[
ON
DELETE
{
NO
ACTION
|
CASCADE
} ]
[
ON
UPDATE
{
NO
ACTION
} ]
[
NOT
FOR
REPLICATION
]
|
CHECK
[
NOT
FOR
REPLICATION
] ( logical_expression )
]
<column_set_definition>
::=
column_set_name
XML
COLUMN
_
SET
FOR
ALL
_
SPARSE
_
COLUMNS
<table_constraint>
::=
[
CONSTRAINT
constraint_name ]
{
{
PRIMARY
KEY
|
UNIQUE
}
[
CLUSTERED
|
NONCLUSTERED
]
( column_name [
ASC
|
DESC
] [ ,... n ] )
[
WITH
FILLFACTOR
= fillfactor
|
WITH
(
<index_option>
[ ,... n ] )
]
[
ON
{ partition_scheme_name (partition_column_name)
| filegroup |
"default"
} ]
|
FOREIGN
KEY
( column_name [ ,... n ] )
```

```sql
REFERENCES
referenced_table_name [ ( ref_column [ ,... n ] ) ]
[
ON
DELETE
{
NO
ACTION
|
CASCADE
|
SET
NULL
|
SET
DEFAULT
} ]
[
ON
UPDATE
{
NO
ACTION
|
CASCADE
|
SET
NULL
|
SET
DEFAULT
} ]
[
NOT
FOR
REPLICATION
]
|
CHECK
[
NOT
FOR
REPLICATION
] ( logical_expression )
}
<table_index>
::=
{
{
INDEX
index_name [
UNIQUE
] [
CLUSTERED
|
NONCLUSTERED
]
( column_name [
ASC
|
DESC
] [ ,... n ] )
|
INDEX
index_name
CLUSTERED
COLUMNSTORE
[
ORDER
(column_name [ , ...n ] ) ]
|
INDEX
index_name [
NONCLUSTERED
]
COLUMNSTORE
( column_name [ ,... n ] )
}
[
INCLUDE
( column_name [ ,... n ] ) ]
[
WHERE
<filter_predicate>
]
[
WITH
(
<index_option>
[ ,... n ] ) ]
[
ON
{ partition_scheme_name ( column_name )
| filegroup_name
| default
}
]
[
FILESTREAM
_
ON
{ filestream_filegroup_name | partition_scheme_name |
"NULL"
} ]
}
<table_option>
::=
{
[
DATA
_
COMPRESSION
= {
NONE
|
ROW
|
PAGE
}
[
ON
PARTITIONS
( {
<partition_number_expression>
|
<range>
}
[ ,... n ] ) ] ]
[
XML
_
COMPRESSION
= {
ON
|
OFF
}
[
ON
PARTITIONS
( {
<partition_number_expression>
|
<range>
}
[ ,... n ] ) ] ]
[
FILETABLE
_
DIRECTORY
=
<directory_name>
]
[
FILETABLE
_
COLLATE
_
FILENAME
= {
<collation_name>
| database_default } ]
[
FILETABLE
_
PRIMARY
_
KEY
_
CONSTRAINT
_
NAME
=
<constraint_name>
]
[
FILETABLE
_
STREAMID
_
UNIQUE
_
CONSTRAINT
_
NAME
=
<constraint_name>
]
[
FILETABLE
_
FULLPATH
_
UNIQUE
_
CONSTRAINT
_
NAME
=
<constraint_name>
]
[
SYSTEM
_
VERSIONING
=
ON
[ (
HISTORY
_
TABLE
= schema_name.history_table_name
[ ,
HISTORY
_
RETENTION
_
PERIOD
=
<history_retention_period>
]
[ ,
DATA
_
CONSISTENCY
_
CHECK
= {
ON
|
OFF
} ]
) ]
]
[
REMOTE
_
DATA
_
ARCHIVE
=
{
ON
[ (
<table_stretch_options>
[ ,... n] ) ]
|
OFF
(
MIGRATION
_
STATE
=
PAUSED
)
}
]
[
DATA
_
DELETION
=
ON
{ (
FILTER
_
COLUMN
= column_name,
RETENTION
_
PERIOD
= {
INFINITE
| number {
DAY
|
DAYS
|
WEEK
|
WEEKS
```

```sql
|
MONTH
|
MONTHS
|
YEAR
|
YEARS
} }
) }
]
[
LEDGER
=
ON
[ (
<ledger_option>
[ ,... n ] ) ]
|
OFF
]
}
<ledger_option>
::=
{
[
LEDGER
_
VIEW
= schema_name.ledger_view_name [ (
<ledger_view_option>
[ ,... n ]
) ] ]
[
APPEND
_
ONLY
=
ON
|
OFF
]
}
<ledger_view_option>
::=
{
[
TRANSACTION
_
ID
_
COLUMN
_
NAME
= transaction_id_column_name ]
[
SEQUENCE
_
NUMBER
_
COLUMN
_
NAME
= sequence_number_column_name ]
[
OPERATION
_
TYPE
_
COLUMN
_
NAME
= operation_type_id column_name ]
[
OPERATION
_
TYPE
_
DESC
_
COLUMN
_
NAME
= operation_type_desc_column_name ]
}
<table_stretch_options>
::=
{
[
FILTER
_
PREDICATE
= {
NULL
| table_predicate_function } , ]
MIGRATION
_
STATE
= {
OUTBOUND
|
INBOUND
|
PAUSED
}
}
<index_option>
::=
{
PAD
_
INDEX
= {
ON
|
OFF
}
|
FILLFACTOR
= fillfactor
|
IGNORE
_
DUP
_
KEY
= {
ON
|
OFF
}
|
STATISTICS
_
NORECOMPUTE
= {
ON
|
OFF
}
|
STATISTICS
_
INCREMENTAL
= {
ON
|
OFF
}
|
ALLOW
_
ROW
_
LOCKS
= {
ON
|
OFF
}
|
ALLOW
_
PAGE
_
LOCKS
= {
ON
|
OFF
}
|
OPTIMIZE
_
FOR
_
SEQUENTIAL
_
KEY
= {
ON
|
OFF
}
|
COMPRESSION
_
DELAY
= { 0 | delay [
M
inutes ] }
|
DATA
_
COMPRESSION
= {
NONE
|
ROW
|
PAGE
|
COLUMNSTORE
|
COLUMNSTORE
_
ARCHIVE
}
[
ON
PARTITIONS
( { partition_number_expression |
<range>
}
[ ,... n ] ) ]
|
XML
_
COMPRESSION
= {
ON
|
OFF
}
[
ON
PARTITIONS
( {
<partition_number_expression>
|
<range>
}
[ ,... n ] ) ]
}
<range>
::=
<partition_number_expression>
TO
<partition_number_expression>
```

```sql
CREATE
TABLE
{ database_name.schema_name.table_name | schema_name.table_name | table_name }
( {
<column_definition>
| [
<table_constraint>
] [ ,... n ]
| [
<table_index>
]
[ ,... n ] }
[
PERIOD
FOR
SYSTEM
_
TIME
( system_start_time_column_name
, system_end_time_column_name ) ]
)
[
WITH
(
<table_option>
[ ,... n ] ) ]
[ ; ]
<column_definition>
::=
column_name
<data_type>
[
COLLATE
collation_name ]
[
GENERATED
ALWAYS
AS
ROW
{
START
|
END
} [
HIDDEN
] ]
[
NULL
|
NOT
NULL
]
[ [
CONSTRAINT
constraint_name ]
DEFAULT
memory_optimized_constant_expression ]
| [
IDENTITY
[ ( 1, 1 ) ] ]
[
<column_constraint>
]
[
<column_index>
]
<data_type>
::=
[type_schema_name. ] type_name [ (precision [ , scale ]) ]
<column_constraint>
::=
[
CONSTRAINT
constraint_name ]
{
{
PRIMARY
KEY
|
UNIQUE
}
{
NONCLUSTERED
|
NONCLUSTERED
HASH
WITH
(
BUCKET
_
COUNT
= bucket_count )
}
[ (
<column_name>
[ ,... n ] ) ]
| [
FOREIGN
KEY
]
REFERENCES
[ schema_name. ] referenced_table_name [ ( ref_column ) ]
|
CHECK
( logical_expression )
}
<table_constraint>
::=
[
CONSTRAINT
constraint_name ]
{
{
PRIMARY
KEY
|
UNIQUE
}
{
NONCLUSTERED
( column_name [
ASC
|
DESC
] [ ,... n ])
|
NONCLUSTERED
HASH
( column_name [ ,... n ] )
WITH
(
BUCKET
_
COUNT
=
bucket_count )
}
|
FOREIGN
KEY
( column_name [ ,... n ] )
REFERENCES
referenced_table_name [ ( ref_column [ ,... n ] ) ]
```
