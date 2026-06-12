---
name: "sys.dm_exec_cached_plans"
title: "sys.dm_exec_cached_plans"
category: "execution"
description: "Returns a row for each query plan that is cached by SQL Server for faster query execution. You can use this dynamic management view to find cached query plans, cached query text, the amount of memory taken by cached plans, and the reuse count of the cached plans."
tags: ["execution","dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_pdw_nodes_exec_cached_plans"
---

## Description

Analytics Platform System (PDW) Returns a row for each query plan that is cached by SQL Server for faster query execution. You can use this dynamic management view to find cached query plans, cached query text, the amount of memory taken by cached plans, and the reuse count of the cached plans. In Azure SQL Database, dynamic management views can't expose information that would impact database containment or expose information about other databases the user has access

## Syntax

`sys.dm_pdw_nodes_exec_cached_plans`
