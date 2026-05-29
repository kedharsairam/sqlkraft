---
title: 'Appendix: Automate memory dump capture'
topic: 'memory-management'
description: 'observed contention points also on the'
tags: ["memory-management", "architecture"]
pubDate: 2026-05-29
---

observed contention points also on the

spinlock type encountered when

not utilizing fully qualified names in calls to stored procedures. Failure to fully qualify

these names results in the need for SQL Server to look up the default schema for the user,

which results in a longer code path required to execute the SQL.

Another example is utilizing parameterized queries and stored

procedure calls to reduce the work needed to generate execution plans. This again results

in a shorter code path for execution.

Contention on certain lock structure or hash bucket collisions is

unavoidable in some cases. Even though the SQL Server engine partitions the majority of

lock structures, there are still times when acquiring a lock results in access the same hash

bucket. For example, an application the accesses the same row by many threads

concurrently (that is, reference data). These types of problems can be approached by

techniques that either scale out this reference data within the database schema or use

optimistic

concurrency control

and

optimized locking

when possible.

The first line of defense in tuning SQL Server workloads is always the standard tuning practices

(for example, indexing, query optimization, I/O optimization, etc.). However, in addition to the

standard tuning one would perform, following practices that reduce the amount of code

needed to perform operations is an important approach. Even when best practices are

followed, there's still a chance that spinlock contention might occur on busy high concurrency

systems. Use of the tools and techniques in this article can help to isolate or rule out these

types of problems and determine when it's necessary to engage the right Microsoft resources

to help.

The following extended events script has proven to be useful to automate the collection of

memory dumps when spinlock contention becomes significant. In some cases, memory dumps

are required to perform a complete diagnosis of the problem or are requested by the

Microsoft teams to perform in-depth analysis.

The following SQL script can be used to automate the process of capturing memory dumps to

help analyze spinlock contention:

SQL

```sql
SOS_CACHESTORE
```

```sql
/*
This script is provided "AS IS" with no warranties, and confers no rights.
Use:    This procedure will monitor for spinlocks with a high number of backoff
events
over a defined time period which would indicate that there is likely
```

```sql
significant
spin lock contention.
Modify the variables noted below before running.
Requires:
xp_cmdshell to be enabled
sp_configure 'xp_cmd', 1
go
reconfigure
go
**********************************************************************************
***********************/
USE
tempdb;
GO
IF object_id('sp_xevent_dump_on_backoffs') IS NOT NULL
DROP
PROCEDURE
sp_xevent_dump_on_backoffs;
GO
CREATE
PROCEDURE
sp_xevent_dump_on_backoffs (
@sqldumper_path
NVARCHAR
(
max
) =
'"c:\Program Files\Microsoft SQL
Server\100\Shared\SqlDumper.exe"'
,
@dump_threshold
INT
= 500,
--capture mini dump when the slot count for the top
bucket exceeds this
@total_delay_time_seconds
INT
= 60,
--poll for 60 seconds
@PID
INT
= 0,
@output_path
NVARCHAR
(
MAX
) =
'c:\',
@dump_captured_flag INT = 0 OUTPUT
)
AS
/*
--Find the spinlock types
select map_value, map_key, name from sys.dm_xe_map_values
where name = '
spinlock_types
'
order by map_value asc
--Example: Get the type value for any given spinlock type
select map_value, map_key, name from sys.dm_xe_map_values
where map_value IN ('
SOS_CACHESTORE
', '
LOCK_HASH
', '
MUTEX
')
*/
IF EXISTS (
SELECT *
FROM sys.dm_xe_session_targets xst
INNER JOIN sys.dm_xe_sessions xs
ON (xst.event_session_address = xs.address)
WHERE xs.name = '
spinlock_backoff_with_dump
'
)
DROP EVENT SESSION spinlock_backoff_with_dump
ON SERVER
CREATE EVENT SESSION spinlock_backoff_with_dump ON SERVER
ADD EVENT sqlos.spinlock_backoff (
ACTION(package0.callstack) WHERE type = 61 --LOCK_HASH
```

