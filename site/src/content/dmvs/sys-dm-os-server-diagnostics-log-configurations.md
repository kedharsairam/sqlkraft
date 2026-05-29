---
title: sys.dm_os_server_diagnostics_log_configurations
name: sys.dm_os_server_diagnostics_log_configurations
category: execution
description:
pubDate: 2026-05-29
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

## Returns one row with the current configuration for the SQL Server failover cluster diagnostic

log. These property settings determine whether the diagnostic logging is on or off, and the

location, number, and size of the log files.

is_enabled

Indicates if the logging is turned on or off.

1 = Diagnostics logging is turned on

0 = Diagnostics logging is turned off

max_size

Maximum size in megabytes to which each of the diagnostic logs can

grow. The default is 100 MB.

max_files

Maximum number of diagnostic log files that can be stored on the

computer before they are recycled for new diagnostic logs.

path

Path indicating the location of the diagnostic logs. The default location is

<\MSSQL\Log> within the installation folder of the SQL Server failover

cluster instance.

Requires VIEW SERVER STATE permissions on the SQL Server failover cluster instance.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

The following example uses sys.dm_os_server_diagnostics_log_configurations to return the

property settings for the SQL Server failover diagnostic logs.

ﾉ

Here's the result set.

1

<C:\Program Files\Microsoft SQL

Server\MSSQL13\MSSQL\Log>

10

10

View and Read Failover Cluster Instance Diagnostics Log

Last updated on 11/18/2025

ﾉ

## Applies to:

## sys.dm_os_stacks

## Basic

## S0

## S1

## elastic pools

```sql
SELECT <list of columns>
FROM sys.dm_os_server_diagnostics_log_configurations;
```
