---
title: sys.dm_db_stats_properties
name: sys.dm_db_stats_properties
category: execution
description:
pubDate: 2026-05-29
---

The following example selects from table

with a predicate on column

.

SQL

The following example looks at the previously created statistic on table

and column

for the histogram step matching the predicate in the query above.

SQL

DBCC SHOW_STATISTICS (Transact-SQL)

Object Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_db_stats_properties (Transact-SQL)

Last updated on 11/18/2025

## Applies to:

## int

## int

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

## Returns properties of statistics for the specified database object (table or indexed view) in the

current SQL Server database. For partitioned tables, see the similar

sys.dm_db_incremental_stats_properties

.

object_id

Is the ID of the object in the current database for which properties of one of its statistics is

requested.

object_id

is

.

stats_id

Is the ID of statistics for the specified

object_id

. The statistics ID can be obtained from the

sys.stats

dynamic management view.

stats_id

is

.

object_id

ID of the object (table or indexed view) for which to return the

properties of the statistics object.

stats_id

ID of the statistics object. Is unique within the table or indexed

view. For more information, see

sys.stats (Transact-SQL)

.

last_updated

Date and time the statistics object was last updated. For more

information, see the

## Remarks

section in this page.

rows

Total number of rows in the table or indexed view when statistics

were last updated. If the statistics are filtered or correspond to a

ﾉ

## sys.dm_db_stats_properties

## object_id

## stats_id

## sys.dm_db_stats_properties

## sys.objects

## sys.stats

filtered index, the number of rows might be less than the

number of rows in the table.

rows_sampled

Total number of rows sampled for statistics calculations.

steps

Number of steps in the histogram. For more information, see

DBCC SHOW_STATISTICS (Transact-SQL)

.

unfiltered_rows

Total number of rows in the table before applying the filter

expression (for filtered statistics). If statistics are not filtered,

unfiltered_rows is equal to the value returns in the rows column.

modification_counter

Total number of modifications for the leading statistics column

(the column on which the histogram is built) since the last time

statistics were updated.

Memory-optimized tables: starting SQL Server 2016 (13.x) and in

Azure SQL Database this column contains: total number of

modifications for the table since the last time statistics were

updated or the database was restarted.

persisted_sample_percent

Persisted sample percentage used for statistic updates that do

not explicitly specify a sampling percentage. If value is zero, then

no persisted sample percentage is set for this statistic.

SQL Server 2016 (13.x) SP1 CU4

returns an empty rowset under any of the following conditions:

or

is NULL.

The specified object is not found or does not correspond to a table or indexed view.

The specified statistics ID does not correspond to existing statistics for the specified

object ID.

The current user does not have permissions to view the statistics object.

This behavior allows for the safe usage of

when cross applied to

rows in views such as

and

.

Statistics update date is stored in the

statistics blob object

together with the

histogram

and

density vector

, not in the metadata. When no data is read to generate statistics data, the

statistics blob is not created, the date is not available, and the

last_updated

column is NULL.

This is the case for filtered statistics for which the predicate does not return any rows, or for

new empty tables.

```sql
Region
```

```sql
Region_Name
```

```sql
Region
```

```sql
Region_Name
```

```sql
SELECT
*
FROM
Region
WHERE
Region_Name =
'Canada'
;
SELECT
ss.name,
ss.stats_id,
shr.steps,
shr.rows,
shr.rows_sampled,
shr.modification_counter,
shr.last_updated,
sh.range_rows,
sh.equal_rows
FROM
sys.stats
AS
ss
INNER
JOIN
sys.stats_columns
AS
sc
ON
ss.stats_id = sc.stats_id
AND
ss.object_id = sc.object_id
INNER
JOIN
sys.all_columns
AS
ac
ON
ac.column_id = sc.column_id
AND
ac.object_id = sc.object_id
CROSS
APPLY
sys.dm_db_stats_properties(ss.object_id, ss.stats_id)
AS
shr
CROSS
APPLY
sys.dm_db_stats_histogram(ss.object_id, ss.stats_id)
AS
sh
WHERE
ss.[object_id] = OBJECT_ID(
'Region'
)
AND
ac.name =
'Region_Name'
AND
sh.range_high_key =
CAST
(
'Canada'
AS
CHAR
(8));
```

```sql
sys.dm_db_stats_properties (object_id, stats_id)
```
