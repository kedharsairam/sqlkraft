---
name: 'sys.dm_exec_plan_attributes'
title: 'sys.dm_exec_plan_attributes'
category: 'execution'
description: 'The following example returns the'
pubDate: 2026-05-29
---

The following example returns the

options with which the plan was compiled. The

for the plan is also returned. The

operator is used to output the

and

attributes as columns rather than as rows. For more information about the

value returned in

, see

sys.dm_exec_plan_attributes

.

SQL

The following example returns a breakdown of the memory used by all compiled plans in the

cache.

SQL

System dynamic management views

Execution Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_exec_query_plan (Transact-SQL)

sys.dm_exec_plan_attributes (Transact-SQL)

sys.dm_exec_sql_text (Transact-SQL)

sys.dm_os_memory_objects (Transact-SQL)

sys.dm_os_memory_cache_entries (Transact-SQL)

FROM clause plus JOIN, APPLY, PIVOT (Transact-SQL)

Last updated on 12/17/2025

Related content

Article

•

02/28/2023

Applies to:

SQL Server 2016 (13.x) and later

Azure SQL Managed Instance


## Returns errors that occur on PolyBase compute nodes.

## Description
error_id

Unique numeric id

associated with the error

.

Unique across all query errors in the

system

source

Source thread or process


## description
type

Type of error.

create_time

The time of the error

occurrence

compute_node_id

Identifier of the specific

compute node

See compute_node_id of

sys.dm_exec_compute_nodes (Transact-

SQL)

rexecution_id

Identifier of the PolyBase

query, if any.

spid

Identifier of the SQL

Server session

thread_id

Numeric identifier of the

thread on which the

error occurred.

details

nvarchar(4000)

Full description of the

details of the error.

compute_pool_id

Unique identifier for the

pool.

ﾉ

Expand table

See Also

PolyBase troubleshooting with dynamic management views

Dynamic Management Views and Functions (Transact-SQL)

Database Related Dynamic Management Views (Transact-SQL)

Article

•

02/28/2023

Applies to:

SQL Server 2016 (13.x) and later

Azure SQL Managed Instance

Holds additional information about the performance and status of all PolyBase nodes. Lists one

row per node.


## Description
compute_node_id

Unique numeric

id associated with

the node.

Unique across scale-out cluster regardless of

type.

process_id

process_name

Logical name of

the node.

Any string of appropriate length.

allocated_memory

Total allocated

memory on this

node.

available_memory

Total available

memory on this

node.

process_cpu_usage

Total process CPU

usage, in ticks.

total_cpu_usage

Total CPU usage,

in ticks.

thread_count

Total number of

threads in use on

this node.

handle_count

Total number of

handles in use on

this node.

total_elapsed_time

Total time

elapsed since

system start or

restart.

Total time elapsed since system start or

restart. If total_elapsed_time exceeds the

maximum value for an integer (24.8 days in

milliseconds), it will cause materialization

ﾉ

Expand table


## Description
failure due to overflow.The maximum value in

milliseconds is equivalent to 24.8 days.

is_available

Flag indicating

whether this

node is available.

sent_time

Last time a

network package

was sent by this

received_time

Last time a

network package

was sent by this

node.

error_id

Unique identifier

of the last error

that occurred on

this node.

compute_pool_id

Unique identifier

for the pool.

PolyBase troubleshooting with dynamic management views

Dynamic Management Views and Functions (Transact-SQL)

Database Related Dynamic Management Views (Transact-SQL)

See Also

SQL)

Article

•

02/28/2023

Applies to:

SQL Server 2016 (13.x) and later versions

Holds information about nodes used with PolyBase data management. It lists one row per

node.

Use this DMV to see the list of all nodes in the scale-out cluster with their role, name and IP

address.


## Description
compute_node_id

Unique numeric id associated with

the node. Key for this view.

Unique across scale-out

cluster regardless of type.

type

Type of the node.

'COMPUTE', 'HEAD'

name

Logical name of the node.

Any string of appropriate

length.

address

IP address of this node.

IP address range

PolyBase troubleshooting with dynamic management views

Dynamic Management Views and Functions (Transact-SQL)

