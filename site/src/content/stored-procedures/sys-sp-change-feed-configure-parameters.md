---
name: "sys.sp_change_feed_configure_parameters"
title: "sp_change_feed_configure_parameters"
category: "general"
description: "2022 (16.x) and later versions Mirrored databases in Microsoft SQL database in Microsoft Fabric Configures optional performance settings for the change feed for the current database context. This system stored procedure is used to fine tune the operational performance for: SQL database in Microsoft Fabric Microsoft Fabric mirrored databases ."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sys.sp_change_feed_configure_parameters
      [ [ @maxtrans = ] max_trans ]
      [ , [ @pollinterval = ] polling_interval ]
      [ , [ @autoreseed = ] autoreseed ]
      [ , [ @autoreseedthreshold = autoreseed_threshold_percent ]
      [ , [ @dynamicmaxtrans = ] transactions ]
      [ , [ @dynamicmaxtranslowerbound = ] transactions_lower_bound ]
      [ ; ]
---

## Description

2022 (16.x) and later versions Mirrored databases in Microsoft SQL database in Microsoft Fabric Configures optional performance settings for the change feed for the current database context. This system stored procedure is used to fine tune the operational performance for: SQL database in Microsoft Fabric Microsoft Fabric mirrored databases. Indicates the maximum number of transactions to process in each scan cycle.

## Syntax

```sql
sys.sp_change_feed_configure_parameters
[ [ @maxtrans = ] max_trans ]
[ , [ @pollinterval = ] polling_interval ]
[ , [ @autoreseed = ] autoreseed ]
[ , [ @autoreseedthreshold = autoreseed_threshold_percent ]
[ , [ @dynamicmaxtrans = ] transactions ]
[ , [ @dynamicmaxtranslowerbound = ] transactions_lower_bound ]
[ ; ]
```
