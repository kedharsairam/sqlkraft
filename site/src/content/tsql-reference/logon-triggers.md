---
name: 'Logon triggers'
title: 'Logon triggers'
category: 'statements'
description: 'For more information about DDL triggers, see'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Disable a logon trigger

For more information about DDL triggers, see

DDL triggers

.

DDL triggers don't fire in response to events that affect local or global temporary tables and

stored procedures.

Unlike DML triggers, DDL triggers aren't scoped to schemas. So, you can't use functions such

as

,

,

, and

for querying metadata

about DDL triggers. Use the catalog views instead. For more information, see

Get Information

About DDL Triggers

.

Logon triggers carry out stored procedures in response to a

event. This event happens

when a user session is established with an instance of SQL Server. Logon triggers fire after the

authentication phase of logging in finishes, but before the user session is established. So, all

messages originating inside the trigger that would typically reach the user, such as error

messages and messages from the

statement, are diverted to the SQL Server error log.

For more information, see

Logon triggers

.

Logon triggers don't fire if authentication fails.

Distributed transactions aren't supported in a logon trigger. Error 3969 returns when a logon

trigger that contains a distributed transaction fire.

A logon trigger can effectively prevent successful connections to the Database Engine for all

users, including members of the

fixed server role. When a logon trigger is preventing

connections, members of the

fixed server role can connect by using the dedicated

administrator connection, or by starting the Database Engine in minimal configuration mode (

). For more information, see

Database Engine Service startup options

.

stored procedures fire a DDL trigger that's created on a

event.

７

Note

Server-scoped DDL triggers appear in the SQL Server Management Studio Object Explorer

in the

folder. This folder is located under the

folder. Database-

scoped DDL triggers appear in the

folder. This folder is located under

the

folder of the corresponding database.

### Indirect recursion

### Direct recursion

```sql
OBJECT_ID
```

```sql
OBJECT_NAME
```

```sql
OBJECTPROPERTY
```

```sql
OBJECTPROPERTYEX
```

```sql
LOGON
```

```sql
PRINT
```

```sql
-
f
```

```sql
CREATE_TYPE
```
