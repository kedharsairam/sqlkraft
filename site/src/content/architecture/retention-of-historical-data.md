---
title: "Retention of historical data"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  With system-versioned temporal tables, the history table migh
tags:
  - "tables"
  - "retention-of-historical-data"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

With system-versioned temporal tables, the history table might increase your database size

more than regular tables, particularly under the following conditions:

You retain historical data for a long period of time

You have an update or delete heavy data modification pattern

A large and ever-growing history table can become an issue both due to pure storage costs,

and imposing a performance tax on temporal querying. Developing a data retention policy for

managing data in the history table is an important aspect of planning and managing the

lifecycle of every temporal table.

Managing temporal table data retention begins with determining the required retention period

for each temporal table. Your retention policy, in most cases, should be part of the business

logic of the application using the temporal tables. For example, applications in data audit and

time travel scenarios have firm requirements regarding how long historical data must be

available for online querying.

Once you determine your data retention period, you should develop a plan for managing

historical data. Decide how and where you store your historical data, and how to delete

historical data that is older than your retention requirements. The following approaches for

managing historical data in the temporal history table are available:

Table partitioning

Custom cleanup script

Retention policy

With each of these approaches, the logic for migrating or cleaning history data is based on the

column that corresponds to end of period in the current table. The end of period value for

each row determines the moment when the row version becomes

closed

, that is, when it lands

in the history table. For example, the condition

specifies that historical data older than one month needs to be removed or moved out

from the history table.

```sql
ValidTo < DATEADD (DAYS, -30, SYSUTCDATETIME ())
```
