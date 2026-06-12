---
name: "To Restore Database or Point of Failure"
title: "To Restore Database or Point of Failure"
description: "for full backup"
category: "backup-restore"
tags: ["backup-restore","database","restore"]
pubDate: 2025-03-15
---

```sql
--for full backup restore database databasename from disk = 'path\filename.bak'
with norecovery,
move 'mdffilename' to 'newpath\filename.mdf',
move 'ldffilename' to 'newpath\filename.ldf'

--for differential backup restore database databasename from disk = 'path\filename.bak' with norecovery

--for log backup restore log databasename from disk = 'path\filename.trn' with recovery

--for changing the recovery status of a database restore database databasename with recovery
```
