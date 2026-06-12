---
name: "sys.sp_helpsubscriberinfo"
title: "sp_helpsubscriberinfo"
category: "general"
description: "Displays information about a Subscriber. This stored procedure is executed at the Publisher on , and defaults to the name of the current shouldn't be specified, except when it's an Oracle Publisher."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpsubscriberinfo
              [ [ @subscriber = ]
              N
              'subscriber'
              ]
              [ , [ @publisher = ]
              N
              'publisher'
              ]
              [ ; ]
---

## Description

Displays information about a Subscriber. This stored procedure is executed at the Publisher on , and defaults to the name of the current shouldn't be specified, except when it's an Oracle Publisher.

## Syntax

```sql
sp_helpsubscriberinfo
[ [ @subscriber = ]
N
'subscriber'
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
