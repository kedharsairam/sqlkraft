---
title: "Set password policy"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server 2022 (16.x) and later versions on Linux

  This article describes how to set up and manage password policies for SQL Server logins on Linux.

  Custom password policies are availab
tags:
  - "linux-operations"
  - "set-password-policy"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2022 (16.x) and later versions on Linux

This article describes how to set up and manage password policies for SQL Server logins on Linux.

Custom password policies are available starting in SQL Server 2022 (16.x) Cumulative Update (CU)

23, and SQL Server 2025 (17.x).

Password policies enforce rules for complexity, expiration, and changes, which help to keep SQL

Server logins secure.

Set the following configuration parameters in the

file to enforce a custom password

policy:

Description

Sets the minimum number of characters required for a password.

Passwords can be up to 128 characters long.

Sets the number of previous passwords that the system

remembers.

Sets the minimum duration a user must wait before changing their

password again.

Sets the maximum duration a password can be used before it must

be changed.

７

Note

Password policies are also available on Windows. For more information, see

.

ﾉ

Expand table

７

Note

```cmd
mssql.conf
passwordpolicy.passwordminimumlength
passwordpolicy.passwordhistorylength
passwordpolicy.passwordminimumage
passwordpolicy.passwordmaximumage
```
