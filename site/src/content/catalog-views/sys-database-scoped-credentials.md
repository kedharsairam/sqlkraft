---
name: 'sys.database_scoped_credentials'
title: 'sys.database_scoped_credentials (Transact-'
category: 'objects'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

SQL)

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

SQL database in Microsoft Fabric


## Returns one row for each database scoped credential in the database.

## Description
Name of the database scoped credential. Is unique in the

database.

ID of the database scoped credential. Is unique in the database.

ID of the database principal who owns the key.

Name of the identity to use. It does not have to be unique.

Time at which the database scoped credential was created.

Time at which the database scoped credential was last modified.

Type of database scoped credential. Returns

for database

scoped credentials.

ID of the object that the database scoped credential is mapped

to. Returns

for database scoped credentials

Requires

permission on the database.

Credentials (Database Engine)

CREATE DATABASE SCOPED CREDENTIAL (Transact-SQL)

ALTER DATABASE SCOPED CREDENTIAL (Transact-SQL)

DROP DATABASE SCOPED CREDENTIAL (Transact-SQL)

CREATE CREDENTIAL (Transact-SQL)

sys.credentials (Transact-SQL)

ﾉ

Expand table

Related content

Last updated on 11/18/2025

```sql
name
```

```sql
credential_id
```

```sql
principal_id
```

```sql
credential_identity
```

```sql
create_date
```

```sql
modify_date
```

```sql
target_type
```

```sql
NULL
```

```sql
target_id
```

```sql
0
```

```sql
CONTROL
```
