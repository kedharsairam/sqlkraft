---
name: "sys.dm_db_task_space_usage"
title: "sys.dm_db_task_space_usage"
category: "execution"
description: "Analytics Platform System (PDW) Returns page allocation and deallocation activity by task for the database. Request ID within the session. A request is also called a batch and may contain one or more queries. A session may have multiple requests active at the same time. Each query in the request may start multiple threads (tasks), if a parallel execution Execution context ID of the task."
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_pdw_nodes_db_task_space_usage"
---

## Description

Analytics Platform System (PDW) Returns page allocation and deallocation activity by task for the database. Request ID within the session. A request is also called a batch and may contain one or more queries. A session may have multiple requests active at the same time. Each query in the request may start multiple threads (tasks), if a parallel execution Execution context ID of the task. For more information,

## Syntax

`sys.dm_pdw_nodes_db_task_space_usage`
