---
name: 'sys.sp_msx_defect'
title: 'sp_msx_defect'
category: 'general'
description: 'Removes the current server from multiserver operations. Transact-SQL syntax conventions Specifies whether to force the defection to occur if the Master SQLServerAgent has been permanently lost due to an irreversibly corrupt , which indicates that no forced defection should After you force a defection by executing server role at the Master SQLServerAgent must run the following command to complete t'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_msx_defect [ [ @forced_defection = ] forced_defection ]
  [ ; ]
---

## Description

Removes the current server from multiserver operations. Transact-SQL syntax conventions Specifies whether to force the defection to occur if the Master SQLServerAgent has been permanently lost due to an irreversibly corrupt , which indicates that no forced defection should After you force a defection by executing server role at the Master SQLServerAgent must run the following command to complete the

## Syntax

```sql
sp_msx_defect [ [ @forced_defection = ] forced_defection ]
[ ; ]
```
