---
title: "Customize the lock time-out"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

Any snapshot transaction that's active when the

statement is executed receives

an error if it attempts to reference the

table after the

statement is executed.

transactions using row versioning aren't affected.

When an instance of the Database Engine can't grant a lock to a transaction because another

transaction already owns a conflicting lock on the resource, the first transaction becomes blocked

waiting for the existing lock to be released.

By default, there's no timeout period for lock waits, therefore a transaction could potentially get

blocked indefinitely. You can configure some parts of the locking behavior.

The

setting allows an application to set a maximum time that a statement waits on

a blocked resource. When a statement has waited longer than the

setting, the

blocked statement is canceled automatically, and error message 1222 (

) is returned. Any transaction containing the statement, however, isn't rolled

back. Therefore, the application must have an error handler that can trap error message 1222. If

７

Note

operations might cause changes to target table metadata (for example,

when disabling constraint checks). When this happens, concurrent

isolation

transactions accessing bulk inserted tables fail.

７

Note

Use the

dynamic management view to determine whether a task is

being blocked and what is blocking it. For more information and examples, see.

```sql
ALTER INDEX
```

`HumanResources.Employee`

```sql
ALTER INDEX
```

```sql
READ COMMITTED
```

`LOCK_TIMEOUT`

`LOCK_TIMEOUT`

```sql
Lock request time-out period exceeded
```

```sql
USE
AdventureWorks2022;
GO
ALTER
INDEX
AK_Employee_LoginID
ON
HumanResources.Employee
REBUILD
;
GO
```

```sql
BULK INSERT
```

`SNAPSHOT`

`sys.dm_os_waiting_tasks`
