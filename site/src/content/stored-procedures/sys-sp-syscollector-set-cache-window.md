---
name: "sys.sp_syscollector_set_cache_window"
title: "sp_syscollector_set_cache_window"
category: "general"
description: "Sets the number of times to attempt a data upload if a failure occurs. Retrying an upload in the event of a failure mitigates the risk of losing collected data. Transact-SQL syntax conventions The number of times a failed data upload to the management data warehouse is retried Cache all the upload data from the previous upload failures. Don't cache any data from an upload failure. previous upload "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_set_cache_window [ [ @cache_window = ] cache_window ]
  [ ; ]
---

## Description

Sets the number of times to attempt a data upload if a failure occurs. Retrying an upload in the event of a failure mitigates the risk of losing collected data. Transact-SQL syntax conventions The number of times a failed data upload to the management data warehouse is retried Cache all the upload data from the previous upload failures. Don't cache any data from an upload failure. previous upload failures, where

## Syntax

```sql
sp_syscollector_set_cache_window [ [ @cache_window = ] cache_window ]
[ ; ]
```

## Examples

### Example 1

```sql
USE msdb;
GO
EXECUTE dbo.sp_syscollector_disable_collector;
GO
EXECUTE dbo.sp_syscollector_set_cache_window 3;
GO
EXECUTE dbo.sp_syscollector_enable_collector;
```
