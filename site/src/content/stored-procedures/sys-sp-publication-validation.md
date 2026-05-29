---
name: "sys.sp_publication_validation"
title: "sp_publication_validation"
category: "general"
description: "Initiates an article validation request for each article in the specified publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions Specifies whether to return only the rowcount for the table. can be one of the following values. Perform a SQL Server 7.0 compatible checksum. When an article is horizontally filtered, a rowcount opera"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_publication_validation
  [ @publication = ]
  N
  'publication'
  [ , [ @rowcount_only = ] rowcount_only ]
  [ , [ @full_or_fast = ] full_or_fast ]
  [ , [ @shutdown_agent = ] shutdown_agent ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Initiates an article validation request for each article in the specified publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions Specifies whether to return only the rowcount for the table. can be one of the following values. Perform a SQL Server 7.0 compatible checksum. When an article is horizontally filtered, a rowcount operation is performed instead of a

## Syntax

```sql
sp_publication_validation
[ @publication = ]
N
'publication'
[ , [ @rowcount_only = ] rowcount_only ]
[ , [ @full_or_fast = ] full_or_fast ]
[ , [ @shutdown_agent = ] shutdown_agent ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

is used in transactional replication. can be called at any time after the articles associated with the publication are activated. The procedure can be run manually (one time) or as part of a regularly scheduled job that validates the data. If your application has immediate-updating Subscribers, might detect spurious errors. first calculates the rowcount or checksum at the Publisher and then at the Subscriber. Because the immediate-updating trigger could propagate an update from the Subscriber to the Publisher after the rowcount or checksum is completed at the Publisher, but before the rowcount or checksum is completed at the Subscriber, the values could change. To ensure that the values at the Subscriber and Publisher don't change while validating a publication, stop the Microsoft Distributed Transaction Coordinator (MS DTC) service at the Publisher during validation. Only members of the fixed server role or the fixed database role can execute . Validate Replicated Data sp_article_validation (Transact-SQL) sp_table_validation (Transact-SQL) System stored procedures (Transact-SQL) Related content
