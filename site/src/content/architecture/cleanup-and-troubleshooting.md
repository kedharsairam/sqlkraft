---
title: "Cleanup and troubleshooting"
topic: "change-data-capture"
description: "08/22/2025 This article provides ways to troubleshoot common issues observed in change tracking auto cleanup."
tags: ["change-data-capture","cleanup-and-troubleshooting"]
pubDate: 2025-12-01
---

This article provides ways to troubleshoot common issues observed in change tracking auto

cleanup.

Generally, if the auto cleanup isn't functioning as expected, you can see one or more of the

following symptoms:

High storage consumption by one or more change tracking side tables or the

system table.

Side tables (internal tables whose name begins with prefix

, for example,

) or

or both, show significant number of rows that

are outside of the configured retention period.

table has entries with specific cleanup errors.

performance has degraded over time.

Auto cleanup or manual cleanup reports high CPU usage.

To identify the root cause of a problem with change tracking auto cleanup, use the following

steps to debug and mitigate the issue.

Check if auto cleanup has been running. To check this, query the cleanup history table in the

same database. If the cleanup has been running, the table has entries with the start and end

times of the cleanup. If the cleanup hasn't been running, the table is empty or has stale entries.

If the history table has entries with the tag

in the column

, then the

cleanup is failing due to table level cleanup errors.

```sql
syscommittab change_tracking change_tracking_12345 syscommittab dbo.MSChange_tracking_history
CHANGETABLE cleanup errors comments
SELECT
TOP 1000 *
FROM dbo.MSChange_tracking_history
ORDER
BY start_time
DESC
;
```
