---
name: "sys.sp_monitor"
title: "sp_monitor"
category: "general"
description: "Displays statistics about SQL Server. Number of elapsed seconds since Number of seconds that the server computer's CPU has done SQL Server work. Number of seconds that SQL Server spent doing input and output operations. Number of seconds that SQL Server was idle."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  USE
      master
      ;
      GO
      EXECUTE
      sp_monitor;
      last_run                   current_run                seconds
      2024-05-01 15:27:51.287    2024-08-21 17:20:34.097    9683563
      cpu_busy           io_busy         idle
      14452(14451)-0%    2555(2554)-0%   4371742(4371629)-45%
      packets_received       packets_sent    packet_errors
      18032(17993)           64572(64533)    0(0)
      total_read     total_write   total_errors    connections
      1593(1593)     4687(4687)    0(0)            155625(155557)
---

## Description

Displays statistics about SQL Server. Number of elapsed seconds since Number of seconds that the server computer's CPU has done SQL Server work. Number of seconds that SQL Server spent doing input and output operations. Number of seconds that SQL Server was idle.

## Syntax

```sql
USE master
;
GO
EXECUTE sp_monitor;
last_run current_run seconds
----------------------- ----------------------- ---------
2024-05-01 15:27:51.287 2024-08-21 17:20:34.097 9683563 cpu_busy io_busy idle
--------------- ------------- --------------------
14452(14451)-0% 2555(2554)-0% 4371742(4371629)-45%
packets_received packets_sent packet_errors
---------------- ------------ -------------
18032(17993) 64572(64533) 0(0) total_read total_write total_errors connections
----------- ----------- ------------- --------------
1593(1593) 4687(4687) 0(0) 155625(155557)
```

## Examples

### Example 1

```sql
@@PACK_RECEIVED
```

### Example 2

```sql
@@
PACK
_
RECEIVED
```

### Example 3

```sql
SELECT
@@PACK_RECEIVED
AS
'Packets Received'
;
Packets Received
----------------
128
```

### Example 4

```sql
@@
CONNECTIONS
```

### Example 5

```sql
SELECT
GETDATE ()
AS
'Today''s Date and Time'
,
@@CONNECTIONS
AS
'Login Attempts'
;
```

### Example 6

```sql
Today's Date and Time Login Attempts
---------------------- --------------
12/5/2006 10:32:45 AM 211023
```

### Example 7

`float`

### Example 8

```sql
@@
IDLE
```

### Example 9

```sql
SELECT
@@IDLE *
CAST (@@TIMETICKS
AS float
)
AS
'Idle microseconds'
,
GETDATE ()
AS
'as of'
;
I
Idle microseconds as of
----------------- ----------------------
8199934 12/5/2006 10:23:00 AM
```

### Example 10

```sql
@@PACK_SENT
```

_(. and 13 more examples)_
