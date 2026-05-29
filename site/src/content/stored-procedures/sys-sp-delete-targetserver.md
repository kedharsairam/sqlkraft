---
name: 'sys.sp_delete_targetserver'
title: 'sp_delete_targetserver'
category: 'general'
description: 'Removes the specified server from the list of available target servers. Transact-SQL syntax conventions The name of the server to remove as an available target server. Specifies whether to clear the download list for the target server. , the procedure clears the download list for the server , the download list isn''t cleared. Specifies whether to post a defect instruction to the target server.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_targetserver
  [ @server_name = ]
  N
  'server_name'
  [ , [ @clear_downloadlist = ] clear_downloadlist ]
  [ , [ @post_defection = ] post_defection ]
  [ ; ]
---

## Description

Removes the specified server from the list of available target servers. Transact-SQL syntax conventions The name of the server to remove as an available target server. Specifies whether to clear the download list for the target server. , the procedure clears the download list for the server , the download list isn't cleared. Specifies whether to post a defect instruction to the target server.

## Syntax

```sql
sp_delete_targetserver
[ @server_name = ]
N
'server_name'
[ , [ @clear_downloadlist = ] clear_downloadlist ]
[ , [ @post_defection = ] post_defection ]
[ ; ]
```
