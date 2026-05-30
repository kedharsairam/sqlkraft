---
name: "sys.sp_removedistpublisherdbreplication"
title: "sp_removedistpublisherdbreplication"
category: "general"
description: "Azure SQL Managed Instance Removes publishing metadata belonging to a specific publication at the Distributor. This stored procedure is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the Publisher server. , with no default. The name of the publication database. , with no default. is used by transactional and snapshot replication."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_removedistpublisherdbreplication"
---

## Description

Azure SQL Managed Instance Removes publishing metadata belonging to a specific publication at the Distributor. This stored procedure is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the Publisher server. , with no default. The name of the publication database. , with no default. is used by transactional and snapshot replication.

## Syntax

```sql
sp_removedistpublisherdbreplication
```

## Permissions

is used when a published database must be recreated without also dropping the distribution database. The following metadata is removed: All publication metadata. Metadata for all articles belong to the publication. Metadata for all subscriptions to the publication. Metadata for all replication agent jobs that belong to the publication. Only members of the fixed server role at the Distributor or members of the fixed database role in the distribution database can execute . System stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Azure SQL Managed Instance

Removes publishing metadata belonging to a specific publication at the Distributor. This stored

procedure is executed at the Distributor on the distribution database.

Transact-SQL syntax conventions

The name of the Publisher server.

, with no default.

The name of the publication database.

@publisher_db

, with no default.

(success) or

is used by transactional and snapshot replication.
