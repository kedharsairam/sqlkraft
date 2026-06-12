---
name: "sys.sp_helpmergearticleconflicts"
title: "sp_helpmergearticleconflicts"
category: "general"
description: "Returns the articles in the publication that have conflicts. This stored procedure is executed at the Publisher on the publication database, or at the Subscriber on the merge subscription The name of the merge publication. returns all articles in the database that have conflicts."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergearticleconflicts
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
              [ ; ]
---

## Description

Returns the articles in the publication that have conflicts. This stored procedure is executed at the Publisher on the publication database, or at the Subscriber on the merge subscription The name of the merge publication. returns all articles in the database that have conflicts.

## Syntax

```sql
sp_helpmergearticleconflicts
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
[ ; ]
```
