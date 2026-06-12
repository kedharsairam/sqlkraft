---
name: "sys.fn_check_object_signatures"
title: "sys.fn_check_object_signatures"
category: "system"
description: "Returns a list of all signable objects and indicates whether an object is signed by a specified certificate or asymmetric key. If the object is signed by the specified certificate or asymmetric key signed, it also returns whether the object's signature is valid."
tags: ["system","function"]
pubDate: 2026-05-29
syntax: |
  fn_ check_object_signatures (
            { '@class' } , { @thumbprint }
            )
---

## Description

Returns a list of all signable objects and indicates whether an object is signed by a specified certificate or asymmetric key. If the object is signed by the specified certificate or asymmetric key signed, it also returns whether the object's signature is valid. Identifies the type of thumbprint being provided: SHA-1 hash of the certificate with which the key is encrypted, or the GUID of the asymmetric

## Syntax

```sql
fn_ check_object_signatures (
{ '@class' } , { @thumbprint }
)
```

## Examples

### Example 1

`master`

### Example 2

`is_signed`

### Example 3

`is_signature_valid`

### Example 4

```sql
USE master;
-- Declare a variable to hold the thumbprint.
DECLARE @thumbprint varbinary(20) ;
-- Populate the thumbprint variable with the master database schema signing certificate.
SELECT @thumbprint = thumbprint
FROM sys.certificates
WHERE name LIKE '%SchemaSigningCertificate%' ;
-- Evaluates the objects signed by the schema signing certificate
SELECT type, entity_id, OBJECT_NAME(entity_id) AS [object name], is_signed,
is_signature_valid
FROM sys.fn_check_object_signatures ('certificate', @thumbprint) ;
```
