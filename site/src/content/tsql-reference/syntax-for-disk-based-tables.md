---
name: "Syntax for disk-based tables"
title: "Syntax for disk-based tables"
category: "statements"
description: "Azure SQL Managed Instance"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure

Synapse Analytics

Analytics Platform System (PDW)

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Modifies a table definition by altering, adding, or dropping columns and constraints.

also reassigns and rebuilds partitions, or disables and enables constraints and triggers.

The syntax for

is different for disk-based tables and memory-optimized tables. Use

the following links to take you directly to the appropriate syntax block for your table types and to

the appropriate syntax examples:

## Syntax

## Examples

## Syntax

Altering Memory-Optimized Tables

For more information about the syntax conventions, see

Transact-SQL syntax conventions

.



Tip

The syntax of

varies in different versions of the

. Use the version selector dropdown list to

.

#### syntaxsql

```sql
ALTER TABLE
```

```sql
ALTER TABLE
```

```sql
ALTER TABLE
```

```sql
ALTER
TABLE
{ database_name.schema_name.table_name | schema_name.table_name |
table_name }
{
ALTER
COLUMN
column_name
{
[ type_schema_name. ] type_name
[ (
```

```sql
{
precision [ , scale ]
| max
| xml_schema_collection
}
) ]
[
COLLATE
collation_name ]
[
NULL
|
NOT
NULL
] [
SPARSE
]
| {
ADD
|
DROP
}
{
ROWGUIDCOL
|
PERSISTED
|
NOT
FOR
REPLICATION
|
SPARSE
|
HIDDEN
}
| {
ADD
|
DROP
}
MASKED
[
WITH
(
FUNCTION
=
' mask_function '
) ]
}
[
WITH
(
ONLINE
=
ON
|
OFF
) ]
| [
WITH
{
CHECK
|
NOCHECK
} ]
|
ADD
{
<column_definition>
|
<computed_column_definition>
|
<table_constraint>
|
<column_set_definition>
} [ ,...n ]
| [ system_start_time_column_name datetime2
GENERATED
ALWAYS
AS
ROW
START
[
HIDDEN
] [
NOT
NULL
] [
CONSTRAINT
constraint_name ]
DEFAULT
constant_expression [
WITH
VALUES
] ,
system_end_time_column_name datetime2
GENERATED
ALWAYS
AS
ROW
END
[
HIDDEN
] [
NOT
NULL
][
CONSTRAINT
constraint_name ]
DEFAULT
constant_expression [
WITH
VALUES
] ,
start_transaction_id_column_name bigint
GENERATED
ALWAYS
AS
TRANSACTION
_
ID
START
[
HIDDEN
]
NOT
NULL
[
CONSTRAINT
constraint_name ]
DEFAULT
constant_expression [
WITH
VALUES
],
end_transaction_id_column_name bigint
GENERATED
ALWAYS
AS
TRANSACTION
_
ID
END
[
HIDDEN
]
NULL
[
CONSTRAINT
constraint_name ]
DEFAULT
constant_expression [
WITH
VALUES
],
start_sequence_number_column_name bigint
GENERATED
ALWAYS
AS
SEQUENCE
_
NUMBER
START
[
HIDDEN
]
NOT
NULL
[
CONSTRAINT
constraint_name ]
DEFAULT
constant_expression [
WITH
VALUES
],
end_sequence_number_column_name bigint
GENERATED
ALWAYS
AS
SEQUENCE
_
NUMBER
END
[
HIDDEN
]
NULL
[
CONSTRAINT
constraint_name ]
DEFAULT
constant_expression [
WITH
VALUES
]
]
PERIOD
FOR
SYSTEM
_
TIME
( system_start_time_column_name,
system_end_time_column_name )
|
DROP
[ {
[
CONSTRAINT
][
IF
EXISTS
]
{
constraint_name
[
WITH
(
<drop_clustered_constraint_option>
[ ,...n ] )
]
```

```sql
} [ ,...n ]
|
COLUMN
[
IF
EXISTS
]
{
column_name
} [ ,...n ]
|
PERIOD
FOR
SYSTEM
_
TIME
} [ ,...n ] ]
| [
WITH
{
CHECK
|
NOCHECK
} ] {
CHECK
|
NOCHECK
}
CONSTRAINT
{
ALL
| constraint_name [ ,...n ] }
| {
ENABLE
|
DISABLE
}
TRIGGER
{
ALL
| trigger_name [ ,...n ] }
| {
ENABLE
|
DISABLE
}
CHANGE
_
TRACKING
[
WITH
(
TRACK
_
COLUMNS
_
UPDATED
= {
ON
|
OFF
} ) ]
|
SWITCH
[
PARTITION
source_partition_number_expression ]
TO
target_table
[
PARTITION
target_partition_number_expression ]
[
WITH
(
<low_priority_lock_wait>
) ]
|
SET
(
[
FILESTREAM
_
ON
=
{ partition_scheme_name | filegroup |
"default"
|
"NULL"
} ]
|
SYSTEM
_
VERSIONING
=
{
OFF
|
ON
[ (
HISTORY
_
TABLE
= schema_name . history_table_name
[,
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
[,
HISTORY
_
RETENTION
_
PERIOD
=
{
INFINITE
| number {
DAY
|
DAYS
|
WEEK
|
WEEKS
|
MONTH
|
MONTHS
|
YEAR
|
YEARS
}
}
]
)
]
}
|
DATA
_
DELETION
=
{
OFF
|
ON
[(  [
FILTER
_
COLUMN
= column_name ]
[,
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
|
MONTH
|
MONTHS
|
YEAR
|
YEARS
} } ]
)]
} )
|
REBUILD
[ [
PARTITION
=
ALL
]
[
WITH
(
<rebuild_option>
[ ,...n ] ) ]
| [
PARTITION
= partition_number
[
WITH
(
<single_partition_rebuild_option>
[ ,...n ] ) ]
```

```sql
]
]
|
<table_option>
|
<filetable_option>
|
<stretch_configuration>
}
[ ; ]
-- ALTER TABLE options
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
<drop_clustered_constraint_option>
::=
{
MAXDOP
= max_degree_of_parallelism
|
ONLINE
= {
ON
|
OFF
}
|
MOVE
TO
{ partition_scheme_name ( column_name ) | filegroup |
"default"
}
}
<table_option>
::=
{
SET
(
LOCK
_
ESCALATION
= {
AUTO
|
TABLE
|
DISABLE
} )
}
<filetable_option>
::=
{
[ {
ENABLE
|
DISABLE
}
FILETABLE
_
NAMESPACE
]
[
SET
(
FILETABLE
_
DIRECTORY
= directory_name ) ]
}
<stretch_configuration>
::=
{
SET
(
REMOTE
_
DATA
_
ARCHIVE
{
=
ON
(
<table_stretch_options>
)
| =
OFF
_
WITHOUT
_
DATA
_
RECOVERY
(
MIGRATION
_
STATE
=
PAUSED
)
| (
<table_stretch_options>
[, ...n] )
}
)
}
<table_stretch_options>
::=
{
[
FILTER
_
PREDICATE
= { null | table_predicate_function } , ]
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
<single_partition_rebuild__option>
::=
{
SORT
_
IN
_
TEMPDB
= {
ON
|
OFF
}
|
MAXDOP
= max_degree_of_parallelism
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
```
