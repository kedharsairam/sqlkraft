---
title: "Database options"
topic: "io-fundamentals"
description: "option."
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Deprecated feature

Replacement

Feature name

statement with the

option. To rebuild multiple log

files, when one or more have a new location, use the

option.

in

sp_renamedb

Deprecated feature

Replacement

Feature name

sp_unbindefault

keyword in

and

CREATE_DROP_DEFAULT

sp_bindrule

keyword in

and

CREATE_DROP_RULE

Use

.

and

Use MARS or distributed transactions.

Deprecated feature

Replacement

Feature name

Use MARS or distributed transactions.

{

|

}

sp_resetstatus

option of

option of

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

```sql
sp_attach_db sp_attach_single_file_db
CREATE DATABASE
```

```sql
FOR ATTACH
```

```sql
FOR ATTACH_REBUILD_LOG
```

```sql
sp_attach_db sp_attach_single_file_db sp_certify_removable sp_create_removable sp_detach_db sp_certify_removable sp_create_removable sp_dbremove
DROP DATABASE sp_dbremove sp_renamedb
MODIFY NAME
```

```sql
ALTER DATABASE
```

```sql
CREATE DEFAULT
DROP DEFAULT sp_bindefault
```

`DEFAULT`

```sql
CREATE TABLE
```

```sql
ALTER TABLE
```

```sql
sp_bindefault sp_unbindefault
CREATE RULE
DROP RULE
```

```sql
sp_unbindrule
CHECK
```

```sql
CREATE TABLE
```

```sql
ALTER TABLE
```

```sql
sp_bindrule sp_unbindrule sp_change_users_login
```

```sql
ALTER USER
```

```sql
sp_change_users_login sp_depends sys.dm_sql_referencing_entities
```

```sql
sys.dm_sql_referenced_entities sp_depends sp_getbindtoken
```

`sp_getbindtoken`

`sp_bindsession`

```sql
sp_bindsession sp_resetstatus
ALTER DATABASE SET
```

`ONLINE`

`EMERGENCY`

`TORN_PAGE_DETECTION`

```sql
ALTER
DATABASE
PAGE_VERIFY TORN_PAGE_DETECTION
```

```sql
ALTER
DATABASE
ALTER DATABASE WITH
TORN_PAGE_DETECTION
```
