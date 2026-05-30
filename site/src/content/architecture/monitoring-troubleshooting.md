---
title: "Monitoring & troubleshooting"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  This article provides information about the tools that can be used to monitor and troubleshoot

  managed database objects and assemblies running in SQL
tags:
  - "clr-integration"
  - "monitoring-troubleshooting"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

This article provides information about the tools that can be used to monitor and troubleshoot

managed database objects and assemblies running in SQL Server.

SQL Server provides SQL Trace and event notifications to monitor events that occur in the

Database Engine. By recording specified events, SQL Trace helps you troubleshoot

performance, audit database activity, gather sample data for a test environment, debug

Transact-SQL statements and stored procedures, and gather data for performance analysis

tools. For more information, see

SQL Trace

and

Extended Events overview

.

Description

SQL Server Event Class Reference

Used to monitor assembly load requests (success and

failures).

SQL:BatchStarting Event Class

,

SQL:BatchCompleted Event Class

Provides information about Transact-SQL batches that

have started or completed.

SP:Starting Event Class

,

SP:Completed Event

Class

Used to monitor the execution of Transact-SQL stored

procedures.

SQL:StmtStarting Event Class

,

SQL:StmtCompleted Event Class

Used to monitor the execution of CLR and Transact-

SQL routines.

SQL Server provides objects and counters that can be used by Performance Monitor to monitor

activity in computers running an instance of SQL Server. An object is any SQL Server resource,

such as a SQL Server lock or a Windows process. Each object contains one or more counters

that determine various aspects of the objects to monitor. For more information, see

Use SQL

Server Objects

.

ﾉ

Expand table

ﾉ

Expand table
