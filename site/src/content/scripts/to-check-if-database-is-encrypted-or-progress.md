---
name: "To Check if Database is Encrypted or Progress"
title: "To Check if Database is Encrypted or Progress"
description: "encryption_state = 3 encrypted; =2 in progress"
category: security-audit
tags: ["database", "encryption", "health-check", "security-audit"]
pubDate: 2025-03-15
---

```sql
--encryption_state = 3 encrypted; =2 in progress

USE master
GO
SELECT db_name(database_id) [TDE Encrypted DB Name], c.name as CertName, encryptor_thumbprint , dek.*     FROM sys.dm_database_encryption_keys dek     INNER JOIN sys.certificates c on dek.encryptor_thumbprint = c.thumbprint
```
