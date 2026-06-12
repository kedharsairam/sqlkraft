---
name: "sys.fn_get_audit_file"
title: "sys.fn_get_audit_file"
category: "system"
description: "Returns information from an audit file created by a server audit in SQL Server. For more SQL Server Audit (Database Engine) Specifies the directory or path and file name for the audit file set to be read. Type is Passing a path without a file name pattern generates an error."
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: '<path>\LoginsAudit_{GUID}*'
---

## Description

Returns information from an audit file created by a server audit in SQL Server. For more SQL Server Audit (Database Engine) Specifies the directory or path and file name for the audit file set to be read. Type is Passing a path without a file name pattern generates an error.

## Syntax

```sql
<path>\LoginsAudit_{GUID}*
```
