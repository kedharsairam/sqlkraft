---
name: "sys.fn_servershareddrives"
title: "sys.fn_servershareddrives"
category: "system"
description: "Returns the names of shared drives used by the clustered server. Transact-SQL syntax conventions If the current server is a clustered server, If the current server instance is not a clustered server, returns a list of shared drives used by this clustered server. These shared drives belong to the same cluster group as the Microsoft SQL Server resource. Further, the SQL Server resource is dependent "
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "fn_servershareddrives"
---

## Description

Returns the names of shared drives used by the clustered server. Transact-SQL syntax conventions If the current server is a clustered server, If the current server instance is not a clustered server, returns a list of shared drives used by this clustered server. These shared drives belong to the same cluster group as the Microsoft SQL Server resource. Further, the SQL Server resource is dependent on these drives.

## Syntax

`fn_servershareddrives`

## Permissions

Article • 02/28/2023 Applies to: SQL Server Returns the names of shared drives used by the clustered server. Transact-SQL syntax conventions If the current server is a clustered server, returns the drive name of the shared drives. If the current server instance is not a clustered server, returns an empty rowset. returns a list of shared drives used by this clustered server. These shared drives belong to the same cluster group as the Microsoft SQL Server resource. Further, the SQL Server resource is dependent on these drives. This function is helpful in identifying drives available to users. The user must have VIEW SERVER STATE permission for the SQL Server instance. ） Important This SQL Server system function is included for backward compatibility. We recommend that you use instead.

## Examples

### Example 1

`fn_servershareddrives`

### Example 2

```sql
SELECT * FROM fn_servershareddrives();
```
