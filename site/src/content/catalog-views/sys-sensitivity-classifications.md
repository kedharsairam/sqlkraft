---
name: 'sys.sensitivity_classifications'
title: 'sys.sensitivity_classifications'
category: 'objects'
description: 'This view provides visibility into the classification state of the database. It can be used for'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

This view provides visibility into the classification state of the database. It can be used for

managing the database classifications, as well as for generating reports.

Currently only classification of database columns is supported.

The following example returns a table that lists the table name, column name, label, label ID,

information type, information type ID, rank, and rank description for each classified column in

the database.

SQL

Requires the

permission.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

７

Note

Label is a keyword for Azure Synapse Analytics.

ADD SENSITIVITY CLASSIFICATION (Transact-SQL)

DROP SENSITIVITY CLASSIFICATION (Transact-SQL)

Getting started with SQL Information Protection

See Also

```sql
SELECT
SCHEMA_NAME(sys.all_objects.schema_id)
as
SchemaName,
sys.all_objects.name
AS
[TableName], sys.all_columns.name
As
[ColumnName],
[Label], [Label_ID], [Information_Type], [Information_Type_ID], [
Rank
],
[Rank_Desc]
FROM
sys.sensitivity_classifications
left
join
sys.all_objects
on
sys.sensitivity_classifications.major_id =
sys.all_objects.object_id
left
join
sys.all_columns
on
sys.sensitivity_classifications.major_id =
sys.all_columns.object_id
and
sys.sensitivity_classifications.minor_id =
sys.all_columns.column_id
```
