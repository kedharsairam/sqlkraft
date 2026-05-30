---
name: "sys.sp_dbmmonitoraddmonitoring"
title: "sp_dbmmonitoraddmonitoring"
category: "general"
description: "Creates a database mirroring monitor job that periodically updates the mirroring status for every mirrored database on the server instance. Transact-SQL syntax conventions Specifies the interval between updates in minutes. , with a default of This value can be from 1 to 120 minutes. If update period is set too low, the response time might increase for clients."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbmmonitoraddmonitoring [ [ @update_period = ] update_period ]
  [ ; ]
---

## Description

Creates a database mirroring monitor job that periodically updates the mirroring status for every mirrored database on the server instance. Transact-SQL syntax conventions Specifies the interval between updates in minutes. , with a default of This value can be from 1 to 120 minutes. If update period is set too low, the response time might increase for clients.

## Syntax

```sql
sp_dbmmonitoraddmonitoring [ [ @update_period = ] update_period ]
[ ; ]
```

## Remarks

Applies to:

Creates a database mirroring monitor job that periodically updates the mirroring status for

every mirrored database on the server instance.

Transact-SQL syntax conventions

Specifies the interval between updates in minutes.

@update_period

, with a default of

This value can be from 1 to 120 minutes.

If update period is set too low, the response time might increase for clients.

## Examples

### Example 1

`sp_dbmmonitoraddmonitoring`

### Example 2

```sql
ALTER DATABASE
```

### Example 3

`sp_dbmmonitoraddmonitoring`

### Example 4

```sql
3
```

### Example 5

`sp_dbmmonitoraddmonitoring`

### Example 6

```sql
EXECUTE sp_dbmmonitoraddmonitoring 3;
```
