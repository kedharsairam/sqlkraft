---
name: "sys.sp_helpqreader_agent"
title: "sp_helpqreader_agent"
category: "general"
description: "Returns properties of the Queue Reader agent. This stored procedure is executed at the Distributor on the distribution database or at the Publisher on any database. Specifies whether the stored procedure is called at the Publisher or at the Distributor. means that the stored procedure is called from the Publisher. means that the stored procedure is called from the D"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helpqreader_agent [ [ @frompublisher = ] frompublisher ]
      [ ; ]
---

## Description

Returns properties of the Queue Reader agent. This stored procedure is executed at the Distributor on the distribution database or at the Publisher on any database. Specifies whether the stored procedure is called at the Publisher or at the Distributor. means that the stored procedure is called from the Publisher. means that the stored procedure is called from the Distributor.

## Syntax

```sql
sp_helpqreader_agent [ [ @frompublisher = ] frompublisher ]
[ ; ]
```
