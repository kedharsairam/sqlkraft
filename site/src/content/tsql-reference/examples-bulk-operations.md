---
name: "Examples: Bulk Operations"
title: "Examples: Bulk Operations"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## H. Create an external data source for bulk operations retrieving data

## from Azure Storage

## I. Create external data source using TDS 8.0 to connect with another

For a more detailed example on how to access delta files stored on Azure Data Lake Gen2, see

Virtualize delta table

with PolyBase.

2022 (16.x) and later versions.

Use the following data source for bulk operations using

BULK INSERT

or

OPENROWSET. The credential must set

as the identity, mustn't have the leading

in the SAS token, must have at least read

permission on the file that should be loaded (for example

), and the expiration period should be valid (all

dates are in UTC time). For more information on shared access signatures, see

Using Shared Access Signatures (SAS).

Applies to

: SQL Server 2025 (17.x) and later versions.

When using the latest Microsoft ODBC Driver 18 for SQL Server, you must use the

option under

, and

is also supported. If

isn't specified, the default

）

Important

Don't add a trailing

, file name, or shared access signature parameters at the end of the

URL when

configuring an external data source for bulk operations.

SQL Server

## J. Create external data source using encryption and

## TrustServerCertificate option

behavior is

, and you require a server certificate.

In this example, SQL Authentication is used. To protect the credential, you need a database master key (DMK). For

more information, see

CREATE MASTER KEY. The following sample creates a database scoped credential, with a

custom login and password.

The target server name is

, port

, and it's a default instance. By specifying

, the

connection uses TDS 8.0, and the server certificate is always verified. In this example, the

used is

:

Following the previous example here are two code samples. The first snippet has

and

set.

The following snippet doesn't have

enabled.
