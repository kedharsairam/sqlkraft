---
name: 'sys.dm_exec_function_stats'
title: 'sys.dm_exec_function_stats'
category: 'execution'
description: 'SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns aggregate performance statistics for cached functions. The view returns one row for each cached function plan, and the lifetime of the row is as long as the function remains cached. When a function is removed from the cache, the corresponding row is eliminated from this view. At that time, a Performance Statistics S'
tags: ["execution", "dmv"]
pubDate: 2026-05-29
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns aggregate performance statistics for cached functions. The view returns one row for each cached function plan, and the lifetime of the row is as long as the function remains cached. When a function is removed from the cache, the corresponding row is eliminated from this view. At that time, a Performance Statistics SQL trace event is raised similar to
