---
name: "sys.query_store_plan_feedback"
title: "sys.query_store_plan_feedback"
category: "query-store"
description: "2022 (16.x) and later versions SQL database in Microsoft Fabric Contains information about Query Store tuning via query feedback features, including cardinality estimation (CE) feedback degree of parallelism (DOP) feedback lock after qualification (LAQ) feedback Uniquely identifies the feedback change applied to a query."
tags: ["query-store","catalog-view"]
pubDate: 2026-05-29
syntax: |
  '{"node_id": value}, {"node_id": value},….'
---

## Description

2022 (16.x) and later versions SQL database in Microsoft Fabric Contains information about Query Store tuning via query feedback features, including cardinality estimation (CE) feedback degree of parallelism (DOP) feedback lock after qualification (LAQ) feedback Uniquely identifies the feedback change applied to a query. sys.query_store_plan (Transact-SQL) For CE feedback, displays query hints in use.

## Syntax

```sql
{"node_id": value}, {"node_id": value},….
```
