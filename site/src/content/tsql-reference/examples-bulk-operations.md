---
name: 'Examples: Bulk Operations'
title: 'Examples: Bulk Operations'
category: 'statements'
description: 'For a more detailed example on how to access delta files stored on Azure Data Lake Gen2, see'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## H. Create an external data source for bulk operations retrieving data

## from Azure Storage

## I. Create external data source using TDS 8.0 to connect with another

For a more detailed example on how to access delta files stored on Azure Data Lake Gen2, see

Virtualize delta table

with PolyBase

.

Applies to:

SQL Server 2022 (16.x) and later versions.

Use the following data source for bulk operations using

BULK INSERT

or

OPENROWSET

. The credential must set

as the identity, mustn't have the leading

in the SAS token, must have at least read

permission on the file that should be loaded (for example

), and the expiration period should be valid (all

dates are in UTC time). For more information on shared access signatures, see

Using Shared Access Signatures (SAS)

.

SQL

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

CREATE MASTER KEY

. The following sample creates a database scoped credential, with a

custom login and password.

SQL

The target server name is

, port

, and it's a default instance. By specifying

, the

connection uses TDS 8.0, and the server certificate is always verified. In this example, the

used is

:

SQL

Following the previous example here are two code samples. The first snippet has

and

set.

SQL

The following snippet doesn't have

enabled.

SQL

Related content

ALTER EXTERNAL DATA SOURCE (Transact-SQL)

CREATE DATABASE SCOPED CREDENTIAL (Transact-SQL)

CREATE EXTERNAL FILE FORMAT (Transact-SQL)

CREATE EXTERNAL TABLE (Transact-SQL)

sys.external_data_sources (Transact-SQL)

Using Shared Access Signatures (SAS)

PolyBase connectivity configuration (Transact-SQL)

Last updated on 03/17/2026

```sql
SHARED ACCESS SIGNATURE
```

```sql
?
```

```sql
srt=o&sp=r
```

```sql
Encryption
```

```sql
CONNECTION_OPTIONS
```

```sql
TrustServerCertificate
```

```sql
Encryption
```

```sql
--Create a database scoped credential using SAS Token
CREATE
DATABASE
SCOPED CREDENTIAL datalakegen2
WITH
IDENTITY
=
'SHARED ACCESS SIGNATURE'
,
SECRET =
'<DataLakeGen2_SAS_Token>'
;
GO
CREATE
EXTERNAL
DATA
SOURCE
data_lake_gen2_dfs
WITH
(
LOCATION =
'adls://<container>@<storage_account>.dfs.core.windows.net'
,
CREDENTIAL = datalakegen2
);
```

```sql
/
```

```sql
LOCATION
```

```sql
CREATE
DATABASE
SCOPED CREDENTIAL AccessAzureInvoices
WITH
IDENTITY
=
'SHARED ACCESS SIGNATURE'
,
-- Remove ? from the beginning of the SAS token
SECRET =
'<azure_shared_access_signature>'
;
CREATE
EXTERNAL
DATA
SOURCE
MyAzureInvoices
WITH
(
LOCATION =
'abs://<container>@<storage_account_name>.blob.core.windows.net/'
,
CREDENTIAL = AccessAzureInvoices,
);
```

```sql
Encrypt=Yes;TrustServerCertificate=No;
```

```sql
WINSQL2022
```

```sql
58137
```

```sql
Encrypt=Strict
```

```sql
HostnameinCertificate
```

```sql
WINSQL2022
```

```sql
Encryption
```

```sql
TrustServerCertificate
```

```sql
Encryption
```

```sql
CREATE
DATABASE
SCOPED CREDENTIAL SQLServerCredentials
WITH
IDENTITY
=
'<username>'
,
SECRET =
'<password>'
;
CREATE
EXTERNAL
DATA
SOURCE
SQLServerInstance2
WITH
(
LOCATION =
'sqlserver://WINSQL2022:58137'
,
CONNECTION_OPTIONS =
'Encrypt=Strict;HostnameInCertificate=WINSQL2022;'
CREDENTIAL = SQLServerCredentials
);
```

```sql
CREATE
EXTERNAL
DATA
SOURCE
SQLServerInstance2
WITH
(
LOCATION =
'sqlserver://WINSQL2022:58137'
,
CONNECTION_OPTIONS =
'Encrypt=Yes;HostnameInCertificate=WINSQL2022;TrustServerCertificate=Yes;'
CREDENTIAL = SQLServerCredentials
);
CREATE
EXTERNAL
DATA
SOURCE
SQLServerInstance2
WITH
(
LOCATION =
'sqlserver://WINSQL2022:58137'
,
CONNECTION_OPTIONS =
'Encrypt=no;'
CREDENTIAL = SQLServerCredentials
);
```
