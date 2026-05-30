---
name: "To take Backup to Azure"
title: "To take Backup to Azure"
description: "create credential"
category: backup-restore
tags: ["backup", "backup-restore"]
pubDate: 2025-03-15
---

```sql
--create credential create credential credentialname with identity = N'storageaccountname',
secret = N'accesskeytostorageaccount'

--backup database to storage account backup database databasename to url = N'containerurl/filename.bak'
with credential = 'credentialname'
```
