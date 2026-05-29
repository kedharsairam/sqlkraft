---
name: 'sys.sp_helpsubscription_properties'
title: 'sp_helpsubscription_properties'
category: 'general'
description: 'Retrieves security information from the is executed at the Subscriber. Transact-SQL syntax conventions information on all Publishers. The name of the Publisher database. returns information on all Publisher databases. information on all publications.'
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

Retrieves security information from the is executed at the Subscriber. Transact-SQL syntax conventions information on all Publishers. The name of the Publisher database. returns information on all Publisher databases. information on all publications.

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
