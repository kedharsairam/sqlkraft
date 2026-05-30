---
name: "sys.crypt_properties"
title: "sys.crypt_properties"
category: "compatibility"
description: "The password that is required to decrypt the private key of the certificate or asymmetric key. This clause is only required if the private key isn't protected by the database master key. Specifies the signed, binary large object (BLOB) of the module. This clause is useful if you want to ship a module without shipping the private key. When you use this clause, only the module, signature, and public"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

The password that is required to decrypt the private key of the certificate or asymmetric key. This clause is only required if the private key isn't protected by the database master key. Specifies the signed, binary large object (BLOB) of the module. This clause is useful if you want to ship a module without shipping the private key. When you use this clause, only the module, signature, and public key are required to add the signed binary large object to a database. is the blob itself in hexadecimal format. The name of an asymmetric key with which to sign or counter-sign the stored procedure, function, assembly, or trigger. The module being signed or countersigned and the certificate or asymmetric key used to sign it must already exist. Every character in the module is included in the signature calculation. This sys.crypt_properties (Transact-SQL)

## Remarks

The password that is required to decrypt the private key of the certificate or asymmetric key.

This clause is only required if the private key isn't protected by the database master key.

Specifies the signed, binary large object (BLOB) of the module. This clause is useful if you want

to ship a module without shipping the private key. When you use this clause, only the module,

signature, and public key are required to add the signed binary large object to a database.

signed_blob

is the blob itself in hexadecimal format.

The name of an asymmetric key with which to sign or counter-sign the stored procedure,

function, assembly, or trigger.

The module being signed or countersigned and the certificate or asymmetric key used to sign

it must already exist. Every character in the module is included in the signature calculation. This

includes leading carriage returns and line feeds.

A module can be signed and countersigned by any number of certificates and asymmetric keys.

The signature of a module is dropped when the module is changed.

If a module contains an

clause, the security ID (SID) of the principal is also included

as a part of the signing process.

Data definition language (DDL) triggers and Inline table-valued functions can't be signed.

Information about signatures is visible in the

catalog view.

Module signing should only be used to grant permissions, never to deny or revoke

permissions.

sys.crypt_properties (Transact-SQL)

DROP SIGNATURE (Transact-SQL)

## Code Blocks

```sql
EXECUTE AS
```

`sys.crypt_properties`
