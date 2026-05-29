---
name: 'sys.fn_hadr_distributed_ag_replica'
title: 'sys.fn_hadr_distributed_ag_replica'
category: 'system'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["function"]
pubDate: 2026-05-29
---

## Using sys.fn_hadr_distributed_ag_replica

Article

•

09/27/2023

Applies to:

SQL Server 2016 (13.x) and later versions

Used to map a replica in a distributed availability group to the local availability group.

Transact-SQL syntax conventions

'

lag_Id

'

Is the identifier of the distributed availability group.

lag_Id

is type

.

'

replica_id

'

Is the identifier of a replica in the distributed availability group.

replica_id

is type

.


## Returns the following information.

## Description
Unique identifier (GUID) of the local availability group.

ﾉ

Expand table

The following example returns a table with the local availability group identifier that is

associated with the specified distributed availability group and replica.

Always On Availability Groups Functions (Transact-SQL)

Always On Availability Groups (SQL Server)

Distributed Availability Groups (Always On Availability Groups)

CREATE AVAILABILITY GROUP (Transact-SQL)

ALTER AVAILABILITY GROUP (Transact-SQL)

See Also

```sql
sys.fn_hadr_distributed_ag_replica( lag_Id, replica_id )
```

```sql
DECLARE @lagId uniqueidentifier = '4A03D1A8-4AE6-B153-E7E9-ED22A546008D'
DECLARE @replicaId uniqueidentifier = 'D5517513-04A8-FD82-14C6-E684EC913935'
SELECT * FROM sys.fn_hadr_distributed_ag_replica(@lagId, @replicaId)
GO
```