```sql
--or type = 144           --SOS_CACHESTORE
--or type = 8             --MUTEX
--or type = 53            --LOGCACHE_ACCESS
--or type = 41            --LOGFLUSHQ
--or type = 25            --SQL_MGR
--or type = 39            --XDESMGR
) ADD target package0.asynchronous_bucketizer (
SET filtering_event_name = '
sqlos.spinlock_backoff
',
source_type = 1,
source = '
package0.callstack
'
)
WITH (
MAX_MEMORY = 50 MB,
MEMORY_PARTITION_MODE = PER_NODE
)
ALTER EVENT SESSION spinlock_backoff_with_dump ON SERVER STATE = START;
DECLARE @instance_name NVARCHAR(MAX) = @@SERVICENAME;
DECLARE @loop_count INT = 1;
DECLARE @xml_result XML;
DECLARE @slot_count BIGINT;
DECLARE @xp_cmdshell NVARCHAR(MAX) = NULL;
--start polling for the backoffs
PRINT '
Polling
for
:
' + convert(VARCHAR(32), @total_delay_time_seconds) + '
seconds
';
WHILE (@loop_count < CAST(@total_delay_time_seconds / 1 AS INT))
BEGIN
WAITFOR DELAY '
00:00:01
'
--get the xml from the bucketizer for the session
SELECT @xml_result = CAST(target_data AS XML)
FROM sys.dm_xe_session_targets xst
INNER JOIN sys.dm_xe_sessions xs
ON (xst.event_session_address = xs.address)
WHERE xs.name = '
spinlock_backoff_with_dump
';
--get the highest slot count from the bucketizer
SELECT @slot_count = @xml_result.value(N'
(//Slot/@
count
)[1]
', '
int
');
--if the slot count is higher than the threshold in the one minute period
--dump the process and clean up session
IF (@slot_count > @dump_threshold)
BEGIN
PRINT '
exec xp_cmdshell
''' + @sqldumper_path + '
' +
convert(NVARCHAR(max), @PID) + '
0 0x800 0 c:\
'''
SELECT @xp_cmdshell = '
exec xp_cmdshell
''' + @sqldumper_path + '
' +
convert(NVARCHAR(max), @PID) + '
0 0x800 0
' + @output_path + '
'''
EXEC sp_executesql @xp_cmdshell
PRINT '
loop
count
:
' + convert(VARCHAR(128), @loop_count)
```

```sql
PRINT '
slot
count
:
' + convert(VARCHAR(128), @slot_count)
SET @dump_captured_flag = 1
BREAK
END
--otherwise loop
SET @loop_count = @loop_count + 1
END;
--see what was collected then clean up
DBCC TRACEON (3656, -1);
SELECT event_session_address,
target_name,
execution_count,
cast(target_data AS XML)
FROM sys.dm_xe_session_targets xst
INNER JOIN sys.dm_xe_sessions xs
ON (xst.event_session_address = xs.address)
WHERE xs.name = '
spinlock_backoff_with_dump
';
ALTER EVENT SESSION spinlock_backoff_with_dump ON SERVER STATE = STOP;
DROP EVENT SESSION spinlock_backoff_with_dump ON SERVER;
GO
/* CAPTURE THE DUMPS
******************************************************************/
--Example: This will run continuously until a dump is created.
DECLARE @sqldumper_path NVARCHAR(MAX) = '"c:\Program Files\Microsoft SQL
Server\100\Shared\SqlDumper.exe"';
DECLARE @dump_threshold INT = 300; --capture mini dump when the slot count for the
top bucket exceeds this
DECLARE @total_delay_time_seconds INT = 60; --poll for 60 seconds
DECLARE @PID INT = 0;
DECLARE @flag TINYINT = 0;
DECLARE @dump_count TINYINT = 0;
DECLARE @max_dumps TINYINT = 3; --stop after collecting this many dumps
DECLARE @output_path NVARCHAR(max) = '
c:\
'; --no spaces in the path please :)
--Get the process id for sql server
DECLARE @error_log TABLE (
LogDate DATETIME,
ProcessInfo VARCHAR(255),
TEXT VARCHAR(max)
);
INSERT INTO @error_log
EXEC ('
xp_readerrorlog 0, 1,
''
Server
Process
ID
''');
SELECT @PID = convert(INT, (REPLACE(REPLACE(TEXT, '
Server
Process
ID
is
', ''),
'
.
', '')))
FROM @error_log
WHERE TEXT LIKE ('
Server
Process
ID
is
%
');
```
