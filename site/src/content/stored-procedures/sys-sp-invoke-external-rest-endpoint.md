---
name: "sys.sp_invoke_external_rest_endpoint"
title: "sp_invoke_external_rest_endpoint"
category: "general"
description: "SQL database in Microsoft Fabric stored procedure invokes an HTTPS REST endpoint provided as an input argument to the procedure. To mitigate the risk of unauthorized access or transfer of data, consider the following security : Ensure that only authorized users have access to sensitive data and REST API endpoints. Use the database roles and privileges. : Ensure that all REST calls are authenticate"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_invoke_external_rest_endpoint"
---

## Description

SQL database in Microsoft Fabric stored procedure invokes an HTTPS REST endpoint provided as an input argument to the procedure. To mitigate the risk of unauthorized access or transfer of data, consider the following security : Ensure that only authorized users have access to sensitive data and REST API endpoints. Use the database roles and privileges. : Ensure that all REST calls are authenticated and

## Syntax

```sql
sp_invoke_external_rest_endpoint
```
