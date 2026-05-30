---
name: "Understand DBCC error messages"
title: "Understand DBCC error messages"
category: "statements"
description: "command finishes, a message is written to the SQL Server error log."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

After the

command finishes, a message is written to the SQL Server error log.

If the DBCC command successfully executes, the message indicates a successful completion

and the amount of time that the command ran. If the DBCC command stops before completing

the check because of an error, the message indicates the command was terminated, a state

value, and the amount of time the command ran. The following table lists and describes the

state values that can be included in the message.

## Description

0

Error number 8930 was raised. This indicates a metadata corruption that caused the DBCC

command to terminate.

1

Error number 8967 was raised. There was an internal DBCC error.

2

A failure occurred during emergency mode database repair.

3

This indicates a metadata corruption that caused the DBCC command to terminate.

4

An assert or access violation was detected.

5

An unknown error occurred that terminated the DBCC command.

A mini-dump file (

) is created in the SQL Server

directory whenever

detects a corruption error. When the

Feature Usage

data collection and

Error

Reporting

features are enabled for the instance of SQL Server, the file is automatically

forwarded to Microsoft. The collected data is used to improve SQL Server functionality.

The dump file contains the results of the

command and additional diagnostic

output. The file has restricted discretionary access-control lists (DACLs). Access is limited to the

SQL Server service account and members of the sysadmin role. By default, the sysadmin role

７

Note

This feature is not available in every edition of SQL Server. For more information, see

parallel consistency check in the

section of

.

Expand table

```sql
DBCC CHECKTABLE
```

```sql
SQLDUMP<nnnn>.txt
```

`LOG`

```sql
DBCC
CHECKTABLE
```

```sql
DBCC CHECKTABLE
```
