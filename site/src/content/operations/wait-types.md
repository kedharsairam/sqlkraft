---
title: "Wait types"
topic: "high-availability"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  When troubleshooting Always On Availability Groups latency, wait statistics can be monitored
  
  for accumulation using the availability groups-specific w
tags:
  - "high-availability"
  - "wait-types"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

When troubleshooting Always On Availability Groups latency, wait statistics can be monitored

for accumulation using the availability groups-specific wait types in the dynamic management

view (DMV)

sys.dm_os_wait_stats (Transact-SQL)

.

For general information on using wait statistics, see

SQL Server 2005 Waits and Queues

. That

document was written for SQL Server 2005, but its information can be applied to later SQL

Server versions.

Use the T-SQL query below to retrieve all wait statistics with the availability groups wait types:

SQL

To monitor the wait statistics by capturing extended events, use the following T-SQL command.

SQL

You can view the key-value mapping of the wait type by running the following query:

SQL

```cmd
SELECT
*
FROM
sys.dm_os_wait_stats
WHERE
wait_type
LIKE
'%hadr%'
ORDER
BY
wait_time_ms
DESC
CREATE
EVENT
SESSION
[alwayson]
ON
SERVER
ADD
EVENT
sqlos.wait_info(
WHERE
([wait_type]=(758)
OR
[wait_type]=(776)
OR
[wait_type]=(853)
OR
[wait_type]=(833)))
WITH
(MAX_MEMORY=4096
KB,EVENT_RETENTION_MODE=ALLOW_SINGLE_EVENT_LOSS,MAX_DISPATCH_LATENCY=30
SECONDS
,
MAX_EVENT_SIZE=0
KB,MEMORY_PARTITION_MODE=
NONE
,TRACK_CAUSALITY=
OFF
,STARTUP_STATE=
OFF
)
GO
SELECT
*
FROM
sys.dm_xe_map_values
WHERE
name
=
'wait_types'
AND
map_value
LIKE
'%hadr%'
```