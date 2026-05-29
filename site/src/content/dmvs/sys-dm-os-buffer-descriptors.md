---
title: sys.dm_os_buffer_descriptors
name: sys.dm_os_buffer_descriptors
category: execution
description:
pubDate: 2026-05-29
---

numa_node

Nonuniform Memory Access node for the buffer. Is nullable.

read_microsec

The actual time (in microseconds) required to read the page into the

buffer. This number is reset when the buffer is reused. Is nullable.

is_in_bpool_extension

1 = Page is in buffer pool extension. Is nullable.

pdw_node_id

: Azure Synapse Analytics, Analytics Platform System (PDW)

The identifier for the node that this distribution is on.

On SQL Server and SQL Managed Instance, requires

permission.

On SQL Database

,

, and

service objectives, and for databases in

, the

server

admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

either the

permission on the database, or membership in the

server role is required.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

sys.dm_os_buffer_descriptors returns pages that are being used by the Resource database.

sys.dm_os_buffer_descriptors does not return information about free or stolen pages, or about

pages that had errors when they were read.

sys.dm_os_buffer_descriptors

sys.databases

database_id

many-to-one

sys.dm_os_buffer_descriptors

<userdb>.sys.allocation_units

allocation_unit_id

many-to-one

sys.dm_os_buffer_descriptors

<userdb>.sys.database_files

file_id

many-to-one

sys.dm_os_buffer_descriptors

sys.dm_os_buffer_pool_extension_configuration

file_id

many-to-one

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
