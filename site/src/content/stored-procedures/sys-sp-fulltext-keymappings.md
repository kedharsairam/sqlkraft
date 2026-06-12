---
name: "sys.sp_fulltext_keymappings"
title: "sp_fulltext_keymappings"
category: "general"
description: "Returns mappings between document identifiers (DocIds) and full-text key values. The DocId integer that maps to a particular full-text key value in a full- text indexed table. DocId values that satisfy a search condition are passed from the Full-Text Engine to the Database Engine, where they are mapped to full-text key values from the base table being queried. The full-text key column is a unique"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_fulltext_keymappings { table_id | table_id , doc
              I
              d | table_id ,
              NULL
              , key }
              [ ; ]
---

## Description

Returns mappings between document identifiers (DocIds) and full-text key values. The DocId integer that maps to a particular full-text key value in a full- text indexed table. DocId values that satisfy a search condition are passed from the Full-Text Engine to the Database Engine, where they are mapped to full-text key values from the base table being queried. The full-text key column is a unique index that is required on one column

## Syntax

```sql
sp_fulltext_keymappings { table_id | table_id , doc
I d | table_id ,
NULL
, key }
[ ; ]
```
