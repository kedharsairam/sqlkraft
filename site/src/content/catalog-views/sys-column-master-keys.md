---
name: 'sys.column_master_keys'
title: 'sys.column_master_keys'
category: 'compatibility'
description: 'SQL Server 2016 (13.x) and later Returns a row for each database master key added by using the statement. Each row represents a single column master key (CMK). Date the column master key was created. Date the column master key was last modified. Name of the provider for the column master key store that contains the CMK. Allowed values are: MSSQL_CERTIFICATE_STORE - If the column master key A user-'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: '''CurrentUser/Personal/''<thumbprint>'
---

## Description

SQL Server 2016 (13.x) and later Returns a row for each database master key added by using the statement. Each row represents a single column master key (CMK). Date the column master key was created. Date the column master key was last modified. Name of the provider for the column master key store that contains the CMK. Allowed values are: MSSQL_CERTIFICATE_STORE - If the column master key A user-defined value, if the column master key store is

## Syntax

```sql
'CurrentUser/Personal/'<thumbprint>
```
