---
name: "Supported objects"
title: "Supported objects"
category: "statements"
description: "Starting with SQL Server 2019 (15.x),"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Starting with SQL Server 2019 (15.x),

automatically captures the stats blobs

for columnstore indexes, so no manual steps are required.

creates a

schema-only copy of a database that includes all the elements necessary to troubleshoot query

performance issues without copying the data. In previous versions of SQL Server, the command

didn't copy the statistics necessary to accurately troubleshoot columnstore index queries and

manual steps were required to capture this information.

For information related to data security on cloned databases, see

Understanding data security

in cloned databases

.

uses an internal database snapshot of the source database for the

transactional consistency that is needed to perform the copy. Using this snapshot prevents

blocking and concurrency problems when these commands are executed. If a snapshot can't

be created,

will fail.

Database level locks are held during following steps of the copy process:

Validate the source database

Get shared (S) lock for the source database

Create snapshot of the source database

Create a clone database (an empty database inherited from the

database)

Get exclusive (X) lock for the clone database

Copy the metadata to the clone database

Release all database locks

As soon as the command has finished running, the internal snapshot is dropped.

and

options are turned off on a cloned database.

Only the following objects can be cloned in the destination database. Encrypted objects get

cloned but aren't usable in the clone database. Any objects that aren't listed in the following

you run the

command. Starting with SQL Server 2019 (15.x), the

manual steps outlined in the article above will no longer be required as the

command gathers this information automatically.

section aren't supported in the clone:

APPLICATION ROLE

AVAILABILITY GROUP

COLUMNSTORE INDEX

CDB

CDC

Change Tracking

CLR

DATABASE PROPERTIES

DEFAULT

FILES AND FILEGROUPS

Full text

FUNCTION

INDEX

LOGIN

PARTITION FUNCTION

PARTITION SCHEME

PROCEDURE

QUERY STORE

ROLE

RULE

SCHEMA

SEQUENCE

SPATIAL INDEX

STATISTICS

SYNONYM

TABLE

MEMORY OPTIMIZED TABLES

FILESTREAM AND FILETABLE OBJECTS

TRIGGER

TYPE

UPGRADED DB

USER

VIEW

XML INDEX

XML SCHEMA COLLECTION

Starting in SQL Server 2014 (12.x) Service Pack 2 CU 3.

Starting in SQL Server 2016 (13.x) Service Pack 1.

6, 7, 8

1, 2

3

4

2, 5

9

2

1, 2

1

2

### sysadmin

```sql
DBCC CLONEDATABASE
```

```sql
DBCC CLONEDATABASE
```

```sql
DBCC CLONEDATABASE
```

```sql
DBCC CLONEDATABASE
```

```sql
model
```

```sql
TRUSTWORTHY
```

```sql
DB_CHAINING
```

```sql
DBCC CLONEDATABASE
```

```sql
DBCC
CLONEDATABASE
```
