---
name: "sys.fn_backup_instance_config"
title: "managed_backup.fn_backup_instance_config"
category: "backup-restore"
description: "The type of encryptor used: Certificate or Asymmetric Key. Is set to NULL if there is no encryptor specified."
tags: ["backup-restore","function"]
pubDate: "2026-05-29"
syntax: |
  Use msdb;
    GO
    SELECT * FROM managed_backup.fn_backup_instance_config ();
---

## Description

The type of encryptor used: Certificate or Asymmetric Key. Is set to NULL if there is no encryptor specified.

## Syntax

```sql
Use msdb;
GO
SELECT * FROM managed_backup.fn_backup_instance_config ();
```

## Examples

### Example 1

```sql
Use msdb;
GO
SELECT * FROM managed_backup.fn_backup_instance_config ();
```
