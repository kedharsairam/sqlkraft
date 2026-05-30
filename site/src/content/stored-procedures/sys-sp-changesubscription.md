---
name: "sys.sp_changesubscription"
title: "sp_changesubscription"
category: "general"
description: "Changes the properties of a snapshot or transactional push subscription or a pull subscription involved in queued updating transactional replication. To change properties of all other types sp_change_subscription_properties executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to change. When configuring a Publisher with a remote Distrib"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_changesubscription"
---

## Description

Changes the properties of a snapshot or transactional push subscription or a pull subscription involved in queued updating transactional replication. To change properties of all other types sp_change_subscription_properties executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to change. When configuring a Publisher with a remote Distributor, the values supplied for all

## Syntax

```sql
sp_changesubscription
```

## Permissions

Only members of the fixed server role or fixed database role can execute . sp_addsubscription (Transact-SQL) sp_dropsubscription (Transact-SQL) Related content If the MSreplication_subscriptions table doesn't exist at the Subscriber, creates it. It also adds a row to the MSreplication_subscriptions table. For pull subscriptions, sp_addsubscription should be called at the Publisher first. SQL Only members of the fixed server role or fixed database role can execute . should execute to change the connection to use SQL Server Authentication after the subscription is configured.
