---
name: "sys.sp_validatemergepublication"
title: "sp_validatemergepublication"
category: "general"
description: "Performs a publication-wide validation for which all subscriptions (push, pull, and anonymous) are validated once. This stored procedure is executed at the Publisher on the publication The type of validation to perform. , and can be one of the following values. Rowcount and checksum validation."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_validatemergepublication
      [ @publication = ]
      N
      'publication'
      , [ @level = ] level
      [ ; ]
---

## Description

Performs a publication-wide validation for which all subscriptions (push, pull, and anonymous) are validated once. This stored procedure is executed at the Publisher on the publication The type of validation to perform. , and can be one of the following values. Rowcount and checksum validation.

## Syntax

```sql
sp_validatemergepublication
[ @publication = ]
N
'publication'
, [ @level = ] level
[ ; ]
```
