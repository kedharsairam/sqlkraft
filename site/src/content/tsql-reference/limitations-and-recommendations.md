---
name: "Limitations and Recommendations"
title: "Limitations and Recommendations"
category: "operators"
description: "Removes the specified availability group and all of its replicas. If a server instance that hosts"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

Article

•

09/03/2024

Applies to:

SQL Server

Removes the specified availability group and all of its replicas. If a server instance that hosts

one of the availability replicas is offline when you delete an availability group, after coming

online, the server instance will drop the local availability replica. Dropping an availability group

also deletes the associated availability group listener, if any.

For information about alternative ways to drop an availability group, see

Remove an Availability

Group (SQL Server)

.

Transact-SQL syntax conventions

## syntaxsql

group_name

Specifies the name of the availability group to be dropped.

Executing

requires that the Always On Availability Groups

feature is enabled on the server instance. For more information, see

Enable and Disable

Always On Availability Groups (SQL Server)

.

）

Important

If possible, remove the availability group only while connected to the server instance that

hosts the primary replica. When the availability group is dropped from the primary replica,

changes are allowed in the former primary databases (without high availability protection).

Deleting an availability group from a secondary replica leaves the primary replica in the

state, and changes are not allowed on the databases.

### DROP AVAILABILITY GROUP

### DROP AVAILABILITY GROUP

### OFFLINE

### DROP AVAILABILITY GROUP

### RESTORING

### ALTER AVAILABILITY GROUP

### CONTROL

### AVAILABILITY GROUP

### ALTER ANY AVAILABILITY GROUP

### CONTROL

### SERVER

### CONTROL SERVER

### CONTROL

```sql
DROP
AVAILABILITY
GROUP
group_name
[ ; ]
```
