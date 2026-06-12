---
name: "sys.sp_vupgrade_mergeobjects"
title: "sp_vupgrade_mergeobjects"
category: "general"
description: "Regenerates the article-specific triggers, stored procedures, and views that are used to track and apply data changes for merge replication. Execute this procedure in the following If an object required by replication is accidentally dropped. If you apply an update, such as a hotfix, which requires modification to one or more replication objects. Execute the procedure on each node after applying t"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_vupgrade_mergeobjects
      [ [ @login = ]
      N
      'login'
      ]
      [ , [ @password = ]
      N
      'password'
      ]
      [ , [ @security_mode = ] security_mode ]
      [ ; ]
---

## Description

Regenerates the article-specific triggers, stored procedures, and views that are used to track and apply data changes for merge replication. Execute this procedure in the following If an object required by replication is accidentally dropped. If you apply an update, such as a hotfix, which requires modification to one or more replication objects. Execute the procedure on each node after applying the update.

## Syntax

```sql
sp_vupgrade_mergeobjects
[ [ @login = ]
N
'login'
]
[ , [ @password = ]
N
'password'
]
[ , [ @security_mode = ] security_mode ]
[ ; ]
```
