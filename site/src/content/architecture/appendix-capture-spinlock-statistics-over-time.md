---
title: "Appendix: Capture spinlock statistics over time"
topic: "locking"
description: "The following script can be used to look at spinlock statistics over a specific time period. Each"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

The following script can be used to look at spinlock statistics over a specific time period. Each

time it runs it will return the delta between the current values and previous values collected.

SQL

Performance monitoring and tuning tools

Related content

```sql
PRINT '
SQL
Server
PID:
' + convert(VARCHAR(6), @PID);
--Loop to monitor the spinlocks and capture dumps. while (@dump_count <
@max_dumps)
BEGIN
EXEC sp_xevent_dump_on_backoffs @sqldumper_path = @sqldumper_path,
@dump_threshold = @dump_threshold,
@total_delay_time_seconds = @total_delay_time_seconds,
@PID = @PID,
@output_path = @output_path,
@dump_captured_flag = @flag OUTPUT
IF (@flag > 0)
SET @dump_count = @dump_count + 1
PRINT '
Dump
Count
:
' + convert(VARCHAR(2), @dump_count)
WAITFOR DELAY '
00:00:02
'
END;
```

```sql
/* Snapshot the current spinlock stats and store so that this can be compared over
a time period
Return the statistics between this point in time and the last collection point
in time.
**This data is maintained in tempdb so the connection must persist between each
execution**
**alternatively this could be modified to use a persisted table in tempdb. if
that
is changed code should be included to clean up the table at some point.**
*/
USE
tempdb;
GO
DECLARE
@current_snap_time DATETIME;
DECLARE
@previous_snap_time DATETIME;
SET
@current_snap_time =
GETDATE
();
IF NOT EXISTS (
SELECT
name
FROM
tempdb.sys.sysobjects
WHERE
name
LIKE
'#_spin_waits%'
)
```

```sql
CREATE
TABLE
#_spin_waits (
lock_name
VARCHAR
(128),
collisions
BIGINT
,
spins
BIGINT
,
sleep_time
BIGINT
,
backoffs
BIGINT
,
snap_time DATETIME
);
--capture the current stats
INSERT
INTO
#_spin_waits (
lock_name,
collisions,
spins,
sleep_time,
backoffs,
snap_time
)
SELECT
name
,
collisions,
spins,
sleep_time,
backoffs,
@current_snap_time
FROM
sys.dm_os_spinlock_stats;
SELECT
TOP 1 @previous_snap_time = snap_time
FROM
#_spin_waits
WHERE
snap_time < (
SELECT
max
(snap_time)
FROM
#_spin_waits
)
ORDER
BY
snap_time
DESC
;
--get delta in the spin locks stats
SELECT
TOP 10 spins_current.lock_name,
(spins_current.collisions - spins_previous.collisions)
AS
collisions,
(spins_current.spins - spins_previous.spins)
AS
spins,
(spins_current.sleep_time - spins_previous.sleep_time)
AS
sleep_time,
(spins_current.backoffs - spins_previous.backoffs)
AS
backoffs,
spins_previous.snap_time
AS
[start_time],
spins_current.snap_time
AS
[end_time],
DATEDIFF
(ss, @previous_snap_time, @current_snap_time)
AS
[seconds_in_sample]
FROM
#_spin_waits spins_current
INNER
JOIN
(
SELECT
*
FROM
#_spin_waits
WHERE
snap_time = @previous_snap_time
) spins_previous
ON
(spins_previous.lock_name = spins_current.lock_name)
WHERE
spins_current.snap_time = @current_snap_time
AND
spins_previous.snap_time = @previous_snap_time
AND
spins_current.spins > 0
ORDER
BY
(spins_current.spins - spins_previous.spins)
DESC
;
```

```sql
--clean up table
DELETE
FROM
#_spin_waits
WHERE
snap_time = @previous_snap_time;
```