Database Related Dynamic Management Views (Transact-SQL)

ﾉ

Expand table

See Also

## sys.dm_pdw_exec_connections (Transact-SQL)

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

SQL analytics endpoint in Microsoft Fabric

Warehouse in

Microsoft Fabric

SQL database in Microsoft Fabric


## Returns information about the connections established to this instance of the database engine
and the details of each connection. Returns server wide connection information for SQL Server

and Azure SQL Managed Instance. Returns connection information for the current database in

Azure SQL Database. Returns connection information for all databases in the same elastic pool

for databases in

elastic pools

in Azure SQL Database.


## Description
session_id

Identifies the session associated with this connection. Is

nullable.

most_recent_session_id

Represents the session ID for the most recent request

associated with this connection. (SOAP connections can be

reused by another session.) Is nullable.

connect_time

Timestamp when connection was established. Is not

nullable.

net_transport

When MARS is used, returns

for each additional

connection associated with a MARS logical session.

Note:

Describes the physical transport protocol that is used

by this connection. Is not nullable.

protocol_type

Specifies the protocol type of the payload. It currently

distinguishes between TDS ("TSQL"), "SOAP", and "Database

Mirroring". Is nullable.

protocol_version

Version of the data access protocol associated with this

connection. Is nullable.

７

Note

To call this from dedicated SQL pool in Azure Synapse Analytics or Analytics Platform

System (PDW), see

. For serverless SQL pool

or Microsoft Fabric use

.

ﾉ

Expand table


## Description
endpoint_id

An identifier that describes what type of connection it is.

This

can be used to query the

view. Is nullable.

encrypt_option

Boolean value to describe whether encryption is enabled for

this connection. Is not nullable.

For HADR mirroring endpoints, this column always returns

FALSE. Use the

DMV

instead to check if connections to a HADR mirroring

endpoint are encrypted.

auth_scheme

Specifies SQL Server/Windows Authentication scheme used

with this connection. Is not nullable.

node_affinity

Identifies the memory node to which this connection has

affinity. Is not nullable.

num_reads

Number of byte reads that have occurred over this

connection. Is nullable.

num_writes

Number of byte writes that have occurred over this

connection. Is nullable.

last_read

Timestamp when last read occurred over this connection. Is

nullable.

last_write

Timestamp when last write occurred over this connection. Is

nullable.

net_packet_size

Network packet size used for information and data transfer.

Is nullable.

client_net_address

Host address of the client connecting to this server. Is

nullable.

client_tcp_port

Port number on the client computer that is associated with

this connection. Is nullable.

In Azure SQL Database, this column always returns NULL.

local_net_address

Represents the IP address on the server that this connection

targeted. Available only for connections using the TCP

transport provider. Is nullable.

In Azure SQL Database, this column always returns NULL.

local_tcp_port

Represents the server TCP port that this connection targeted

if it were a connection using the TCP transport. Is nullable.

## Basic

## S0

## S1

## elastic pools


## Description
In Azure SQL Database, this column always returns NULL.

connection_id

Identifies each connection uniquely. Is not nullable.

parent_connection_id

Identifies the primary connection that the MARS session is

using. Is nullable.

most_recent_sql_handle

The SQL handle of the last request executed on this

connection. The

column is always in

sync with the

column. Is nullable.

pdw_node_id

: Azure Synapse Analytics, Analytics Platform

System (PDW)

The identifier for the node that this distribution is on.

On SQL Server and SQL Managed Instance, requires

permission.

On Azure SQL Database

,

, and

service objectives, and for databases in

,

the

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


## Permissions for SQL Server 2022 and later
sys.dm_exec_sessions

.

One-to-zero or

one-to-many

sys.dm_exec_requests

.

Many-to-one

sys.dm_broker_connections

.

One-to-one

Most commonly, for each row in

there is a single matching row in

. However, in some cases such as system internal sessions or

Service

Broker

activation procedures, there may be a row in

without a matching

row in

.

When MARS is used, there may be multiple rows in

for a row in

, one row for the parent connection, and one row for each MARS logical

session. The latter rows can be identified by the value in the

