---
name: "sys.sp_add_log_file_recover_suspect_db"
title: "sp_add_log_file_recover_suspect_db"
category: "general"
description: "Adds a log file to a database when recovery can't complete on a database due to insufficient log space (error 9002). After the file is added, the suspect setting and completes the recovery of the database. The parameters are the same The name used in the SQL Server to reference the file. The name must be unique in the server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_add_log_file_recover_suspect_db"
---

## Description

Adds a log file to a database when recovery can't complete on a database due to insufficient log space (error 9002). After the file is added, the suspect setting and completes the recovery of the database. The parameters are the same The name used in the SQL Server to reference the file. The name must be unique in the server. The path and file name used by the operating system for the file.

## Syntax

`sp_add_log_file_recover_suspect_db`

## Examples

### Example 1

`db1`

### Example 2

```sql
USE master
;
GO
EXECUTE sp_add_log_file_recover_suspect_db db1,
logfile2,
'C:\Program Files\Microsoft SQL
Server\MSSQL16.MSSQLSERVER\MSSQL\Data\db1_logfile2.ldf'
,
'1 MB'
;
```
