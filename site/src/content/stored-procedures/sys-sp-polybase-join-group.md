---
name: "sys.sp_polybase_join_group"
title: "sp_polybase_join_group"
category: "general"
description: "SQL Server 2016 (13.x) and later versions Adds a SQL Server instance as a compute node to a PolyBase group for scale-out computation. The SQL Server instance must have the feature installed. PolyBase enables the integration of non-SQL Server data sources, such as Hadoop and Azure Blob Storage. See also Transact-SQL syntax conventions The name of the machine that hosts the SQL Server head node of t"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_polybase_join_group (
  @head_node_address =
  N
  'head_node_address'
  , @dms_control_channel_port = dms_control_channel_port
  , @head_node_sql_server_instance_name =
  'head_node_sql_server_instance_name'
  )
  [ ; ]
---

## Description

SQL Server 2016 (13.x) and later versions Adds a SQL Server instance as a compute node to a PolyBase group for scale-out computation. The SQL Server instance must have the feature installed. PolyBase enables the integration of non-SQL Server data sources, such as Hadoop and Azure Blob Storage. See also Transact-SQL syntax conventions The name of the machine that hosts the SQL Server head node of the PolyBase scale-out

## Syntax

```sql
sp_polybase_join_group (
@head_node_address =
N
'head_node_address'
, @dms_control_channel_port = dms_control_channel_port
, @head_node_sql_server_instance_name =
'head_node_sql_server_instance_name'
)
[ ; ]
```
