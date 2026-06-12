---
name: "sys.sp_cdc_get_captured_columns"
title: "sys.sp_cdc_get_captured_columns"
category: "general"
description: "Returns change data capture metadata information for the captured source columns tracked by the specified capture instance. Change data capture isn't available in every edition of SQL Server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_get_captured_columns
  [ @capture_instance = ]
  'capture_instance'
  [ ; ]
---

## Description

Returns change data capture metadata information for the captured source columns tracked by the specified capture instance. Change data capture isn't available in every edition of SQL Server. For a list of features that are supported by the editions of SQL Server, see supported features of SQL Server 2022 The name of the capture instance associated with a source table.

## Syntax

```sql
sys.sp_cdc_get_captured_columns
[ @capture_instance = ]
'capture_instance'
[ ; ]
```