column being set

ﾉ

Expand table

## Session

to

. For these connections, the value in the

column of

matches the value in the

column of

for MARS requests in progress.

The following Transact-SQL query gathers information about a query's own connection.

SQL

Learn more about related concepts in the following articles:

Execution Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_exec_sessions (Transact-SQL)

sys.dm_exec_sql_text (Transact-SQL)

sys.dm_pdw_exec_connections (Transact-SQL)

Last updated on 11/18/2025

Next steps

## nvarchar(

## n

## )

## nvarchar(max)

## nvarchar(

## n

## )

## nvarchar(max)

```sql
SET
```

```sql
sql_handle
```

```sql
PIVOT
```

```sql
set_options
```

```sql
sql_handle
```

```sql
set_options
```

```sql
SELECT
plan_handle,
query_plan,
objtype
FROM
sys.dm_exec_cached_plans
CROSS
APPLY
sys.dm_exec_query_plan(plan_handle)
WHERE
objtype =
'Trigger'
;
```

```sql
SELECT
plan_handle,
pvt.set_options,
pvt.sql_handle
FROM
(
SELECT
plan_handle,
epa.attribute,
epa.value
FROM
sys.dm_exec_cached_plans
OUTER
APPLY
sys.dm_exec_plan_attributes(plan_handle)
AS
epa
WHERE
cacheobjtype =
'Compiled Plan'
)
AS
ecpa
PIVOT
(
MAX
(ecpa.value)
FOR
ecpa.attribute
IN
(
"set_options"
,
"sql_handle"
))
AS
pvt;
```

```sql
SELECT
plan_handle,
ecp.memory_object_address
AS
CompiledPlan_MemoryObject,
omo.memory_object_address,
type
,
page_size_in_bytes
FROM
sys.dm_exec_cached_plans
AS
ecp
INNER
JOIN
sys.dm_os_memory_objects
AS
omo
ON
ecp.memory_object_address = omo.memory_object_address
```

```sql
OR
ecp.memory_object_address = omo.parent_address
WHERE
cacheobjtype =
'Compiled Plan'
;
```

```sql
nvarchar(36)
```

```sql
nvarchar(255)
```

```sql
nvarchar(255)
```

```sql
datetime
```

```sql
int
```

```sql
nvarchar(36)
```

```sql
int
```

```sql
int
```

```sql
int
```

```sql
int
```

```sql
int
```

```sql
nvarchar(255)
```

```sql
bigint
```

```sql
bigint
```

```sql
bigint
```

```sql
bigint
```

```sql
bigint
```

```sql
bigint
```

```sql
bigint
```

```sql
bit
```

```sql
datetime
```

```sql
datetime
```

```sql
nvarchar(36)
```

```sql
int
```

```sql
sys.dm_exec_connections
```

```sql
endpoint_id
```

```sql
sys.endpoints
```

```sql
sys.database_mirroring_endpoints
```

```sql
most_recent_sql_handle
```

```sql
most_recent_session_id
```

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
session_id
sys.dm_exec_connections.session_id
```

```sql
connection_id
sys.dm_exec_connections.connection_id
```

```sql
connection_id
sys.dm_exec_connections.connection_id
```

```sql
sys.dm_exec_connections
```

```sql
sys.dm_exec_sessions
```

```sql
sys.dm_exec_sessions
```

```sql
sys.dm_exec_connections
```

```sql
sys.dm_exec_connections
```

```sql
sys.dm_exec_sessions
```

```sql
net_transport
```

```sql
connection_id
```

```sql
sys.dm_exec_connections
```

```sql
connection_id
```

```sql
sys.dm_exec_requests
```

```sql
SELECT
c.session_id, c.net_transport, c.encrypt_option,
c.auth_scheme, s.host_name, s.program_name,
s.client_interface_name, s.login_name, s.nt_domain,
s.nt_user_name, s.original_login_name, c.connect_time,
s.login_time
FROM
sys.dm_exec_connections
AS
c
JOIN
sys.dm_exec_sessions
AS
s
ON
c.session_id = s.session_id
WHERE
c.session_id = @@SPID;
```
