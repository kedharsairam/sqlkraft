---
title: "Query Tuning Assistant"
topic: "upgrade"
description: |
  Article

  •

  03/28/2025

  Applies to:

  SQL Server 2016 (13.x) and later versions

  When migrating from an older version of SQL Server to SQL Server 2014 (12.x) or later versions,

  and

  upgrading the data
tags:
  - "upgrade"
  - "query-tuning-assistant"
pubDate: 2025-12-01
---

Article

•

03/28/2025

Applies to:

SQL Server 2016 (13.x) and later versions

When migrating from an older version of SQL Server to SQL Server 2014 (12.x) or later versions,

and

upgrading the database compatibility level

to the latest available, a workload might be

exposed to the risk of performance regression. This is also possible to a lesser degree when

upgrading between SQL Server 2014 (12.x) and any newer version.

In SQL Server 2014 (12.x) and later versions, all query optimizer changes are gated to the latest

database compatibility level, so execution plans aren't changed right at point of upgrade but

rather when a user changes the

database option to the latest available.

For more information on query optimizer changes introduced in SQL Server 2014 (12.x), see

Cardinality Estimation (SQL Server)

. For more information about compatibility levels and how

they can affect upgrades, see

Compatibility Levels and Database Engine Upgrades

.

This gating capability provided by the database compatibility level, in combination with Query

Store gives you a great level of control over the query performance in the upgrade process if

the upgrade follows the recommended workflow seen in the next diagram. For more

information on the recommended workflow for upgrading the compatibility level, see

Change

the database compatibility level and use the Query Store

.

This control over upgrades was further improved with SQL Server 2017 (14.x) where

automatic

tuning

was introduced and allows automating the last step in the recommended workflow.

Starting with SQL Server Management Studio v18, the

feature

guides users through the recommended workflow to keep performance stability during

upgrades to newer SQL Server versions, as documented in the section

Keep performance

stability during the upgrade to newer SQL Server

of

Query Store Usage Scenarios

. However, QTA

doesn't roll back to a previously known good plan as seen in the last step of the recommended

workflow. Instead, QTA tracks any regressions found in the

Query Store



```cmd
COMPATIBILITY_LEVEL
```
