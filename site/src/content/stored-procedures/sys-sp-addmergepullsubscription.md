---
name: "sys.sp_addmergepullsubscription"
title: "sp_addmergepullsubscription"
category: "general"
description: "Adds a pull subscription to a merge publication. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions , with a default of the local server name. The Publisher must be a valid server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergepullsubscription
  [ @publication = ]
  N
  'publication'
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  [ , [ @subscriber_type = ]
  N
  'subscriber_type'
  ]
  [ , [ @subscription_priority = ] subscription_priority ]
  [ , [ @sync_type = ]
  N
  'sync_type'
  ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ ; ]
---

## Description

Adds a pull subscription to a merge publication. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions , with a default of the local server name. The Publisher must be a valid server. The name of the Publisher database.

## Syntax

```sql
sp_addmergepullsubscription
[ @publication = ]
N
'publication'
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @subscriber_type = ]
N
'subscriber_type'
]
[ , [ @subscription_priority = ] subscription_priority ]
[ , [ @sync_type = ]
N
'sync_type'
]
[ , [ @description = ]
N
'description'
]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Create a Pull Subscription Subscribe to Publications sp_addmergepullsubscription_agent (Transact-SQL) sp_changemergepullsubscription (Transact-SQL) Related content Description sp_addmergepullsubscription Creates a pull subscription at the Subscriber for a Merge publication. sp_addmergepullsubscription_agent Creates the Merge Agent job for a pull subscription at the Subscriber. sp_addmergepushsubscription_agent Creates the Merge Agent job for a push subscription at the Distributor. sp_addmergesubscription Creates a push or pull subscription to a Merge publication. sp_browsemergesnapshotfolder Returns the path to the most recent snapshot generated for a Merge publication. sp_changemergearticle Modifies properties of an existing article in a Merge publication. sp_changemergefilter Modifies an existing join filter or logical record relationship. sp_changemergepublication Modifies properties of a Merge publication. sp_changemergepullsubscription Changes the properties of a merge pull subscription. sp_changemergesubscription Changes properties of a merge push subscription. sp_copymergesnapshot Copies the snapshot folder to an alternate folder. sp_deletemergeconflictrow Deletes rows from a merge conflict table. sp_dropmergealternatepublisher Removes an alternate Publisher from a Merge publication. sp_dropmergearticle Removes an article from a Merge publication. sp_dropmergefilter Drops a join filter from a Merge publication. sp_dropmergepartition Removes a partition definition from a Merge publication with parameterized filters. sp_dropmergepublication Removes a Merge publication and its associated Snapshot Agent. sp_dropmergepullsubscription Drops a Merge pull subscription at the Subscriber database. sp_dropmergesubscription Drops a subscription to a Merge publication and removes the associated Merge Agent. sp_getmergedeletetype Returns the type of merge delete operation. sp_helpmergealternatepublisher Returns a list of servers configured as alternate Publishers. sp_helpmergearticle Returns properties of articles in a Merge publication. sp_helpmergearticlecolumn Returns the list of columns in a Merge publication article.
