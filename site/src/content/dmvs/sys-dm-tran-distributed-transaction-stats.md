---
name: 'sys.dm_tran_distributed_transaction_stats'
title: 'sys.dm_tran_distributed_transaction_stats'
category: 'io'
description: 'Returns information about MSDTC statistics in SQL Server. The number of transactions that were shut down before they were The highest number of aborted transactions since DTC last started. The number of aborted transactions that were manually shut down The number of committed transactions for the instance. The highest number of committed transactions since DTC last started. The number of committed'
tags: ["io", "dmv"]
pubDate: 2026-05-29
---

## Description

Returns information about MSDTC statistics in SQL Server. The number of transactions that were shut down before they were The highest number of aborted transactions since DTC last started. The number of aborted transactions that were manually shut down The number of committed transactions for the instance. The highest number of committed transactions since DTC last started. The number of committed transactions that were manually

## Permissions

Article • 02/27/2023 SQL Server 2022 (16.x) Azure SQL Managed Instance Returns information about MSDTC statistics in SQL Server. aborted int The number of transactions that were shut down before they were completed. aborted_max int The highest number of aborted transactions since DTC last started. forced_abort int The number of aborted transactions that were manually shut down before they were completed. committed int The number of committed transactions for the instance. committed_max int The highest number of committed transactions since DTC last started. forced_commit int The number of committed transactions that were manually committed. heuristic int TBD heuristic_max int TBD in_doubt int The number of in doubt transactions. in_doubt_max int The highest number of in doubt transactions since DTC last started. open int The number of running transactions for the instance. open_max int The highest number of concurrently running transactions since DTC last started. single_phase_in_doubt int TBD ﾉ sys.sp_manage_distributed_transaction (Transact-SQL) sys.dm_tran_distributed_transaction_stats (Transact-SQL) Related content
