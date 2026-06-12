---
name: "sys.dm_clr_properties"
title: "sys.dm_clr_properties"
category: "clr"
description: "Returns a row for each property related to SQL Server common language runtime (CLR) integration, including the version and state of the hosted CLR. The hosted CLR is initialized by executing any CLR routine, type, or trigger. The whether execution of user CLR code has been enabled on the server. Execution of user CLR columns. Each row in this view provides details about a property of the hosted CL"
tags: ["clr", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT name, value
  FROM sys.dm_clr_properties;
---

## Description

Returns a row for each property related to SQL Server common language runtime (CLR) integration, including the version and state of the hosted CLR. The hosted CLR is initialized by executing any CLR routine, type, or trigger. The whether execution of user CLR code has been enabled on the server. Execution of user CLR columns. Each row in this view provides details about a property of the hosted CLR.

## Syntax

```sql
SELECT name, value
FROM sys.dm_clr_properties;
```
