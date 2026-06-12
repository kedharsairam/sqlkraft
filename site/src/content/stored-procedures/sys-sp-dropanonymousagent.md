---
name: "sys.sp_dropanonymousagent"
title: "sp_dropanonymousagent"
category: "general"
description: "Drops an anonymous agent for replication monitoring at the distributor from the Publisher. This stored procedure is executed at the Publisher on any database. The global identifier for an anonymous subscription. default. This identifier can be retrieved at the Subscriber using field of the returned result set is this global identifier. The type of subscription."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sp_helppullsubscription"
---

## Description

Drops an anonymous agent for replication monitoring at the distributor from the Publisher. This stored procedure is executed at the Publisher on any database. The global identifier for an anonymous subscription. default. This identifier can be retrieved at the Subscriber using field of the returned result set is this global identifier. The type of subscription. , with no default. Valid values are , if snapshot replication or transactional replication using the Distribution Agent. , if merge replication using the Merge Agent.

## Syntax

`sp_helppullsubscription`

## Permissions

is used in all types of replication. This stored procedure is used to drop anonymous subscription agents only and can't be used to drop well-known subscriptions. Only members of the fixed database role in the distribution database can execute. Replication stored procedures (Transact-SQL)
## Remarks

Drops an anonymous agent for replication monitoring at the distributor from the Publisher.

This stored procedure is executed at the Publisher on any database.

The global identifier for an anonymous subscription.

default. This identifier can be retrieved at the Subscriber using

value in the

field of the returned result set is this global identifier.

The type of subscription.

, with no default. Valid values are

, if snapshot replication or transactional replication using the Distribution Agent.

, if merge replication using the Merge Agent.

(success) or
