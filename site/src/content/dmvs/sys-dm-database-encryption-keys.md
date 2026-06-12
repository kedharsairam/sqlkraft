---
name: "sys.dm_database_encryption_keys"
title: "sys.dm_database_encryption_keys"
category: "io"
description: "When a symmetric key is created, the symmetric key must be encrypted by using at least one of the following options: The key can have more than one encryption of each type. In other words, a single symmetric key can be encrypted by using multiple certificates, passwords, symmetric keys, and asymmetric keys at the same time. To protect the key material of the symmetric key, SQL Server and Azure SQL"
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "is_honor_broker_priority_on"
---

## Description

When a symmetric key is created, the symmetric key must be encrypted by using at least one of the following options: The key can have more than one encryption of each type. In other words, a single symmetric key can be encrypted by using multiple certificates, passwords, symmetric keys, and asymmetric keys at the same time. To protect the key material of the symmetric key, SQL Server and Azure SQL store the key material in encrypted form. Historically, this encryption used PKCS#1 v1.5 padding mode; starting with database compatibility level 170, the encryption uses OAEP-256 padding mode for encryption by certificate or asymmetric key. In The optional password can be used to encrypt the symmetric key before distributing the key to multiple users. Temporary keys are owned by the user that creates them.

## Syntax

`is_honor_broker_priority_on`

## Remarks

When a symmetric key is created, the symmetric key must be encrypted by using at least one

of the following options:

certificate

symmetric key

asymmetric key

The key can have more than one encryption of each type. In other words, a single symmetric

key can be encrypted by using multiple certificates, passwords, symmetric keys, and

asymmetric keys at the same time.

To protect the key material of the symmetric key, SQL Server and Azure SQL store the key

material in encrypted form. Historically, this encryption used PKCS#1 v1.5 padding mode;

starting with database compatibility level 170, the encryption uses OAEP-256 padding mode

for encryption by certificate or asymmetric key. In

displays as

The optional password can be used to encrypt the symmetric key before distributing the key to

multiple users.

Temporary keys are owned by the user that creates them. Temporary keys are only valid for the

current session.

Beginning with SQL Server 2016 (13.x), all algorithms other than AES_128, AES_192, and

AES_256 are deprecated. To use older algorithms (not recommended), you must set the

database to database compatibility level 120 or lower.

When a symmetric key is encrypted with a password instead of a certificate (or another

key), the TRIPLE DES encryption algorithm is used to encrypt the password. Because of

this, keys that are created with a strong encryption algorithm, such as AES, are themselves

secured by a weaker algorithm.
