---
title: "Administer & monitor"
topic: "change-data-capture"
description: "08/22/2025 This topic describes how to administer and monitor change data capture for SQL Server and Azure SQL Managed Instance. For Azure SQL D"
tags: ["change-data-capture","administer-monitor"]
pubDate: 2025-12-01
---

This topic describes how to administer and monitor change data capture for SQL Server and.

For Azure SQL Database, which uses a different job mechanism, see

CDC with Azure SQL

Database.

The capture job is initiated by running the parameterless stored procedure. This stored procedure starts by extracting the configured values for

,

,

, and

for the capture job from. These configured values are then passed as parameters to the stored

procedure. This is used to invoke

to perform the log scan.

To understand capture job behavior, you must understand how the configurable parameters

are used by.

The

parameter specifies the maximum number of transactions that can be processed

in a single scan cycle of the log. If during the scan the number of transactions to be processed

reaches this limit, no additional transactions are included in the current scan. After a scan cycle

is complete, the number of transactions that were processed will always be less than or equal

to.

The

parameter specifies the maximum number of scan cycles that are attempted to

drain the log before either returning (continuous = 0) or executing a waitfor (continuous = 1).

```sql
sp_MScdc_capture_job maxtrans maxscans continuous pollinginterval msdb.dbo.cdc_jobs sp_cdc_scan sp_replcmds sp_cdc_scan maxtrans maxtrans maxscans
```
