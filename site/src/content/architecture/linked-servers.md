---
title: "Linked servers"
topic: "query-processing"
description: "Always On availability groups"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Deprecated feature

Replacement

Feature name

Use

Use

argument of

xp_loginconfig

Deprecated

feature

Replacement

Feature name

database mirroring

Always On availability groups

If your edition of SQL Server doesn't support Always On availability groups, use log

shipping.

DATABASE_MIRRORING

Deprecated feature

Replacement

Feature name

,

, or

## syntax without parentheses

around the options.

Rewrite the statement to use the current

## syntax.

INDEX_OPTION

Deprecated feature

Replacement

Feature name

option 'allow

updates'

System tables are no longer updatable. Setting has no effect.

'allow

updates'

options:

'locks'

'open objects'

'set working set size'

Now automatically configured. Setting has no effect.

'locks'

'open

objects'

'set

working set size'

option 'priority

boost'

System tables are no longer updatable. Setting has no effect. Use the

Windows start /high. program.exe option instead.

'priority

boost'

option 'remote

proc trans'

System tables are no longer updatable. Setting has no effect.

'remote

proc trans'

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

```sql
xp_grantlogin xp_revokelogin xp_loginConfig
```

```sql
CREATE LOGIN
```

```sql
DROP LOGIN IsIntegratedSecurityOnly
```

```sql
SERVERPROPERTY xp_grantlogin xp_revokelogin
```

```sql
sp_indexoption
ALTER INDEX sp_indexoption
CREATE TABLE
```

```sql
ALTER TABLE
```

```sql
CREATE INDEX
```

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`
