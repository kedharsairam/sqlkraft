---
name: "sys.dm_exec_query_memory_grants"
title: "sys.dm_exec_query_memory_grants"
category: "execution"
description: "Analytics Platform System (PDW) Returns information about all queries that have requested and are waiting for a memory grant or have been given a memory grant. Queries that do not require a memory grant will not appear in this view. For example, sort and hash join operations have memory grants for query execution, while queries without an clause will not have a memory grant. In Azure SQL Database,"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_pdw_nodes_exec_query_memory_grants"
---

## Description

Analytics Platform System (PDW) Returns information about all queries that have requested and are waiting for a memory grant or have been given a memory grant. Queries that do not require a memory grant will not appear in this view. For example, sort and hash join operations have memory grants for query execution, while queries without an clause will not have a memory grant. In Azure SQL Database, dynamic management views cannot expose information that would

## Syntax

```sql
sys.dm_pdw_nodes_exec_query_memory_grants
```
