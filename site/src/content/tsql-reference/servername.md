---
name: "@@SERVERNAME"
title: "@@SERVERNAME"
category: "variables"
description: "Returns the name of the SQL Server instance the client is connected to."
tags: ["tsql", "variables"]
pubDate: 2026-05-29
---

Returns the name of the SQL Server instance the client is connected to.

## Syntax

```sql
@@SERVERNAME
```

## Return Type

**nvarchar(128)**

## Remarks

- For the default instance, **@@SERVERNAME** returns the computer name.
- For a named instance, **@@SERVERNAME** returns the computer name and instance name in the format `computername\instancename`.
- For a failover cluster instance, **@@SERVERNAME** returns the virtual server name.
- Connecting through an alias or via `localhost` may return different values than expected.

## Example

```sql
SELECT @@SERVERNAME AS [Server Name];
```
