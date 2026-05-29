---
name: 'sys.sp_replmonitorhelpmergesessiondetail'
title: 'sp_replmonitorhelpmergesessiondetail'
category: 'general'
description: 'Returns detailed, article-level information about a specific replication Merge Agent session, which is used to monitor merge replication. The result set includes a detail row for each article that was synchronized during the session. It also includes a row that represents the session initialization and rows that summarize both the upload and download phases of the session. This stored procedure is'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replmonitorhelpmergesessiondetail [ @session_id = ] session_id
  [ ; ]
---

## Description

Returns detailed, article-level information about a specific replication Merge Agent session, which is used to monitor merge replication. The result set includes a detail row for each article that was synchronized during the session. It also includes a row that represents the session initialization and rows that summarize both the upload and download phases of the session. This stored procedure is executed at the Distributor on the distribution database, or at the

## Syntax

```sql
sp_replmonitorhelpmergesessiondetail [ @session_id = ] session_id
[ ; ]
```

## Permissions

is used to monitor merge replication. When executed on the Subscriber, only returns detailed information about the last 5 Merge Agent sessions. Only members of the or fixed database role on the distribution database at the Distributor or on the subscription database at the Subscriber can execute . Programmatically monitor replication Related content
