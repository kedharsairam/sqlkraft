---
name: "To Create Database Snapshot"
title: "To Create Database Snapshot"
description: "diagnostic script for database operations."
category: "database"
tags: ["database"]
pubDate: 2025-03-15
---

```sql
create database databasesnapshotname on ( name = logicalfilenameofsourcedatabasemdffile,
filename = 'path(snapshotpath)\filename(snapshotphysicalfilename).ss') as snapshot of sourcedatabasename;
go
```
