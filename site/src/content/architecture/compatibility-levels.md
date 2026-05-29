---
title: "Compatibility levels"
topic: "query-processing"
description: "Replace remote servers by using linked servers."
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Deprecated feature

Replacement

Feature name

Feature

ID

Replace remote servers by using linked servers.

can only be used with the local option.

70

69

71

72

73

@@remserver

Replace remote servers by using linked servers.

None

None

Replace remote servers by using linked servers.

110

Deprecated feature

Replacement

Feature name

Feature

ID

for

,

, and

statements

keyword

109

HOLDLOCK table hint without parenthesis.

Use HOLDLOCK with

parenthesis.

HOLDLOCK table hint without

parenthesis

167

The following SQL Server Database Engine features are supported in the next version of SQL Server. The specific version of

SQL Server hasn't been determined.

Deprecated feature

Replacement

Feature name

BACKUP { DATABASE | LOG } TO TAPE

BACKUP { DATABASE | LOG } TO

device_that_is_a_tape

BACKUP { DATABASE | LOG } TO DISK

BACKUP { DATABASE | LOG } TO

device_that_is_a_disk

BACKUP DATABASE or LOG TO

TAPE

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

```sql
sp_addremotelogin
sp_addserver
sp_dropremotelogin
sp_helpremotelogin
sp_remoteoption
```

```sql
sp_addserver
```

```sql
sp_addremotelogin
sp_addserver
sp_dropremotelogin
sp_helpremotelogin
sp_remoteoption
```

```sql
SET
REMOTE_PROC_TRANSACTIONS
```

```sql
SET
REMOTE_PROC_TRANSACTIONS
```

```sql
SET ROWCOUNT
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
TOP
```

```sql
SET ROWCOUNT
```

```sql
sp_addumpdevice 'tape'
sp_addumpdevice 'disk'
ADDING TAPE DEVICE
sp_helpdevice
sys.backup_devices
sp_helpdevice
```
