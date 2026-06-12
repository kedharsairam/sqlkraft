---
name: "sys.database_mirroring"
title: "sys.database_mirroring"
category: "compatibility"
description: "Returns one row for each database in the instance of SQL Server. If the database isn't ONLINE or database mirroring isn't enabled, the values of all columns except database_id are NULL."
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns one row for each database in the instance of SQL Server. If the database isn't ONLINE or database mirroring isn't enabled, the values of all columns except database_id are NULL. To see the row for a database other than master or tempdb, you must either be the database owner or have at least ALTER ANY DATABASE or VIEW ANY DATABASE server-level permission or CREATE DATABASE permission in the master database. To see non-NULL values on a mirror

## Code Blocks

`database_id`

`mirroring_guid`

`mirroring_state`
