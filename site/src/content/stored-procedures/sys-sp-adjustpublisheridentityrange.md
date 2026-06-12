---
name: "sys.sp_adjustpublisheridentityrange"
title: "sp_adjustpublisheridentityrange"
category: "general"
description: "Adjusts the identity range on a publication and reallocates new ranges based on the threshold value on the publication. This stored procedure is executed at the Publisher on the publication The name of the publication in which new identity ranges are reallocated."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_adjustpublisheridentityrange
              [ [ @publication = ]
              N
              'publication'
              ]
              [ , [ @table_name = ]
              N
              'table_name'
              ]
              [ , [ @table_owner = ]
              N
              'table_owner'
              ]
              [ ; ]
---

## Description

Adjusts the identity range on a publication and reallocates new ranges based on the threshold value on the publication. This stored procedure is executed at the Publisher on the publication The name of the publication in which new identity ranges are reallocated.

## Syntax

```sql
sp_adjustpublisheridentityrange
[ [ @publication = ]
N
'publication'
]
[ , [ @table_name = ]
N
'table_name'
]
[ , [ @table_owner = ]
N
'table_owner'
]
[ ; ]
```
