---
name: 'sys.fn_hadr_backup_is_preferred_replica'
title: 'sys.fn_hadr_backup_is_preferred_replica'
category: 'system'
description: 'Used to determine if the current replica is the preferred backup replica.'
tags: ["function"]
pubDate: 2026-05-29
---

at the same data to determine which job should run, so only one of the scheduled jobs actually

proceeds to the backup stage. Sample code could be similar to the following.

SQL

The following example returns 1 if the current database is the preferred backup replica.

SQL

Configure backups on secondary replicas of an Always On availability group

Always On Availability Groups Functions (Transact-SQL)

What is an Always On availability group?

CREATE AVAILABILITY GROUP (Transact-SQL)

ALTER AVAILABILITY GROUP (Transact-SQL)

Offload supported backups to secondary replicas of an availability group

Always On Availability Groups Catalog Views (Transact-SQL)

Related content

```sql
IF sys.fn_hadr_backup_is_preferred_replica(@dbname) <> 1
BEGIN
-- If this is not the preferred replica, exit (probably without error).
SELECT
'This is not the preferred replica, exiting with success'
;
END
-- If this is the preferred replica, continue to do the backup.
/* actual backup command goes here */
```

```sql
SELECT
sys.fn_hadr_backup_is_preferred_replica(
'TestDB'
);
GO
```
