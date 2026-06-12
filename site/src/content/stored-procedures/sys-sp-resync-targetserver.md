---
name: "sys.sp_resync_targetserver"
title: "sp_resync_targetserver"
category: "general"
description: "Resynchronizes all multiserver jobs in the specified target server."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sp_post_msx_operation"
---

## Description

Resynchronizes all multiserver jobs in the specified target server.

## Syntax

`sp_post_msx_operation`

## Remarks

Resynchronizes all multiserver jobs in the specified target server.

The name of the server to resynchronize.

@server_name

, with no default. If

specified, all target servers are resynchronized.

(success) or

Reports the result of

deletes the current set of instructions for the target server and posts a

new set for the target server to download. The new set consists of an instruction to delete all

multiserver jobs, followed by an insert for each job currently targeted at the server.

## Examples

### Example 1

`SEATTLE1`

### Example 2

```sql
USE msdb;
GO
EXECUTE dbo.sp_resync_targetserver N
'SEATTLE1'
;
GO
```
