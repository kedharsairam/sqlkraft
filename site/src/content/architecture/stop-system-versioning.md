---
title: "Stop system-versioning"
topic: "tables"
description: ""
tags: ["tables","stop-system-versioning"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

You might want to stop versioning on your temporal table either temporarily or permanently.

You can do that by setting the

clause to.

Stop system-versioning if you want to perform specific maintenance operations on a temporal

table or don't need a versioned table anymore. Because of this operation, you get two

independent tables:

Current table with a period definition

History table as a regular table

The history table stops capturing the updates during.

No data loss happens on the temporal table when you set

or drop

the

period.

When you set

and don't remove drop the

period, the

system continues to update the period columns for every insert and update operation. Deletes

on the current table are permanent.

You must drop the

period to delete the period columns. To remove the period

columns, use. For more information, see

Change the

schema of a system-versioned temporal table.

When you set

, all users with sufficient permissions can modify the

schema and content of the history table, or even permanently delete the history table.

You can't set

if you have other objects created with

using temporal query extensions, such as referencing. This restriction prevents

these objects from failing if you set.

```sql
SYSTEM_VERSIONING
OFF
SYSTEM_VERSIONING = OFF
SYSTEM_VERSIONING = OFF
SYSTEM_TIME
SYSTEM_VERSIONING = OFF
SYSTEM_TIME
SYSTEM_TIME
ALTER TABLE <table> DROP <column>;
SYSTEM_VERSIONING = OFF
SYSTEM_VERSIONING = OFF
SCHEMABINDING
SYSTEM_TIME
SYSTEM_VERSIONING = OFF
```
