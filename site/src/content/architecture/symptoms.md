---
title: 'Symptoms'
topic: 'query-processing'
description: 'Periodic spikes in CPU were observed, which pushed the CPU utilization to nearly 100%. A'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Periodic spikes in CPU were observed, which pushed the CPU utilization to nearly 100%. A

divergence between throughput and CPU consumption was observed leading up to the

problem. By the time that the large CPU spike occurred, a pattern of a large number of spins

occurring during times of heavy CPU usage at particular intervals was established.

This was an extreme case in which the contention was such that it created a spinlock convoy

condition. A convoy occurs when threads can no longer make progress servicing the workload

but instead spend all processing resources attempting to gain access to the lock. The

performance monitor log illustrates this divergence between transaction log throughput and

CPU consumption and, ultimately, the large spike in CPU utilization.

After querying

to determine the existence of significant contention

on

, an extended events script was used to measure the number of backoff

events for the spinlock types of interest.

ﾉ

Expand table

### Script

14,752,117

942,869,471,526

63,914

67,900,620

69,267,367

473,760,338,765

6,840

2,167,281

5,765,761

260,885,816,584

45,247

3,739,208

2,802,773

9,767,503,682

3,485

350,997

1,207,007

3,692,845,572

3,060

109,746

The most straightforward way to quantify the impact of the spins is to look at the number of

backoff events exposed by

over the same 1-minute interval for the

spinlock type(s) with the highest number of spins. This method is best to detect significant

contention because it indicates when threads are exhausting the spin limit while waiting to

acquire the spinlock. The following script illustrates an advanced technique that utilizes

extended events to measure related backoff events and identify the specific code paths where

the contention lies.

For more information about Extended Events in SQL Server, see

Extended Events overview

.

SQL

By analyzing the output, we can see the call stacks for the most common code paths for the

spins. The script was run a couple of different times during the time when CPU

utilization was high to check for consistency in the call stacks returned. The call stacks with the

highest slot bucket count are common between the two outputs (35,668 and 8,506). These call

stacks have a slot count that is two orders of magnitude greater than the next highest entry.

This condition indicates a code path of interest.

### Output 1

XML

７

Note

It isn't uncommon to see call stacks returned by the previous script. When the script ran

for 1 minute, we observed that call stacks with a slot count of > 1,000 was problematic but

the slot count of > 10,000 was more likely to be problematic since it's a higher slot count.

７

Note

The formatting of the following output has been cleaned for readability purposes.

### Output 2

XML

### Fully Qualified Names:

```sql
sys.dm_os_spinlock_stats
```

```sql
SOS_CACHESTORE
```

```sql
SOS_CACHESTORE
```

```sql
SOS_SUSPEND_QUEUE
```

```sql
LOCK_HASH
```

```sql
MUTEX
```

```sql
SOS_SCHEDULER
```

```sql
sys.dm_os_spinlock_stats
```

```sql
/*
This script is provided "AS IS" with no warranties, and confers no rights.
This script will monitor for backoff events over a given period of time and
capture the code paths (callstacks) for those.
--Find the spinlock types
select map_value, map_key, name from sys.dm_xe_map_values
where name = 'spinlock_types'
order by map_value asc
--Example: Get the type value for any given spinlock type
select map_value, map_key, name from sys.dm_xe_map_values
where map_value IN ('SOS_CACHESTORE', 'LOCK_HASH', 'MUTEX')
Examples:
61LOCK_HASH
144 SOS_CACHESTORE
08MUTEX
*/
--create the even session that will capture the callstacks to a bucketizer
--more information is available in this reference: http://msdn.microsoft.com/en-
us/library/bb630354.aspx
```

```sql
SOS_CACHESTORE
```

```sql
CREATE
EVENT
SESSION
spin_lock_backoff
ON
SERVER
ADD
EVENT
sqlos.spinlock_backoff (
ACTION
(package0.callstack)
WHERE
type
= 61
--LOCK_HASH
OR
TYPE
= 144
--SOS_CACHESTORE
OR
TYPE
= 8
--MUTEX
)
ADD
TARGET package0.asynchronous_bucketizer (
SET
filtering_event_name =
'sqlos.spinlock_backoff'
,
source_type = 1,
source
=
'package0.callstack'
)
WITH
(
MAX_MEMORY = 50 MB,
MEMORY_PARTITION_MODE = PER_NODE
);
--Ensure the session was created
SELECT
*
FROM
sys.dm_xe_sessions
WHERE
name
=
'spin_lock_backoff'
;
--Run this section to measure the contention
ALTER
EVENT
SESSION
spin_lock_backoff
ON
SERVER
STATE =
START
;
--wait to measure the number of backoffs over a 1 minute period
WAITFOR DELAY '00:01:00';
--To view the data
--1. Ensure the sqlservr.pdb is in the same directory as the sqlservr.exe
--2. Enable this trace flag to turn on symbol resolution
DBCC TRACEON (3656, -1);
--Get the callstacks from the bucketizer target
SELECT
event_session_address,
target_name,
execution_count,
cast
(target_data
AS
XML
)
FROM
sys.dm_xe_session_targets xst
INNER
JOIN
sys.dm_xe_sessions xs
ON
(xst.event_session_address = xs.address)
WHERE
xs.name =
'spin_lock_backoff'
;
--clean up the session
ALTER
EVENT
SESSION
spin_lock_backoff
ON
SERVER
STATE =
STOP
;
DROP
EVENT
SESSION
spin_lock_backoff
ON
SERVER
;
```

