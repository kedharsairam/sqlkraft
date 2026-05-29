---
name: 'sys.dm_exec_requests'
title: 'sys.dm_exec_requests'
category: 'execution'
description: 'If this option isn''t enabled, these columns return null values. For more information about how'
pubDate: 2026-05-29
---

If this option isn't enabled, these columns return null values. For more information about how

to set this server configuration option, see

Enable common criteria compliance configuration

.

The admin connections on Azure SQL Database see one row per authenticated session. The

sessions that appear in the resultset, don't have any effect on the user quota for sessions. The

non-admin connections only see information related to their database user sessions.

Because of differences in how they're recorded,

might not match

.

.

sys.dm_exec_requests

One-to-zero or one-

to-many

sys.dm_exec_connections

One-to-zero or one-

to-many

sys.dm_tran_session_transactions

One-to-zero or one-

to-many

sys.dm_exec_cursors

(

|

)

One-to-zero or one-

to-many

sys.dm_db_session_space_usage

One-to-one

The following example finds the users that are connected to the server and returns the number

of sessions for each user.

SQL

ﾉ

```sql
last_successful_logon
last_unsuccessful_logon
unsuccessful_logons
```

```sql
sa
```

```sql
open_transaction_count
```

```sql
sys.dm_tran_session_transactions
```

```sql
open_transaction_count
```

```sql
sys.dm_exec_sessions
```

```sql
session_id
```

```sql
sys.dm_exec_sessions
```

```sql
session_id
```

```sql
sys.dm_exec_sessions
```

```sql
session_id
```

```sql
sys.dm_exec_sessions
```

```sql
session_id
```

```sql
0
```

```sql
session_id CROSS
APPLY
OUTER APPLY
```

```sql
sys.dm_exec_sessions
```

```sql
session_id
```
