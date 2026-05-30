---
name: "sys.sp_oastop"
title: "sp_OAStop"
category: "general"
description: "Stops the server-wide OLE Automation stored procedure execution environment. Transact-SQL syntax conventions (success) or a nonzero number (failure) that is the integer value of the HRESULT returned by For more information about HRESULT return codes, see OLE automation return codes and error A single execution environment is shared by all clients that use OLE Automation stored procedures. If one c"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  EXECUTE
  sp_OAStop;
  GO
---

## Description

Stops the server-wide OLE Automation stored procedure execution environment. Transact-SQL syntax conventions (success) or a nonzero number (failure) that is the integer value of the HRESULT returned by For more information about HRESULT return codes, see OLE automation return codes and error A single execution environment is shared by all clients that use OLE Automation stored procedures. If one client calls

## Syntax

```sql
EXECUTE sp_OAStop;
GO
```

## Permissions

06/23/2025 Applies to: SQL Server Stops the server-wide OLE Automation stored procedure execution environment. Transact-SQL syntax conventions syntaxsql None. (success) or a nonzero number (failure) that is the integer value of the HRESULT returned by the OLE Automation object. For more information about HRESULT return codes, see OLE automation return codes and error information . A single execution environment is shared by all clients that use OLE Automation stored procedures. If one client calls , the shared execution environment is stopped for all clients. After the execution environment is stopped, any call to restarts the execution environment. Requires membership in the fixed server role or execute permission directly on this stored procedure. The Ole Automation Procedures server configuration option must be

## Examples

### Example 1

```sql
EXECUTE sp_OAStop;
GO
```
