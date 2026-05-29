---
name: 'sys.dm_resource_governor_resource_pools'
title: 'sys.dm_resource_governor_resource_pools'
category: 'execution'
description: 'is successfully executed, the following'
pubDate: 2026-05-29
---

When

is successfully executed, the following

counters are reset:

,

,

,

,

,

,

,

,

,

,

,

,

, and

. The counter

is set to the

current system date and time, and the other counters are set to zero (0).

Requires

permission.

Requires

permission on the server.

Dynamic Management Views and Functions (Transact-SQL)

sys.dm_resource_governor_resource_pools (Transact-SQL)

sys.resource_governor_workload_groups (Transact-SQL)

ALTER RESOURCE GOVERNOR (Transact-SQL)

CREATE WORKLOAD GROUP

Article

•

02/28/2023

SQL Server

This section contains the following dynamic management objects:

sys.dm_audit_actions (Transact-SQL)

sys.dm_audit_class_type_map (Transact-SQL)

sys.dm_cryptographic_provider_algorithms (Transact-SQL)

sys.dm_cryptographic_provider_keys (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_cryptographic_provider_properties (Transact-SQL)

sys.dm_cryptographic_provider_sessions (Transact-SQL)

sys.dm_database_encryption_keys (Transact-SQL)

sys.dm_external_provider_certificate_info (Transact-SQL)

Extensible Key Management (EKM)

Transparent Data Encryption (TDE)

SQL Server Audit (Database Engine)

SQL Server

Azure SQL Database

Azure SQL Managed Instance


## Returns a row for every audit action that can be reported in the audit log and every audit
action group that can be configured as part of SQL Server Audit. For more information about

SQL Server Audit, see

SQL Server Audit (Database Engine)

.

Yes

ID of the audit action. Related to the

value written to each audit record.

Can be

for audit groups.

No

Name of the audit action or action group.

No

The name of the class of the object that the

audit action applies to. Can be any one of the

Server, Database, or Schema scope objects,

but doesn't include Schema objects.

Yes

Identified for informational purposes only.

Not supported. Future compatibility is not

guaranteed.

Yes

Name of the parent class for the object

described by

. Can be

if the

is

.

Yes

Name of the audit action or audit group that

contains the audit action described in this

row. This value is used to create a hierarchy of

actions and covering actions.

Yes

Indicates that the action or action group

specified in this row is configurable at the

Group or Action level. Can be

if the

action isn't configurable.

Yes

The name of the audit group that contains

the specified action. Can be

if the value

in

is a group.

No

Indicates whether an action can be written to

an audit log. Possible values:

ﾉ

= Yes

= No

This view is visible to the public.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

visibility configuration

.

CREATE SERVER AUDIT (Transact-SQL)

ALTER SERVER AUDIT (Transact-SQL)

DROP SERVER AUDIT (Transact-SQL)

CREATE SERVER AUDIT SPECIFICATION (Transact-SQL)

ALTER SERVER AUDIT SPECIFICATION (Transact-SQL)

DROP SERVER AUDIT SPECIFICATION (Transact-SQL)

CREATE DATABASE AUDIT SPECIFICATION (Transact-SQL)

ALTER DATABASE AUDIT SPECIFICATION (Transact-SQL)

DROP DATABASE AUDIT SPECIFICATION (Transact-SQL)

ALTER AUTHORIZATION (Transact-SQL)

sys.fn_get_audit_file (Transact-SQL)

sys.server_audits (Transact-SQL)

sys.server_file_audits (Transact-SQL)

sys.server_audit_specifications (Transact-SQL)

sys.server_audit_specification_details (Transact-SQL)

sys.database_audit_specifications (Transact-SQL)

sys.database_audit_specification_details (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_class_type_map (Transact-SQL)

Create a Server Audit and Server Audit Specification

Last updated on 12/17/2025

SQL Server

Azure SQL Database

Azure SQL Managed Instance


## Returns a table that lists securable classes that can be mapped to the
column in the

audit log. For more information about SQL Server Audit, see

SQL Server Audit (Database

Engine)

.

No

The class type of the entity that was audited. Maps to

the

written to the audit log returned by

the

function.

No

The name of the class of the object that was audited.

Yes

The securable class that maps to the

being audited. Can be

if the

doesn't

map to a securable object. Can be joined with

in

This view is visible to the public.

To use the

function, SQL Server 2019 (15.x) and earlier versions require

permission on the server, while SQL Server 2022 (16.x) and later versions

require

permission on the server.

This SQL Server example reads a locally stored Audit file and joins it with the

view.

SQL

ﾉ

CREATE SERVER AUDIT (Transact-SQL)

ALTER SERVER AUDIT (Transact-SQL)

DROP SERVER AUDIT (Transact-SQL)

CREATE SERVER AUDIT SPECIFICATION (Transact-SQL)

ALTER SERVER AUDIT SPECIFICATION (Transact-SQL)

DROP SERVER AUDIT SPECIFICATION (Transact-SQL)

CREATE DATABASE AUDIT SPECIFICATION (Transact-SQL)

ALTER DATABASE AUDIT SPECIFICATION (Transact-SQL)

DROP DATABASE AUDIT SPECIFICATION (Transact-SQL)

ALTER AUTHORIZATION (Transact-SQL)

sys.fn_get_audit_file (Transact-SQL)

sys.server_audits (Transact-SQL)

sys.server_file_audits (Transact-SQL)

sys.server_audit_specifications (Transact-SQL)

sys.server_audit_specification_details (Transact-SQL)

sys.database_audit_specifications (Transact-SQL)

sys.database_audit_specification_details (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_class_type_map

Create a Server Audit and Server Audit Specification

Last updated on 12/17/2025

```sql
ALTER RESOURCE GOVERNOR RESET STATISTICS
```

```sql
statistics_start_time
```

```sql
total_request_count
```

```sql
total_queued_request_count
```

```sql
total_cpu_limit_violation_count
```

```sql
total_cpu_usage_ms
```

```sql
max_request_cpu_time_ms
```

```sql
total_lock_wait_count
```

```sql
total_lock_wait_time_ms
```

```sql
total_query_optimization_count
```

```sql
total_suboptimal_plan_generation_count
```

```sql
total_reduced_memgrant_count
```

```sql
max_request_grant_memory_kb
```

```sql
peak_tempdb_data_space_kb
```

```sql
total_tempdb_data_limit_violation_count
```

```sql
statistics_start_time
```

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

```sql
action_id
```

```sql
action_id
```

```sql
NULL
```

```sql
name
```

```sql
class_desc
```

```sql
covering_action_name
```

```sql
parent_class_desc
```

```sql
class_desc
```

```sql
NULL
```

```sql
class_desc
```

```sql
Server
```

```sql
covering_parent_action_name
```

```sql
configuration_level
```

```sql
NULL
```

```sql
containing_group_name
```

```sql
NULL
```

```sql
name
```

```sql
action_in_log
```

```sql
1
```

```sql
0
```

```sql
class_type
```

```sql
class_type
```

```sql
class_type
```

```sql
get_audit_file()
```

```sql
class_type_desc
```

```sql
securable_class_desc
```

```sql
class_type
```

```sql
NULL
```

```sql
class_type
```

```sql
class_desc
```

```sql
sys.dm_audit_actions.
```

```sql
sys.fn_get_audit_file
```

```sql
CONTROL SERVER
```

```sql
VIEW SERVER SECURITY AUDIT
```

```sql
sys.dm_audit_class_type_map
```

```sql
SELECT
*
FROM
sys.fn_get_audit_file(
'D:\SQLData\Audits\*.sqlaudit'
,
DEFAULT
,
DEFAULT
)
AS
audit_file
INNER
JOIN
sys.dm_audit_class_type_map
AS
dm_audit_class_type_map
```

```sql
ON
audit_file.class_type = dm_audit_class_type_map.class_type;
GO
```
