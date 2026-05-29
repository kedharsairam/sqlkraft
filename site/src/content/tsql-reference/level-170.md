---
name: 'level 170'
title: 'level 170'
category: 'statements'
description: 'compatibility level (140). Database compatibility level 130 retained the SQL Server 2016'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

compatibility level (140). Database compatibility level 130 retained the SQL Server 2016

(13.x) cardinality estimation behavior.

The following table summarizes this behavior:

13 (SQL Server 2016 (13.x))

< 130

130

Disabled

Enabled

14 (SQL Server 2017 (14.x))

< 140

140

Disabled

Enabled

15 (SQL Server 2019 (15.x))

< 150

150

Disabled

Enabled

16 (SQL Server 2022 (16.x))

< 160

160

Disabled

Enabled

17 (SQL Server 2025 (17.x))

< 170

170

Disabled

Enabled

Also applicable to Azure SQL Database and SQL database in Microsoft Fabric.

Other differences between specific compatibility levels are available in the next sections of this

article.

This section describes new behaviors introduced with compatibility level 170.

To protect the key material of the

symmetric key, database master key and

service master key, SQL Server and Azure

SQL stores the key material in encrypted

form. The encryption uses PKCS#1 v1.5

padding mode.

To protect the key material of the symmetric key, database

master key and service master key, SQL Server and Azure

SQL stores the key material in encrypted form. The

encryption uses OAEP-256 padding mode. In the

dm_database_encryption_keys, the encryptor_type will be

displayed as

instead of

.

ﾉ

Expand table

1

1

1

1

1

ﾉ

Expand table

#### Compatibility level setting of 160 or

#### lower

#### Compatibility level setting of 170

#### Compatibility level setting of 150 or lower

#### Compatibility level setting of 160

```sql
CERTIFICATE_OAEP_256
```

```sql
CERTIFICATE
```
