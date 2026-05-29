---
title: "Considerations for Replaying Traces"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  SQL Server Profiler can't replay the following kinds of traces:

  Traces that contain transactional replication and other transaction lo
tags:
  - "profiler"
  - "considerations-for-replaying-traces"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server Profiler can't replay the following kinds of traces:

Traces that contain transactional replication and other transaction log activity. These

events are skipped. Other types of replication don't mark the transaction log so they

aren't affected.

Traces that contain operations that involve globally unique identifiers (GUID). These

events will be skipped.

Traces that contain operations on

,

, and

columns involving the

utility,

the

,

,

, and

statements, and full-text

operations. These events are skipped.

Traces that contain session binding:

and

system stored

procedures. These events are skipped.

If you don't use the preconfigured replay template (

), and don't capture all

required data, SQL Server Profiler doesn't replay the trace. For more information, see

Replay

Requirements

.

For information about what permissions are required to replay a trace, see

Permissions

required to run SQL Server Profiler

.

bcp Utility

SQL Server Event Class Reference

sp_getbindtoken

sp_bindsession

BULK INSERT (Transact-SQL)

READTEXT (Transact-SQL)

WRITETEXT (Transact-SQL)

UPDATETEXT (Transact-SQL)

```cmd
BULK INSERT
READTEXT
WRITETEXT
UPDATETEXT
sp_getbindtoken
```
