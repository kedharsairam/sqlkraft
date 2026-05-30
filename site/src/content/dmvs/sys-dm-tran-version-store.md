---
name: "sys.dm_tran_version_store"
title: "sys.dm_tran_version_store"
category: "io"
description: "SQL database in Microsoft Fabric Returns a virtual table that displays all version records in the version store. is inefficient to run because it queries the entire version store, and the version store can be very large. Each versioned record is stored as binary data together with some tracking or status information. Similar to records in database tables, version-store records are stored in 8192- "
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_tran_version_store"
---

## Description

SQL database in Microsoft Fabric Returns a virtual table that displays all version records in the version store. is inefficient to run because it queries the entire version store, and the version store can be very large. Each versioned record is stored as binary data together with some tracking or status information. Similar to records in database tables, version-store records are stored in 8192- byte pages. If a record exceeds 8192 bytes, the record will be split across two different records.

## Syntax

```sql
sys.dm_tran_version_store
```
