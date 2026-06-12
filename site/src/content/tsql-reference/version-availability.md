---
name: "Version availability"
title: "Version availability"
category: "statements"
description: "Syntax for Azure Synapse Analytics and Analytics Platform System (PDW):"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Syntax for Azure Synapse Analytics and Analytics Platform System (PDW):

## syntaxsql

Some of the options aren't available in all database engine versions. The following table shows

the versions when the options are introduced in clustered columnstore and nonclustered

columnstore indexes:

2016 (13.x)

2016 (13.x)

2016 (13.x)

2016 (13.x)

2019 (15.x)

2017 (14.x)

clause

N/A

2016 (13.x)

clause

2016 (13.x)

2025 (17.x)

All options are available in Azure SQL Database and Azure SQL Managed Instance.

For more detail on feature availability, see

What's new in columnstore indexes.

Expand table

AUTD

`COMPRESSION_DELAY`

`DATA_COMPRESSION`

`ONLINE`

`WHERE`

`ORDER`

```sql
|
COMPRESSION
_
DELAY
= { 0 | delay [
MINUTES
] }
|
DATA
_
COMPRESSION
= {
COLUMNSTORE
|
COLUMNSTORE
_
ARCHIVE
}
[
ON
PARTITIONS ( { partition_number_expression | range } [ ,.n ] ) ]
<on_option>
::=
partition_scheme_name ( column_name )
| filegroup_name
|
"default"
<filter_expression>
::=
column_name
IN ( constant [ ,.n ]
| column_name {
IS
|
IS
NOT
| = |
<>
| != | > | >= | !> |
< | <= | !< } constant
)
CREATE
CLUSTERED
COLUMNSTORE
INDEX index_name
ON
{ database_name.schema_name.table_name | schema_name.table_name | table_name
}
[
ORDER ( column [ ,.n ] ) ]
[
WITH (
DROP
_
EXISTING
= {
ON
|
OFF
} ) ]
-- default is OFF
[;]
```
