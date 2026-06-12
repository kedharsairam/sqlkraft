---
name: "Returns"
title: "Returns"
category: "statements"
description: "Returns the number of passwords tracked for the login, using the password-"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## Description

## Returns the number of passwords tracked for the login, using the password-

policy enforcement mechanism. 0 if the password policy isn't enforced.

Resuming password policy enforcement restarts at 1.

Indicates whether the login's password has expired.

Indicates whether the login is locked.

Indicates whether the login must change its password the next time it

connects.

## Returns the date when the SQL Server login was locked out because it had

exceeded the permitted number of failed login attempts.

## Returns the hash of the password.

## Returns the date when the current password was set.

## Returns the algorithm used to hash the password. In SQL Server 2022 (16.x)

and earlier versions, the stored password information is calculated using SHA-

512 of the salted password. Starting with SQL Server 2025 (17.x), an iterated

hash algorithm, RFC2898 (PBKDF) is used. The first byte of the hash indicates

the version:

for version 2 (SQL Server 2022 (16.x) and earlier versions)

and

for version 3 (SQL Server 2025 (17.x) and later versions).

Data type depends on requested value.

,

, and

are of type.

1 if the login is in the specified state.

0 if the login isn't in the specified state.

and

are of type.

,

,

are of type.

is of type.

NULL if the login isn't a valid SQL Server login.

is of type.

0 if the login is expired or if it will expire on the day when queried.

### PasswordHashAlgorithm

### BadPasswordCount

### badpasswordcount

### PasswordHash,

### PasswordHashAlgorithm

### PasswordLastSetTime

```sql
0x02
```

```sql
0x03
```
