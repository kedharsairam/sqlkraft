---
name: "sys.sp_helppeerresponses"
title: "sp_helppeerresponses"
category: "general"
description: "Returns all responses to a specific status request received from a participant in a peer-to-peer replication topology, where the request was initiated by executing any published database in the topology. This stored procedure is executed on the publication database at a Publisher participating in a peer-to-peer replication topology."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helppeerresponses [ @request_id = ] request_id
              [ ; ]
---

## Description

Returns all responses to a specific status request received from a participant in a peer-to-peer replication topology, where the request was initiated by executing any published database in the topology. This stored procedure is executed on the publication database at a Publisher participating in a peer-to-peer replication topology. For more Peer-to-Peer - Transactional Replication ## Syntax

```sql
sp_helppeerresponses [ @request_id = ] request_id
[ ; ]
```
