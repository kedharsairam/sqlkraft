---
name: "sys.sp_helpsubscription_properties"
title: "sp_helpsubscription_properties"
category: "general"
description: "Retrieves security information from the is executed at the Subscriber. information on all Publishers."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpsubscription_properties
  [ [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  [ , [ @publication = ]
  N
  'publication'
  ]
  [ , [ @publication_type = ] publication_type ]
  [ ; ]
---

## Description

Retrieves security information from the is executed at the Subscriber. information on all Publishers.

## Syntax

```sql
sp_helpsubscription_properties
[ [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @publication = ]
N
'publication'
]
[ , [ @publication_type = ] publication_type ]
[ ; ]
```
