---
name: "sys.sp_attach_db"
title: "sp_attach_db"
category: "general"
description: "Attaches a database to a server. Don't attach or restore databases from unknown or untrusted sources. Such databases could contain malicious code that might execute unintended Transact-SQL code or cause errors by modifying the schema or the physical database structure. Before you use a database from an unknown or untrusted source, run on the database on a nonproduction server and also examine the "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "CREATE DATABASE <database_name> FOR ATTACH"
---

## Description

Attaches a database to a server. Don't attach or restore databases from unknown or untrusted sources. Such databases could contain malicious code that might execute unintended Transact-SQL code or cause errors by modifying the schema or the physical database structure. Before you use a database from an unknown or untrusted source, run on the database on a nonproduction server and also examine the code, such as stored procedures or other user-defined code, in the

## Syntax

```sql
CREATE DATABASE <database_name> FOR ATTACH
```
