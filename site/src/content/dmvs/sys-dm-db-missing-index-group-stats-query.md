---
name: "sys.dm_db_missing_index_group_stats_query"
title: "sys.dm_db_missing_index_group_stats_query"
category: "index"
description: "One missing index group may have several queries that needed the same index. For more information about individual queries that needed a specific index in this DMV, see sys.dm_db_missing_index_group_stats_query To query this dynamic management view, users must be granted the VIEW SERVER STATE permission or any permission that implies the VIEW SERVER STATE permission. Requires VIEW SERVER PERFORMAN"
tags: ["index","dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_db_missing_index_group_stats"
---

## Description

One missing index group may have several queries that needed the same index. For more information about individual queries that needed a specific index in this DMV, see sys.dm_db_missing_index_group_stats_query To query this dynamic management view, users must be granted the VIEW SERVER STATE permission or any permission that implies the VIEW SERVER STATE permission. Requires VIEW SERVER PERFORMANCE STATE permission on the server.

## Syntax

`sys.dm_db_missing_index_group_stats`
