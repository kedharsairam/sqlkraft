---
name: "sys.sp_addpullsubscription"
title: "sp_addpullsubscription"
category: "general"
description: "Adds a pull subscription to a snapshot or transactional publication. This stored procedure is executed at the Subscriber on the database where the pull subscription is to be created. Server name can be specified as for a named instance."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addpullsubscription
  [ @publisher = ]
  N
  'publisher'
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  , [ @publication = ]
  N
  'publication'
  [ , [ @independent_agent = ]
  N
  'independent_agent'
  ]
  [ , [ @subscription_type = ]
  N
  'subscription_type'
  ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @update_mode = ]
  N
  'update_mode'
  ]
  [ , [ @immediate_sync = ] immediate_sync ]
  [ ; ]
---

## Description

Adds a pull subscription to a snapshot or transactional publication. This stored procedure is executed at the Subscriber on the database where the pull subscription is to be created. Server name can be specified as for a named instance. Specify the port number for your connection when SQL Server is deployed on Linux or Windows with a custom port, and the browser service is disabled. The use of custom port numbers for remote

## Syntax

```sql
sp_addpullsubscription
[ @publisher = ]
N
'publisher'
[ , [ @publisher_db = ]
N
'publisher_db'
]
, [ @publication = ]
N
'publication'
[ , [ @independent_agent = ]
N
'independent_agent'
]
[ , [ @subscription_type = ]
N
'subscription_type'
]
[ , [ @description = ]
N
'description'
]
[ , [ @update_mode = ]
N
'update_mode'
]
[ , [ @immediate_sync = ] immediate_sync ]
[ ; ]
```

## Permissions

If the MSreplication_subscriptions table doesn't exist at the Subscriber, creates it. It also adds a row to the MSreplication_subscriptions table. For pull subscriptions, sp_addsubscription should be called at the Publisher first. SQL Only members of the fixed server role or fixed database role can execute. should execute to change the connection to use SQL Server Authentication after the subscription is configured. Description sp_addpullsubscription Creates a pull subscription at the Subscriber for a Snapshot or Transactional publication. sp_addpullsubscription_agent Creates the Distribution Agent job for a pull subscription at the Subscriber. sp_addpushsubscription_agent Creates the Distribution Agent job for a push subscription at the Distributor. sp_addqueued_artinfo Adds article information to the queue used by queued updating subscriptions. sp_addscriptexec Posts a SQL script to be executed at all Subscribers to a publication. sp_addsynctriggers Creates synchronization triggers at the Subscriber for updatable subscriptions. sp_attachsubscription Attaches an existing subscription database to any Subscriber. sp_change_subscription_properties Changes security information and settings for a pull subscription. sp_changesubscriber Changes options for a Subscriber, including connection settings and schedules. sp_changesubscriber_schedule Changes the Distribution Agent or Merge Agent schedule for a Subscriber. sp_changesubscription Modifies properties of a Snapshot or Transactional subscription. sp_changesubscriptiondtsinfo Changes the DTS package properties of a transactional push subscription. sp_changesubstatus Changes the status of an existing subscription at the Publisher. sp_copysubscription Copies a subscription database that has pull subscriptions but no push subscriptions. sp_droppullsubscription Drops a pull subscription at the Subscriber database. sp_dropsubscriber Removes the Subscriber designation from a registered server. sp_dropsubscription Removes a subscription to a Snapshot or Transactional publication. sp_expired_subscription_cleanup Removes expired anonymous subscriptions from publications. sp_getqueuedrows Returns rows from the Subscriber that have pending updates in the queue. sp_getsubscriptiondtspackagename Returns the DTS package name for a subscription. sp_helpsubscriberinfo Returns information about a Subscriber.
