---
name: 'sys.sp_requestpeertopologyinfo'
title: 'sp_requestpeertopologyinfo'
category: 'general'
description: 'MSpeer_topologyresponse system table with information about a peer-to-peer transactional replication topology. Execute sp_gettopologyinfo to obtain information from the table in XML format. Transact-SQL syntax conventions The name of the publication for which to perform a topology-wide status request. , with no default. The ID number that is assigned to the topology status request. parameter of ty'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_requestpeertopologyinfo
  [ @publication = ]
  N
  'publication'
  [ , [ @request_id = ] request_id
  OUTPUT
  ]
  [ ; ]
---

## Description

MSpeer_topologyresponse system table with information about a peer-to-peer transactional replication topology. Execute sp_gettopologyinfo to obtain information from the table in XML format. Transact-SQL syntax conventions The name of the publication for which to perform a topology-wide status request. , with no default. The ID number that is assigned to the topology status request. parameter of type . This ID can be used by sp_gettopologyinfo

## Syntax

```sql
sp_requestpeertopologyinfo
[ @publication = ]
N
'publication'
[ , [ @request_id = ] request_id
OUTPUT
]
[ ; ]
```

## Permissions

is used in peer-to-peer transactional replication. Execute before executing sp_gettopologyinfo . These procedures are used by the Configure Peer-to-Peer Topology Wizard, but they can also be used directly if you require topology information in an XML format. If you prefer tabular results, query the MSpeer_topologyresponse system table. Requires membership in the fixed server role, fixed database role, or execute permission directly on this stored procedure. Peer-to-Peer - Transactional Replication Replication stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Populates the

MSpeer_topologyresponse

system table with information about a peer-to-peer

transactional replication topology. Execute

sp_gettopologyinfo

to obtain information from the

table in XML format.

Transact-SQL syntax conventions

The name of the publication for which to perform a topology-wide status request.

@publication

, with no default.

The ID number that is assigned to the topology status request.

@request_id

is an OUTPUT

parameter of type

. This ID can be used by

sp_gettopologyinfo

(success) or
