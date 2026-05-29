---
name: "To Restore Encrypted Database in Another Instan"
title: "To Restore Encrypted Database in Another Instan"
description: "first create a master key"
category: security-audit
tags: ["database", "encryption", "restore", "security-audit"]
pubDate: 2025-03-15
---

```sql
--first create a master key
use master
create master key encryption by password = '[password]'

--then create a certificate using the backups of source certificate and key
create certificate newcertificatename
from file = 'path\filename.cer'
with private key (file = 'path\filename.key', decryption by password = '[password]')

--now you can restore the database from the backup normally
```
