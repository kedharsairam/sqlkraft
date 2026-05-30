---
title: "Diagnostics Log"
topic: "high-availability"
description: |
  Article

  •

  04/02/2024

  Applies to:

  SQL Server

  All critical errors and warning events for the SQL Server Resource DLL are written to the

  Windows event log. A running log of the diagnostic informati
tags:
  - "high-availability"
  - "diagnostics-log"
pubDate: 2025-12-01
---

Article

•

04/02/2024

Applies to:

SQL Server

All critical errors and warning events for the SQL Server Resource DLL are written to the

Windows event log. A running log of the diagnostic information specific to SQL Server is

captured by the

sp_server_diagnostics (Transact-SQL)

system stored procedure and is written to

the SQL Server failover cluster diagnostics (also known as the

SQLDIAG

logs) log files.

File name, location and format

,

Security

SQL Server Management Studio

,

Transact-SQL

Transact-SQL

By default, the SQLDIAG are stored under a local LOG folder of the SQL Server instance

directory, for example, 'C\Program Files\Microsoft SQL Server\MSSQL13.

<InstanceName>\MSSQL\LOG' of the owning node of the Always On Failover Cluster Instance

(FCI). The maximum size of each SQLDIAG log file is fixed at 100 MB. Ten such log files are

stored on the computer before they are recycled for new logs. The file name is of the following

format

where the last part 'xxxxxxxx' is

an auto-generated number. For example for a default instance the file name would be

and for a named instance the name

would be

The logs use the extended events file format. The

system

function can be used to read the files that are created by Extended Events and display them as

a result-set. One event, in XML format, is returned per row. For more information, see

sys.fn_xe_file_target_read_file (Transact-SQL)

.

```cmd
MACHINE_SQLINSTANCE_SQLDIAG_0_xxxxxxxxxxxxxxxxx.xel
NODE1_MSSQLSERVER_SQLDIAG_0_133177967257760000.xel
NODE1_SQL2019INST_SQLDIAG_0_133177967257760000.xel sys.fn_xe_file_target_read_file
```
