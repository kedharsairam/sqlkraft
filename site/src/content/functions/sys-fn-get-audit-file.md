---
name: "sys.fn_get_audit_file"
title: "sys.fn_get_audit_file"
category: "system"
description: "SQL database in Microsoft Fabric Returns information from an audit file created by a server audit in SQL Server. For more SQL Server Audit (Database Engine) Transact-SQL syntax conventions Specifies the directory or path and file name for the audit file set to be read. Type is Passing a path without a file name pattern generates an error."
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: '<path>\LoginsAudit_{GUID}*'
---

## Description

SQL database in Microsoft Fabric Returns information from an audit file created by a server audit in SQL Server. For more SQL Server Audit (Database Engine) Transact-SQL syntax conventions Specifies the directory or path and file name for the audit file set to be read. Type is Passing a path without a file name pattern generates an error. This argument must include both a path (drive letter or network share) and a file name

## Syntax

```sql
<path>\LoginsAudit_{GUID}*
```
