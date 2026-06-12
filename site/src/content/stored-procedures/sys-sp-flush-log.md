---
name: "sys.sp_flush_log"
title: "sys.sp_flush_log"
category: "general"
description: "2016 (13.x) and later versions Flushes to disk the transaction log of the current database, thereby hardening all previously committed delayed durable transactions. If you choose to use delayed transaction durability because of the performance benefits, but you also want to have a guaranteed limit on the amount of data that is lost on server crash or on a regular schedule. For example,"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  EXECUTE
              sys.sp_flush_log;
---

## Description

2016 (13.x) and later versions Flushes to disk the transaction log of the current database, thereby hardening all previously committed delayed durable transactions. If you choose to use delayed transaction durability because of the performance benefits, but you also want to have a guaranteed limit on the amount of data that is lost on server crash or on a regular schedule.

## Syntax

```sql
EXECUTE sys.sp_flush_log;
```
