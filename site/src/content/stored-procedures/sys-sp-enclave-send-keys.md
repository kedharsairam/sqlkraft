---
name: 'sys.sp_enclave_send_keys'
title: 'sp_enclave_send_keys'
category: 'general'
description: 'SQL Server 2019 (15.x) and later - Windows only Sends columns encryption keys, defined in the database, to the server-side secure enclave used Always Encrypted with secure enclaves only sends only the keys that are enclave-enabled and encrypt columns that use randomized encryption and have indexes. For a regular user query, a client driver provides the enclave with the keys needed for computations'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_enclave_send_keys
  [ ; ]
---

## Description

SQL Server 2019 (15.x) and later - Windows only Sends columns encryption keys, defined in the database, to the server-side secure enclave used Always Encrypted with secure enclaves only sends only the keys that are enclave-enabled and encrypt columns that use randomized encryption and have indexes. For a regular user query, a client driver provides the enclave with the keys needed for computations in the query.

## Syntax

```sql
sp_enclave_send_keys
[ ; ]
```

## Arguments

Applies to:


SQL Server 2019 (15.x) and later - Windows only


Sends columns encryption keys, defined in the database, to the server-side secure enclave used


Always Encrypted with secure enclaves


only sends only the keys that are enclave-enabled and encrypt columns


that use randomized encryption and have indexes. For a regular user query, a client driver


provides the enclave with the keys needed for computations in the query.


sends all column encryption keys defined in the database and used for


indexes encrypted columns.


provides an easy way to send keys to the enclave and populate the


column encryption key cache for subsequent indexing operations. Use


A DBA to rebuild or alter indexes or statistics on encrypted database columns, if the DBA


doesn't have access to the column master key(s). See


Invoke indexing operations using


cached column encryption keys


SQL Server to complete the recovery of indexes on encrypted columns. See


An application using .NET Framework Data Provider for SQL Server to bulk load data to


encrypted columns.


To successfully invoke


, you need to connect to the database with Always


Encrypted and enclave computations enabled for the database connection. You also need to


have access to column master keys, protecting the column encryption keys, you're going to


send, and you need permissions to access Always Encrypted key metadata in the database.
