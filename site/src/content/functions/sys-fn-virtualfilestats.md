---
name: "sys.fn_virtualfilestats"
title: "sys.fn_virtualfilestats"
category: "system"
description: "Returns I/O statistics for database files, including log files. In SQL Server, this information is also , with no default. Specify NULL to return information for all databases in the instance of SQL Server. , with no default. Specify NULL to return information for all files Database timestamp at which the data was taken."
tags: ["system","function"]
pubDate: 2026-05-29
syntax: "fn_virtualfilestats ( { database_id | NULL } , { file_id | NULL } )"
---

## Description

Returns I/O statistics for database files, including log files. In SQL Server, this information is also , with no default. Specify NULL to return information for all databases in the instance of SQL Server. , with no default. Specify NULL to return information for all files Database timestamp at which the data was taken. Number of reads issued on the file.

## Syntax

```sql
fn_virtualfilestats ( { database_id | NULL } , { file_id | NULL } )
```
