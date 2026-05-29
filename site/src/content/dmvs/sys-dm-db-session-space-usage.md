---
name: 'sys.dm_db_session_space_usage'
title: 'sys.dm_db_session_space_usage'
category: 'execution'
description: 'Number of pages reserved or allocated for user'
pubDate: 2026-05-29
---

Number of pages reserved or allocated for user

objects by this task.

Number of pages deallocated and no longer reserved

for user objects by this task.

Number of pages reserved or allocated for internal

objects by this task.

Number of pages deallocated and no longer reserved

for internal objects by this task.

: Azure Synapse Analytics, Analytics Platform

System (PDW)

The identifier for the node that this distribution is on.

On SQL Server and SQL Managed Instance, requires

permission.

On SQL Database

,

, and

service objectives, and for databases in

, the

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

either the

permission on the database, or membership in the

server role is required.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

IAM pages are not included in any of the page counts reported by this view.

Page counters are initialized to zero (0) at the start of a request. These values are aggregated at

the session level when the request is completed. For more information, see

sys.dm_db_session_space_usage (Transact-SQL)

.

Work table caching, temporary table caching, and deferred drop operations affect the number

of pages allocated and deallocated in a specified task.

The following objects are included in the user object page counters:

User-defined tables and indexes

System tables and indexes

Global temporary tables and indexes

Local temporary tables and indexes

Table variables

Tables returned in the table-valued functions

Internal objects are only in

. The following objects are included in the internal object

page counters:

Work tables for cursor or spool operations and temporary large object (LOB) storage

Work files for operations such as a hash join

Sort runs

One-to-one

One-to-one

Dynamic Management Views and Functions (Transact-SQL)

Database Related Dynamic Management Views (Transact-SQL)

sys.dm_exec_sessions (Transact-SQL)

sys.dm_exec_requests (Transact-SQL)

sys.dm_os_tasks (Transact-SQL)

sys.dm_db_session_space_usage (Transact-SQL)

sys.dm_db_file_space_usage (Transact-SQL)

Last updated on 11/18/2025

ﾉ

