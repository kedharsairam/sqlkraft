---
name: 'sys.server_file_audits'
title: 'sys.server_file_audits'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Managed Instance

Contains extended information about the file audit type in a SQL Server audit on a server

instance. For more information, see

SQL Server Audit (Database Engine)

.


## Description
No

ID of the audit.

No

Name of the audit.

Yes

GUID of the audit.

No

UTC date when the file audit was created.

No

UTC date when the file audit was last modified.

Yes

ID of the owner of the audit as registered on the server.

No

Audit type:

-

= Windows Security event log

-

= Windows Application event log

-

= File on file system

Yes

Audit type description.

Yes

On failure condition:

-

= Continue

-

= Shut down server instance

-

= Fail operation

Yes

On failure to write an action entry:

-

-

-

Yes

-

= Disabled

-

= Enabled

ﾉ

Expand table

```sql
audit_id
```

```sql
name
```

```sql
audit_guid
```

```sql
create_date
```

```sql
modify_date
```

```sql
principal_id
```

```sql
type
```

```sql
SL
```

```sql
AL
```

```sql
FL
```

```sql
type_desc
```

```sql
on_failure
```

```sql
0
```

```sql
1
```

```sql
2
```

```sql
on_failure_desc
```

```sql
CONTINUE
```

```sql
SHUTDOWN SERVER INSTANCE
```

```sql
FAIL OPERATION
is_state_enabled
```

```sql
0
```

```sql
1
```
