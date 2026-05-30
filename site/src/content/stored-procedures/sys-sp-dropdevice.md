---
name: "sys.sp_dropdevice"
title: "sp_dropdevice"
category: "general"
description: "Drops a database device or backup device from a SQL Server Database Engine instance, Transact-SQL syntax conventions The logical name of the database device or backup device as listed in Specifies whether the physical backup device file should be deleted. , the physical backup device disk file is deleted."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "master.dbo.sysdevices"
---

## Description

Drops a database device or backup device from a SQL Server Database Engine instance, Transact-SQL syntax conventions The logical name of the database device or backup device as listed in Specifies whether the physical backup device file should be deleted. , the physical backup device disk file is deleted.

## Syntax

```sql
master.dbo.sysdevices
```

## Examples

### Example 1

```sql
sp_dropdevice
```

### Example 2

```sql
tapedump1
```

### Example 3

```sql
EXECUTE
sp_dropdevice
'tapedump1'
;
```
