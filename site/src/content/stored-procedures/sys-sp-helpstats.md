---
name: "sys.sp_helpstats"
title: "sp_helpstats"
category: "general"
description: "Returns statistics information about columns and indexes on the specified table. Specifies the table on which to provide statistics information. no default. A one-part or two-part name can be specified. Specifies the extent of information to provide."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpstats
              [ @objname = ]
              N
              'objname'
              [ , [ @results = ]
              N
              'results'
              ]
              [ ; ]
---

## Description

Returns statistics information about columns and indexes on the specified table. Specifies the table on which to provide statistics information. no default. A one-part or two-part name can be specified. Specifies the extent of information to provide. lists statistics for all indexes and also columns that have statistics created on them.

## Syntax

```sql
sp_helpstats
[ @objname = ]
N
'objname'
[ , [ @results = ]
N
'results'
]
[ ; ]
```
