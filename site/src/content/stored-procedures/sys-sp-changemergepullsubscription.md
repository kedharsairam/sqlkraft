---
name: "sys.sp_changemergepullsubscription"
title: "sp_changemergepullsubscription"
category: "general"
description: "Changes the properties of the merge pull subscription. This stored procedure is executed at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changemergepullsubscription
              [ [ @publication = ]
              N
              'publication'
              ]
              [ , [ @publisher = ]
              N
              'publisher'
              ]
              [ , [ @publisher_db = ]
              N
              'publisher_db'
              ]
              [ , [ @property = ]
              N
              'property'
              ]
              [ , [ @value = ]
              N
              'value'
              ]
              [ ; ]
---

## Description

Changes the properties of the merge pull subscription. This stored procedure is executed at the Subscriber on the subscription database.

## Syntax

```sql
sp_changemergepullsubscription
[ [ @publication = ]
N
'publication'
]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @property = ]
N
'property'
]
[ , [ @value = ]
N
'value'
]
[ ; ]
```
