---
name: "sys.sp_revokelogin"
title: "sp_revokelogin"
category: "general"
description: "Removes the login entries from SQL Server for a Windows user or group created by using Transact-SQL syntax conventions The name of the Windows user or group. , with no default."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: '<ComputerName>\<User>'
---

## Description

Removes the login entries from SQL Server for a Windows user or group created by using Transact-SQL syntax conventions The name of the Windows user or group. , with no default. can be any existing Windows user name or group in the form This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
<ComputerName>\<User>
```

## Remarks

Applies to:

Removes the login entries from SQL Server for a Windows user or group created by using

Transact-SQL syntax conventions

The name of the Windows user or group.

, with no default.

can be any existing Windows user name or group in the form

(success) or

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

## Examples

### Example 1

`sp_revokelogin`

### Example 2

```sql
ADVWORKS\john
```

### Example 3

```sql
ADVWORKS\Admins
```

### Example 4

`sp_revokelogin`

### Example 5

```sql
ADVWORKS\john
```

### Example 6

```sql
ADVWORKS\john
```

### Example 7

```sql
ADVWORKS\Admins
```

### Example 8

```sql
ADVWORKS\Admins
```

### Example 9

```sql
ADVWORKS\john
```

### Example 10

```sql
ADVWORKS\john
```

_(... and 30 more examples)_
