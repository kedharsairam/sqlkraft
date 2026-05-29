---
title: sys.dm_exec_describe_first_result_set
name: sys.dm_exec_describe_first_result_set
category: execution
description:
pubDate: 2026-05-29
---

The following example creates a stored procedure named TestProc2 that returns two result

sets. Then the example demonstrates that

returns

information about the first result set in the procedure, with and without the browse

information.

The following example uses both the sys.procedures system catalog view and the

function to display metadata for the result

sets of all stored procedures in the

database.

sp_describe_first_result_set (Transact-SQL)

sp_describe_undeclared_parameters (Transact-SQL)

sys.dm_exec_describe_first_result_set (Transact-SQL)

Last updated on 11/18/2025

Article

•

02/28/2023

Applies to:

SQL Server 2016 (13.x) and later versions

Holds information about all steps that compose a given PolyBase request or query. It lists one row per query step.

Column Name

Data Type

Description

Range

execution_id

int

execution_id

and

step_index

make up

the key for

this view.

Unique

numeric id

associated

with the

request.

See ID in

sys.dm_exec_requests (Transact-SQL)

.

step_index

int

The position

of this step

in the

sequence of

steps that

make up

the request.

0 to (n-1) for a request with n steps.

operation_type

nvarchar(128)

Type of the

operation

represented

by this step.

'MoveOperation','OnOperation','RandomIDOperation','RemoteOperation','ReturnOperation','ShuffleMoveOperation',

'HadoopShuffleOperation', 'HadoopBroadCastOperation', 'HadoopRoundRobinOperation'

distribution_type

nvarchar(32)

Where the

step is

executing.

'AllComputeNodes','AllDistributions','ComputeNode','Distribution','AllNodes','SubsetNodes','SubsetDistributions','Un

location_type

nvarchar(32)

Where the

step is

executing.

'Compute','Head' or 'DMS'. All data movement steps show 'DMS'.

status

nvarchar(32)

Status of

this step

'Pending', 'Running', 'Complete', 'Failed', 'UndoFailed', 'PendingCancel', 'Cancelled', 'Undone', 'Aborted'

error_id

nvarchar(36)

Unique id of

the error

associated

with this

step, if any

See id of

sys.dm_exec_compute_node_errors (Transact-SQL)

, NULL if no error occurred.

start_time

datetime

Time at

which the

step started

execution

Smaller or equal to current time and larger or equal to end_compile_time of the query to which this step belongs.

end_time

datetime

Time at

which this

step

completed

execution,

was

cancelled,

or failed.

Smaller or equal to current time and larger or equal to start_time, set to NULL for steps currently in execution or que

total_elapsed_time

int

Total

amount of

time the

query step

has been

executing,

Between 0 and the difference between end_time and start_time. 0 for queued steps.

ﾉ

Expand table

```sql
AdventureWorks2025
```

```sql
CREATE PROC TestProc2
AS
SELECT object_id, name FROM sys.objects ;
SELECT name, schema_id, create_date FROM sys.objects ;
GO
SELECT * FROM
sys.dm_exec_describe_first_result_set_for_object(OBJECT_ID('TestProc2'), 0) ;
SELECT * FROM
sys.dm_exec_describe_first_result_set_for_object(OBJECT_ID('TestProc2'), 1) ;
GO
```

```sql
USE AdventureWorks2022;
GO
SELECT p.name, r.*
FROM sys.procedures AS p
CROSS APPLY sys.dm_exec_describe_first_result_set_for_object(p.object_id, 0) AS r;
GO
```
