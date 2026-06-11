---
name: "sys.sp_adjustpublisheridentityrange"
title: "sp_adjustpublisheridentityrange"
category: "general"
description: "Adjusts the identity range on a publication and reallocates new ranges based on the threshold value on the publication. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions The name of the publication in which new identity ranges are reallocated."
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

Adjusts the identity range on a publication and reallocates new ranges based on the threshold value on the publication. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions The name of the publication in which new identity ranges are reallocated. The name of the table in which new identity ranges are reallocated. The owner of the table at the Publisher.

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
