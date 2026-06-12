---
name: "sys.sp_add_data_file_recover_suspect_db"
title: "sp_add_data_file_recover_suspect_db"
category: "general"
description: "Adds a data file to a filegroup when recovery can't complete on a database due to insufficient space on the file group (error 1105). After the file is added, this stored procedure turns off the suspect setting and completes the recovery of the database. The parameters are the same as The filegroup you're adding the file to. which indicates the primary file."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "ALTER DATABASE <database_name> ADD FILE"
---

## Description

Adds a data file to a filegroup when recovery can't complete on a database due to insufficient space on the file group (error 1105). After the file is added, this stored procedure turns off the suspect setting and completes the recovery of the database. The parameters are the same as The filegroup you're adding the file to. which indicates the primary file.

## Syntax

```sql
ALTER DATABASE <database_name> ADD FILE
```
