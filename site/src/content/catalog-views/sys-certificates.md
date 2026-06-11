---
name: "sys.certificates"
title: "sys.certificates"
category: "compatibility"
description: "Analytics Platform System (PDW) Returns a row for each certificate in the database."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
  Cert_ID(
  'ABerglundCert3'
  );
  GO
---

## Description

Analytics Platform System (PDW) Returns a row for each certificate in the database. Name of the certificate. Is unique within the database. ID of the certificate. Is unique within the database. ID of the database principal that owns this certificate. How the private key is encrypted. NA = There is no private key for the certificate MK = Private key is encrypted by the master key PW = Private key is encrypted by a user-defined

## Syntax

```sql
SELECT
Cert_ID(
'ABerglundCert3'
);
GO
```
