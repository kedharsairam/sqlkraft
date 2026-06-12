---
name: "sys.key_encryptions"
title: "sys.key_encryptions"
category: "compatibility"
description: "Returns a row for each symmetric key encryption specified by using the To protect the key material of the symmetric key, SQL Server and Azure SQL store the key material in encrypted form. Historically, this encryption utilized PKCS#1 v1.5 padding mode; starting with database compatibility level 170, the encryption uses OAEP-256 padding mode."
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: |
  ENCRYPTION BY SYMMETRIC KEY
              ENCRYPTION BY PASSWORD
---

## Description

Returns a row for each symmetric key encryption specified by using the To protect the key material of the symmetric key, SQL Server and Azure SQL store the key material in encrypted form. Historically, this encryption utilized PKCS#1 v1.5 padding mode; starting with database compatibility level 170, the encryption uses OAEP-256 padding mode.

## Syntax

```sql
ENCRYPTION BY SYMMETRIC KEY
ENCRYPTION BY PASSWORD
```
