---
title: 'Security'
topic: 'query-processing'
description: 'Specifying the SQLOLEDB provider for linked servers.'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Deprecated feature

Replacement

Feature name

Specifying the SQLOLEDB provider for linked servers.

Microsoft OLE DB Driver for SQL Server

SQLOLEDB for linked servers

Deprecated feature

Replacement

Feature name

FILE_ID

INDEXKEY_PROPERTY

FILE_IDEX

FILE_ID

INDEXKEY_PROPERTY

Deprecated feature

Replacement

Feature name

The

or

statement with

the

option.

sys.endpoint_webmethods

Use Windows Communications Foundation

(WCF) or ASP.NET instead.

/

EXT_soap_endpoints

Deprecated

feature

Replacement

Feature

name

DB-Library

Embedded

SQL for C

Although the Database Engine still supports connections from existing applications that use the DB-Library

and Embedded SQL APIs, it doesn't include the files or documentation required to do programming work on

applications that use these APIs. A future version of the SQL Server Database Engine drops support for

connections from DB-Library or Embedded SQL applications. Don't use DB-Library or Embedded SQL to

develop new applications. Remove any dependencies on either DB-Library or Embedded SQL when you're

modifying existing applications. Instead of these APIs, use the SQLClient namespace or an API such as ODBC.

SQL Server 2019 (15.x) doesn't include the DB-Library DLL required to run these applications. To run DB-

Library or Embedded SQL applications, you must have available the DB-Library DLL from SQL Server version

6.5, SQL Server 7.0, or SQL Server 2000 (8.x).

None

Deprecated feature

Replacement

Feature name

The


## syntax
Replaced by the new

and


## syntax
ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

```sql
sys.index_columns
```

```sql
CREATE ENDPOINT
```

```sql
ALTER ENDPOINT
```

```sql
FOR SOAP
```

```sql
sys.soap_endpoints
```

```sql
CREATE
```

```sql
ALTER ENDPOINT
sys.endpoint_webmethods
```

```sql
sys.soap_endpoints
```

```sql
ALTER LOGIN WITH SET
CREDENTIAL
```

```sql
ALTER LOGIN ADD
```

```sql
DROP CREDENTIAL
```

```sql
ALTER LOGIN WITH SET CREDENTIAL
```
