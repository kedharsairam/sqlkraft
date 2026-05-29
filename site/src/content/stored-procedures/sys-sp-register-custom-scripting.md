---
name: "sys.sp_register_custom_scripting"
title: "sp_register_custom_scripting"
category: "general"
description: "Replication allows user-defined custom stored procedures to replace one or more of the default procedures used in transactional replication. When a schema change is made to a replicated table, these stored procedures are re-created. registers a stored procedure or Transact-SQL script file that is executed when a schema change occurs to script out the definition for a new user-defined custom stored"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_register_custom_scripting"
---

## Description

Replication allows user-defined custom stored procedures to replace one or more of the default procedures used in transactional replication. When a schema change is made to a replicated table, these stored procedures are re-created. registers a stored procedure or Transact-SQL script file that is executed when a schema change occurs to script out the definition for a new user-defined custom stored procedure. This new user-defined custom stored procedure should reflect the

## Syntax

```sql
sp_register_custom_scripting
```

## Permissions

Regenerate custom procedures to reflect schema changes . Only members of the fixed server role, the fixed database role, or the fixed database role can execute . sp_unregister_custom_scripting (Transact-SQL) Related content
