---
name: "sys.dm_os_wait_stats"
title: "sys.dm_os_wait_stats"
category: "os"
description: "Analytics Platform System (PDW) Returns information about all the waits encountered by threads that executed. You can use this aggregated view to diagnose performance issues with SQL Server and also with specific queries sys.dm_exec_session_wait_stats provides similar information by session."
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_pdw_nodes_os_wait_stats"
---

## Description

Analytics Platform System (PDW) Returns information about all the waits encountered by threads that executed. You can use this aggregated view to diagnose performance issues with SQL Server and also with specific queries sys.dm_exec_session_wait_stats provides similar information by session. Name of the wait type. For more information, see Number of waits on this wait type. This counter is incremented at

## Syntax

`sys.dm_pdw_nodes_os_wait_stats`

## Permissions

SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns information about all the waits encountered by threads that executed. You can use this aggregated view to diagnose performance issues with SQL Server and also with specific queries and batches. sys.dm_exec_session_wait_stats provides similar information by session. Name of the wait type. For more information, see Types of waits , later in this article. Number of waits on this wait type. This counter is incremented at the start of each wait. Total wait time for this wait type in milliseconds. This time is inclusive of . Maximum wait time on this wait type. Difference between the time that the waiting thread was signaled and when it started running. The identifier for the node that this distribution is on. : Azure Synapse Analytics, Analytics Platform System (PDW) On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the ７ To call this dynamic management view from Azure Synapse Analytics or Analytics Platform System (PDW), use the name . This syntax is not supported by serverless SQL pool in Azure Synapse Analytics. ﾉ Thread and task architecture guide Transaction locking and row versioning guide sys.dm_os_wait_stats (Transact-SQL) sys.dm_exec_requests (Transact-SQL) Last updated on 11/18/2025 For information about types of waits, see sys.dm_os_wait_stats . If the request is currently blocked, this column returns the duration in milliseconds, of the current wait. Not nullable. If this request has previously been blocked, this column returns the type of the last wait. Not nullable. If the request is currently blocked, this column returns the resource for which the request is currently waiting. Not nullable. Number of transactions that are open for this request. Not nullable. Number of result sets that are open for this request. Not nullable. ID of the transaction in which this request executes. Not nullable. CONTEXT_INFO value of the session. Nullable. Percentage of work completed for the following commands: option with Not nullable. Internal only. Not nullable. CPU time in milliseconds that is used by the request. Not nullable.
