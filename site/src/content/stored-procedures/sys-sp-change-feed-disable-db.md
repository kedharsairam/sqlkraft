---
name: "sys.sp_change_feed_disable_db"
title: "sp_change_feed_disable_db"
category: "general"
description: "2022 (16.x) and later versions Azure SQL Database SQL Managed Instance Azure Synapse Analytics Mirrored databases in Microsoft SQL database in Microsoft Fabric Disable the change feed at the database level, and then the metadata for all the associated This system stored procedure is used for: SQL database in Microsoft Fabric Microsoft Fabric mirrored databases Azure Synapse Link Transac"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_change_feed_disable_db
              [ ; ]
---

## Description

2022 (16.x) and later versions Azure SQL Database SQL Managed Instance Azure Synapse Analytics Mirrored databases in Microsoft SQL database in Microsoft Fabric Disable the change feed at the database level, and then the metadata for all the associated This system stored procedure is used for: SQL database in Microsoft Fabric Microsoft Fabric mirrored databases Azure Synapse Link database permissions, database role membership, or server role membership can execute this procedure. When the change feed is disabled with active table groups, all connections and schedulers are stopped immediately/forcefully without waiting for the current operations are completed. No This system stored procedure is used internally and isn't recommended for direct administrative use. Use Synapse Studio or the Fabric portal instead. Using this procedure

## Syntax

```sql
sys.sp_change_feed_disable_db
[ ; ]
```

## Remarks

2022 (16.x) and later versions

SQL Managed Instance

Mirrored databases in Microsoft

Disable the change feed at the database level, and then the metadata for all the associated

This system stored procedure is used for:

Microsoft Fabric mirrored databases

Azure Synapse Link

A user with

database permissions,

database role membership, or

server role membership can execute this procedure.

When the change feed is disabled with active table groups, all connections and schedulers are

stopped immediately/forcefully without waiting for the current operations are completed. No

This system stored procedure is used internally and isn't recommended for direct

administrative use. Use Synapse Studio or the Fabric portal instead. Using this procedure

could introduce inconsistency.
