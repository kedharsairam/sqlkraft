---
name: "sys.sp_helpdynamicsnapshot_job"
title: "sp_helpdynamicsnapshot_job"
category: "general"
description: "Returns information on agent jobs that generate filtered data snapshots. This stored procedure is executed at the Publisher on the publication database. information on all filtered data snapshot jobs that match the specified The name of a filtered data snapshot job. , which returns all dynamic jobs for a publication with the specified . If a job name wasn't explicit"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  'dyn_' + <name of the standard snapshot job> +
  <GUID>
---

## Description

Returns information on agent jobs that generate filtered data snapshots. This stored procedure is executed at the Publisher on the publication database. information on all filtered data snapshot jobs that match the specified The name of a filtered data snapshot job. , which returns all dynamic jobs for a publication with the specified.

## Syntax

```sql
'dyn_' + <name of the standard snapshot job> +
<GUID>
```

## Permissions

is used in merge replication. If all of the default parameter values are used, information on all partitioned data snapshot jobs for the entire publication database is returned. Only members of the fixed server role, the fixed database role, and the publication access list for the publication can execute. System stored procedures (Transact-SQL)
