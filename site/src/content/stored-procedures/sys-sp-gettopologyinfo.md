---
name: "sys.sp_gettopologyinfo"
title: "sp_gettopologyinfo"
category: "general"
description: "Returns information about a peer-to-peer transactional replication topology. Execute sp_requestpeertopologyinfo to collect information before you execute this procedure. The ID of a topology status request. , with a default of . To obtain an ID, OUTPUT parameter from sp_requestpeertopologyinfo MSpeer_topologyrequest returns a result set that's a single XML column. T"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_gettopologyinfo [ [ @request_id = ] request_id ]
              [ ; ]
---

## Description

Returns information about a peer-to-peer transactional replication topology. Execute sp_requestpeertopologyinfo to collect information before you execute this procedure. The ID of a topology status request. , with a default of. To obtain an ID, OUTPUT parameter from sp_requestpeertopologyinfo MSpeer_topologyrequest returns a result set that's a single XML column. The data in the XML column is the same as the data in the MSpeer_topologyresponse is used in peer-to-peer transactional replication. Execute sp_requestpeertopologyinfo before you execute.

## Syntax

```sql
sp_gettopologyinfo [ [ @request_id = ] request_id ]
[ ; ]
```

## Permissions

is used in peer-to-peer transactional replication. Execute before executing sp_gettopologyinfo. These procedures are used by the Configure Peer-to-Peer Topology Wizard, but they can also be used directly if you require topology information in an XML format. If you prefer tabular results, query the MSpeer_topologyresponse system table. Requires membership in the fixed server role, fixed database role, or execute permission directly on this stored procedure. Peer-to-Peer - Transactional Replication Replication stored procedures (Transact-SQL)
## Remarks

Returns information about a peer-to-peer transactional replication topology. Execute

sp_requestpeertopologyinfo

to collect information before you execute this procedure.

The ID of a topology status request.

@request_id

, with a default of. To obtain an ID,

@request_id

OUTPUT parameter from

sp_requestpeertopologyinfo

, or query the

MSpeer_topologyrequest

system table.

returns a result set that's a single XML column. The data in the XML

column is the same as the data in the

MSpeer_topologyresponse

system table.

(success) or

is used in peer-to-peer transactional replication. Execute

sp_requestpeertopologyinfo

before you execute. These procedures are
