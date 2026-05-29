---
title: "Frequently asked questions"
topic: "migration"
description: |
  ﾃ
  
  Summarize this article for me
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  The following questions and answers provide guidance on a variety of tasks faced by
  
  administrators of replicated
tags:
  - "migration"
  - "frequently-asked-questions"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

Applies to:

SQL Server

Azure SQL Managed Instance

The following questions and answers provide guidance on a variety of tasks faced by

administrators of replicated databases.

No. Activity can continue on a database while a publication is being created. Be aware that

producing a snapshot can be resource-intensive, so it is best to generate snapshots during

periods of lower activity on the database (by default a snapshot is generated when you

complete the New Publication Wizard).

The length of time that the locks are taken depends on the type of replication used:

For merge publications, the Snapshot Agent does not take any locks.

For transactional publications, by default the Snapshot Agent takes locks only during the

initial phase of snapshot generation.

For snapshot publications the Snapshot Agent takes locks during the entire snapshot

generation process.

Because locks prevent other users from updating the tables, the Snapshot Agent should be

scheduled to execute during periods of lower activity on the database, especially for snapshot

publications.

A subscription is available after the snapshot has been applied to the subscription database.

Even though the subscription database is accessible prior to this, the database should not be