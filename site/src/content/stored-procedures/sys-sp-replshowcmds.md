---
name: 'sys.sp_replshowcmds'
title: 'sp_replshowcmds'
category: 'general'
description: 'Returns the commands for transactions marked for replication in readable format. can be run only when client connections (including the current connection) aren''t reading replicated transactions from the log. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The number of transactions about which to return information. , which specifies'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replshowcmds [ [ @maxtrans = ] maxtrans ]
  [ ; ]
---

## Description

Returns the commands for transactions marked for replication in readable format. can be run only when client connections (including the current connection) aren't reading replicated transactions from the log. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The number of transactions about which to return information. , which specifies the maximum number of transactions pending replication for which

## Syntax

```sql
sp_replshowcmds [ [ @maxtrans = ] maxtrans ]
[ ; ]
```
