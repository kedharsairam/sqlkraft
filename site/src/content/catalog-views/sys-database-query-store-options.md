---
name: "sys.database_query_store_options"
title: "sys.database_query_store_options"
category: "query-store"
description: "SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns the Query Store options for this database. Indicates the desired operation mode of Query Store, explicitly set by user. Textual description of the desired operation mode of Query Store: Indicates the operation mode of Query Store. In addition to list of desired states required by the user, actual state Textual descr"
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  READ_CAPTURE_SECONDARY
  desired_state_desc
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns the Query Store options for this database. Indicates the desired operation mode of Query Store, explicitly set by user. Textual description of the desired operation mode of Query Store: Indicates the operation mode of Query Store. In addition to list of desired states required by the user, actual state Textual description of the actual

## Syntax

```sql
READ_CAPTURE_SECONDARY
desired_state_desc
```
