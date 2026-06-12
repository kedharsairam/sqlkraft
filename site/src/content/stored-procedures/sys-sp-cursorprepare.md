---
name: "sys.sp_cursorprepare"
title: "sp_cursorprepare"
category: "general"
description: "Compiles the cursor statement or batch into an execution plan, but doesn't create the cursor. The compiled statement can later be used by . This procedure, coupled with , but is split into two phases. in a tabular data stream (TDS) packet. A SQL Server-generated prepared procedure in order to open a cursor."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_cursorprepare prepared_handle
      OUTPUT
      , params , stmt , options
      [ , scrollopt [ , ccopt ] ]
      [ ; ]
---

## Description

Compiles the cursor statement or batch into an execution plan, but doesn't create the cursor. The compiled statement can later be used by. This procedure, coupled with , but is split into two phases. in a tabular data stream (TDS) packet. A SQL Server-generated prepared procedure in order to open a cursor. Once a handle is created, it exists until you sign out, or until you explicitly remove it through a

## Syntax

```sql
sp_cursorprepare prepared_handle
OUTPUT
, params , stmt , options
[ , scrollopt [ , ccopt ] ]
[ ; ]
```