```sql
<BucketizerTarget
truncated
=
"0"
buckets
=
"256"
>
<Slot
count
=
"35668"
trunc
=
"0"
>
<value>
XeSosPkg::spinlock_backoff::Publish
SpinlockBase::Sleep
SpinlockBase::Backoff
Spinlock
<144,1,0>
::SpinToAcquireOptimistic
SOS_CacheStore::GetUserData
OpenSystemTableRowset
CMEDScanBase::Rowset
CMEDScan::StartSearch
CMEDCatalogOwner::GetOwnerAliasIdFromSid
CMEDCatalogOwner::LookupPrimaryIdInCatalog
CMEDCacheEntryFactory::GetProxiedCacheEntryByAltKey
CMEDCatalogOwner::GetProxyOwnerBySID
CMEDProxyDatabase::GetOwnerBySID
ISECTmpEntryStore::Get
ISECTmpEntryStore::Get
NTGroupInfo::`vector deleting destructor'
</value>
</Slot>
<Slot
count
=
"752"
trunc
=
"0"
>
<value>
XeSosPkg::spinlock_backoff::Publish
SpinlockBase::Sleep
SpinlockBase::Backoff
Spinlock
<144,1,0>
::SpinToAcquireOptimistic
SOS_CacheStore::GetUserData
OpenSystemTableRowset
CMEDScanBase::Rowset
CMEDScan::StartSearch
CMEDCatalogOwner::GetOwnerAliasIdFromSid
CMEDCatalogOwner::LookupPrimaryIdInCatalog
CMEDCacheEntryFactory::GetProxiedCacheEntryByAltKey
CMEDCatalogOwner::GetProxyOwnerBySID
```

```sql
CMEDProxyDatabase::GetOwnerBySID
ISECTmpEntryStore::Get
ISECTmpEntryStore::Get
ISECTmpEntryStore::Get
</value>
</Slot>
<BucketizerTarget
truncated
=
"0"
buckets
=
"256"
>
<Slot
count
=
"8506"
trunc
=
"0"
>
<value>
XeSosPkg::spinlock_backoff::Publish
SpinlockBase::Sleep+c7 [ @ 0+0x0 SpinlockBase::Backoff
Spinlock
<144,1,0>
::SpinToAcquireOptimistic
SOS_CacheStore::GetUserData
OpenSystemTableRowset
CMEDScanBase::Rowset
CMEDScan::StartSearch
CMEDCatalogOwner::GetOwnerAliasIdFromSid
CMEDCatalogOwner::LookupPrimaryIdInCatalog
CMEDCacheEntryFactory::GetProxiedCacheEntryByAltKey
CMEDCatalogOwner::GetProxyOwnerBySID
CMEDProxyDatabase::GetOwnerBySID
ISECTmpEntryStore::Get
ISECTmpEntryStore::Get
NTGroupInfo::`vector deleting destructor'
</value>
</Slot>
<Slot
count
=
"190"
trunc
=
"0"
>
<value>
XeSosPkg::spinlock_backoff::Publish
SpinlockBase::Sleep
SpinlockBase::Backoff
Spinlock
<144,1,0>
::SpinToAcquireOptimistic
SOS_CacheStore::GetUserData
OpenSystemTableRowset
CMEDScanBase::Rowset
CMEDScan::StartSearch
CMEDCatalogOwner::GetOwnerAliasIdFromSid
CMEDCatalogOwner::LookupPrimaryIdInCatalog
CMEDCacheEntryFactory::GetProxiedCacheEntryByAltKey
CMEDCatalogOwner::GetProxyOwnerBySID
CMEDProxyDatabase::GetOwnerBySID
ISECTmpEntryStore::Get
ISECTmpEntryStore::Get
ISECTmpEntryStore::Get
</value>
</Slot>
```
