---
name: "sys.dm_os_stacks"
title: "sys.dm_os_stacks"
category: "os"
description: "This dynamic management view is used internally by SQL Server to do the following: Keep track of debug data such as outstanding allocations. Assume or validate logic that is used by SQL Server components in places where the component assumes that a certain call has been made. Unique address for this stack allocation. Is not nullable. Each line represents a function"
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: "##MS_ServerStateReader##"
---

## Description

This dynamic management view is used internally by SQL Server to do the following: Keep track of debug data such as outstanding allocations. Assume or validate logic that is used by SQL Server components in places where the component assumes that a certain call has been made. Unique address for this stack allocation. Is not nullable.

## Syntax

```sql
##MS_ServerStateReader##
```

## Permissions

This dynamic management view is used internally by SQL Server to do the following: Keep track of debug data such as outstanding allocations. Assume or validate logic that is used by SQL Server components in places where the component assumes that a certain call has been made. Unique address for this stack allocation. Is not nullable. Each line represents a function call that, when sorted in ascending order by frame index for a particular , returns the full call stack. Is not nullable. Address of the function call. Is not nullable. requires that the symbols of the server and other components be present on the server to display the information correctly. On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. Requires VIEW SERVER PERFORMANCE STATE permission on the server. ﾉ
