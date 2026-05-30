---
name: "sys.query_store_query_hints"
title: "sys.query_store_query_hints"
category: "query-store"
description: "SQL Server 2022 (16.x) and later versions SQL database in Microsoft Fabric Unique identifier of a query hint. Unique identifier of a query in the Query Store. Determines the scope at which the hint is Error code returned when if applying hints Includes the error description of the error Number of times that the query hint application failed since the query hint was created or last Source of Query "
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  N'OPTION (...)
  last_query_hint_failure_reason
---

## Description

SQL Server 2022 (16.x) and later versions SQL database in Microsoft Fabric Unique identifier of a query hint. Unique identifier of a query in the Query Store. Determines the scope at which the hint is Error code returned when if applying hints Includes the error description of the error Number of times that the query hint application failed since the query hint was created or last Source of Query Store hint: user source is zero

## Syntax

```sql
N'OPTION (...) last_query_hint_failure_reason
```

## Permissions

Applies to: SQL Server 2022 (16.x) and later versions Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns query hints from Query Store hints . Description Unique identifier of a query hint. Unique identifier of a query in the Query Store. Foreign key to the column in sys.query_store_query . Determines the scope at which the hint is applied, as per the column in sys.query_store_replicas . Hint definition in form of Error code returned when if applying hints failed. Includes the of the error message. Includes the error description of the error message. Number of times that the query hint application failed since the query hint was created or last modified. Source of Query Store hint: user source is zero and system-generated is non-zero. Description of source of Query Store hint. Internal use only. Query Store hints are created by sys.sp_query_store_set_hints and removed by sys.sp_query_store_clear_hints . ﾉ Expand table
