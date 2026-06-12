---
name: "Syntax for memory-optimized tables"
title: "Syntax for memory-optimized tables"
category: "statements"
description: "For more information, see:"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

For more information, see:

ALTER TABLE column_constraint (Transact-SQL)

ALTER TABLE column_definition (Transact-SQL)

ALTER TABLE computed_column_definition (Transact-SQL)

ALTER TABLE index_option (Transact-SQL)

ALTER TABLE table_constraint (Transact-SQL)

```sql
|
ONLINE
= {
ON
[(
<low_priority_lock_wait>
) ] |
OFF
}
}
<low_priority_lock_wait>
::=
{
WAIT
_
AT
_
LOW
_
PRIORITY (
MAX
_
DURATION
=
<time>
[
MINUTES
],
ABORT
_
AFTER
_
WAIT
= {
NONE
|
SELF
|
BLOCKERS
} )
}
```

```sql
ALTER
TABLE
{ database_name.schema_name.table_name | schema_name.table_name |
table_name }
{
ALTER
COLUMN column_name
{
[ type_schema_name. ] type_name
[ (
{
precision [ , scale ]
}
) ]
[
COLLATE collation_name ]
[
NULL
|
NOT
NULL
]
}
|
ALTER
INDEX index_name
{
[ type_schema_name. ] type_name
REBUILD
[ [
NONCLUSTERED
]
WITH (
BUCKET
_
COUNT
= bucket_count )
]
}
|
ADD
{
<column_definition>
|
<computed_column_definition>
|
<table_constraint>
|
<table_index>
```

```sql
|
<column_index>
} [ ,.n ]
|
DROP
[ {
CONSTRAINT
[
IF
EXISTS
]
{
constraint_name
} [ ,.n ]
|
INDEX
[
IF
EXISTS
]
{
index_name
} [ ,.n ]
|
COLUMN
[
IF
EXISTS
]
{
column_name
} [ ,.n ]
|
PERIOD
FOR
SYSTEM
_
TIME
} [ ,.n ] ]
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
| constraint_name [ ,.n ] }
| {
ENABLE
|
DISABLE
}
TRIGGER
{
ALL
| trigger_name [ ,.n ] }
|
SWITCH
[ [
PARTITION
] source_partition_number_expression ]
TO target_table
[
PARTITION target_partition_number_expression ]
[
WITH (
<low_priority_lock_wait>
) ]
}
[ ; ]
-- ALTER TABLE options
< table_constraint >
::=
[
CONSTRAINT constraint_name ]
{
{
PRIMARY
KEY
|
UNIQUE
}
{
NONCLUSTERED (column [
ASC
|
DESC
] [ ,. n ])
|
NONCLUSTERED
HASH (column [ ,. n ] )
WITH (
BUCKET
_
COUNT
= bucket_count )
}
|
FOREIGN
KEY ( column [ ,.n ] )
REFERENCES referenced_table_name [ ( ref_column [ ,.n ] ) ]
|
CHECK ( logical_expression )
}
<column_index>
::=
INDEX index_name
{ [
NONCLUSTERED
] | [
NONCLUSTERED
]
HASH
WITH (
BUCKET
_
COUNT
= bucket_count) }
<table_index>
::=
INDEX index_name
```