SQL Server 2017 (14.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric


## Returns detailed information about automatic tuning recommendations. For more information,
see

Automatic tuning

.

Unique name of recommendation.

The name of the automatic tuning option that

produced the recommendation, for example,

.

Reason why this recommendation was provided.

The first time this recommendation was generated.

The last time this recommendation was generated.

JSON document that describes the state of the

recommendation. The following fields are available:

-

- current state of the

recommendation.

-

- constant that describes why the

recommendation is in the current state.

1 = The recommendation can be executed against

the database via Transact-SQL script.

0 = The recommendation can't be executed against

the database (for example: information only or

reverted recommendation).

1 = The recommendation can be automatically

monitored and reverted by Database engine.

0 = The recommendation can't be automatically

monitored and reverted. Most

executable

actions are

revertable

.

Date the recommendation is applied.

Duration of the execute action.

ﾉ

= User manually forced plan in the

recommendation.

= System automatically applied

recommendation.

Date the recommendation was applied.

Date the recommendation was reverted.

Duration of the revert action.

= User manually unforced recommended plan.

= System automatically reverted

recommendation.

Date the recommendation was reverted.

Estimated value or effect for this recommendation on

the 0-100 scale (the larger the better).

A JSON document that contains more details about

the recommendation. The following fields are

available.

:

-

-

of the regressed query.

-

-

of the regressed plan.

-

- Number of

executions of the query with regressed plan before

the regression is detected.

-

- Number of detected

errors during the execution of the regressed plan.

-

- Average CPU time

(in microseconds) consumed by the regressed query

before the regression is detected.

-

- Standard deviation of

CPU time consumed by the regressed query before

the regression is detected.

-

-

of the plan that

should be forced.

-

- Number of

executions of the query with the plan that should be

forced before the regression is detected.

-

- Number of detected

errors during the execution of the plan that should be

forced.

-

- Average CPU time

(in microseconds) consumed by the query executed

with the plan that should be forced (calculated before

the regression is detected).

-

Standard deviation

of CPU time consumed by the regressed query before

the regression is detected.

:

-

- The method that should be used to correct

the regression. Value is always

.

-

- Transact-SQL script that should be

executed to force the recommended plan.

The information returned by

is updated when the database

engine identifies a potential query performance regression, and it isn't persisted. The database

engine keeps recommendations only until it restarts. Use the

column in

sys.dm_os_sys_info

to find the last database engine startup time. Database administrators

should periodically make backup copies of the tuning recommendation if they want to keep it

after server recycling.

The

field in the

column might have the following values:

Recommendation is active and not yet applied. User can take recommendation script and

execute it manually.

Recommendation is applied by Database Engine and internal verification process compares

performance of the forced plan with the regressed plan.

Recommendation is successfully applied.

Recommendation is reverted because there are no significant performance gains.

Recommendation has expired and can't be applied anymore.

The JSON document in the

column contains the reason that describes why the

recommendation is in the current state. Values in the reason field might be:

ﾉ

Recommendation expired because the schema of a referenced table

changed. A new recommendation is created if a new query plan

regression is detected on the new schema.

Recommendation expired due to the statistic change on a

referenced table. A new recommendation is created if a new query

plan regression is detected based on new statistics.

Recommended plan can't be forced on a query. Find the

in the

sys.query_store_plan

view to find

the reason of the failure.

option is disabled by the user during

verification process. Enable

option using

ALTER DATABASE SET AUTOMATIC_TUNING

statement or force the

plan manually using the script in the

column.

Plan can't be forced on the query. Examples of unsupported queries

are cursors and

statement.

Recommendation is successfully applied.

Database Engine identified potential performance regression, but

the

option isn't enabled. For more

information, see

ALTER DATABASE SET AUTOMATIC_TUNING

. Apply

recommendation manually or enable

option.

Verification process is aborted due to the restart or Query Store

cleanup.

Query is recompiled because there's no significant performance

improvement.

User manually forced the plan using

sp_query_store_force_plan

procedure. Database engine won't apply the recommendation if

user explicitly decided to force some plan.

User manually unforced the plan using

sp_query_store_unforce_plan

procedure. Since the user explicitly reverted the recommended plan,

database engine keeps using the current plan and generates a new

recommendation if some plan regression occurs in future.

User manually forced different plan using

sp_query_store_force_plan

procedure. Database engine won't apply the recommendation if

user explicitly decided to force some plan.

A temporary table that was used in the plan is changed.

ﾉ

```sql
VIEW SERVER STATE
```

```sql
##MS_ServerStateReader##
```

```sql
VIEW DATABASE STATE
```

```sql
##MS_ServerStateReader##
```

```sql
tempdb
```

```sql
dm_db_task_space_usage.request_id
dm_exec_requests.request_id
```

```sql
dm_db_task_space_usage.session_id
dm_exec_requests.session_id
```

```sql
name
```

```sql
type
```

```sql
FORCE_LAST_GOOD_PLAN
```

```sql
reason
```

```sql
valid_since
```

```sql
last_refresh
```

```sql
state
```

```sql
currentValue
```

```sql
reason
```

```sql
is_executable_action
```

```sql
is_revertable_action
```

```sql
execute_action_start_time
```

```sql
execute_action_duration
```

```sql
execute_action_initiated_by
```

```sql
User
```

```sql
System
```

```sql
execute_action_initiated_time
```

```sql
revert_action_start_time
```

```sql
revert_action_duration
```

```sql
revert_action_initiated_by
```

```sql
User
```

```sql
System
```

```sql
revert_action_initiated_time
```

```sql
score
```

```sql
details
```

```sql
planForceDetails
```

```sql
queryId
```

```sql
query_id
```

```sql
regressedPlanId
```

```sql
plan_id
```

```sql
regressedPlanExecutionCount
```

```sql
regressedPlanAbortedCount
```

```sql
regressedPlanCpuTimeAverage
```

```sql
regressedPlanCpuTimeStddev
```

```sql
recommendedPlanId
```

```sql
plan_id
```

```sql
recommendedPlanExecutionCount
```

```sql
recommendedPlanAbortedCount
```

```sql
recommendedPlanCpuTimeAverage
```

```sql
recommendedPlanCpuTimeStddev
```

```sql
implementationDetails
```

```sql
method
```

```sql
TSql
```

```sql
script
```

```sql
sys.dm_db_tuning_recommendations
```

```sql
sqlserver_start_time
```

```sql
currentValue
```

```sql
state
```

```sql
Active
```

```sql
Verifying
```

```sql
Success
```

```sql
Reverted
```

```sql
Expired
```

```sql
state
```

```sql
SchemaChanged
```

```sql
StatisticsChanged
```

```sql
ForcingFailed
```

```sql
last_force_failure_reason
```

```sql
AutomaticTuningOptionDisabled
FORCE_LAST_GOOD_PLAN
```

```sql
FORCE_LAST_GOOD_PLAN
```

```sql
details
```

```sql
UnsupportedStatementType
```

```sql
INSERT BULK
```

```sql
LastGoodPlanForced
```

```sql
AutomaticTuningOptionNotEnabled
```

```sql
FORCE_LAST_GOOD_PLAN
```

```sql
FORCE_LAST_GOOD_PLAN
```

```sql
VerificationAborted
```

```sql
VerificationForcedQueryRecompile
```

```sql
PlanForcedByUser
```

```sql
PlanUnforcedByUser
```

```sql
UserForcedDifferentPlan
```

```sql
TempTableChanged
```
