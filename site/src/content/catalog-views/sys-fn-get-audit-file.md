---
name: 'sys.fn_get_audit_file'
title: 'sys.fn_get_audit_file'
category: 'objects'
description: 'Suggested maximum time, in milliseconds, to wait'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
Yes

Suggested maximum time, in milliseconds, to wait

before writing to disk. If

, the audit guarantees a write

before the event can continue.

Yes

Predicate expression that is applied to the event.

Yes

Maximum size, in megabytes, of the audit:

-

= Unlimited/Not applicable to the type of audit

selected.

Yes

Maximum number of files to use with the rollover

option.

Yes

Maximum number of files to use without the rollover

option.

Yes

Amount of disk space to reserve per file.

Yes

Path to where audit is located. File path for file audit,

application log path for application log audit.

Yes

Base name for the log file supplied in the

. An incremental number is added to the

base_log_name file as a suffix to create the log file

name.

Yes

Lifetime in days of the audit log file.

-

= Unlimited.

: Azure SQL Database and Azure SQL

Managed Instance.

Principals with the

or

permission can access this

catalog view. In addition, the principal can't be denied

permission.

The visibility of the metadata in catalog views is limited to securables that a user either owns, or

on which the user was granted some permission. For more information, see

Metadata visibility

configuration

.

CREATE SERVER AUDIT

ALTER SERVER AUDIT

DROP SERVER AUDIT

CREATE SERVER AUDIT SPECIFICATION

ALTER SERVER AUDIT SPECIFICATION

DROP SERVER AUDIT SPECIFICATION

CREATE DATABASE AUDIT SPECIFICATION

ALTER DATABASE AUDIT SPECIFICATION

DROP DATABASE AUDIT SPECIFICATION

ALTER AUTHORIZATION

Create a Server Audit and Server Audit Specification

sys.fn_get_audit_file (Transact-SQL)

sys.server_audits (Transact-SQL)

sys.server_file_audits (Transact-SQL)

sys.server_audit_specifications (Transact-SQL)

sys.database_audit_specifications (Transact-SQL)

sys.database_audit_specification_details (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_actions (Transact-SQL)

sys.dm_audit_class_type_map (Transact-SQL)

Last updated on 04/24/2026

Related content

```sql
queue_delay
```

```sql
0
```

```sql
predicate
```

```sql
max_file_size
```

```sql
0
```

```sql
max_rollover_files
```

```sql
max_files
```

```sql
reserve_disk_space
```

```sql
log_file_path
```

```sql
log_file_name
```

```sql
CREATE AUDIT
DDL
```

```sql
retention_days
```

```sql
0
```

```sql
ALTER ANY SERVER AUDIT
```

```sql
VIEW ANY DEFINITION
```

```sql
VIEW ANY DEFINITION
```
