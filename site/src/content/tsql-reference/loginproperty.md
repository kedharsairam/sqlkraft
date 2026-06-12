---
name: "LOGINPROPERTY"
title: "LOGINPROPERTY"
category: "statements"
description: "Returns information about login policy settings."
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---
## Syntax

```sql
LOGINPROPERTY ( 'login_name' , 'property_name' )
```

## Return Type

sql_variant

## Property Descriptions

| Property | Return Type | Description |
|----------|-------------|-------------|
| BadPasswordCount | int | Number of consecutive failed login attempts. |
| BadPasswordTime | datetime | Time of the last failed login attempt. |
| DaysUntilExpiration | int | Number of days until the password expires. |
| DefaultDatabase | nvarchar | Default database for the login. |
| DefaultLanguage | nvarchar | Default language for the login. |
| HistoryLength | int | Number of password changes tracked. |
| IsExpired | int | Indicates if the password is expired. |
| IsLocked | int | Indicates if the login is locked. |
| LockoutTime | datetime | Time when the login was locked out. |
| PasswordHash | varbinary | Hash of the password. |
| PasswordLastSetTime | datetime | Time when the password was last set. |
| PrincipalID | int | ID of the principal. |
| SID | varbinary | Security identifier of the login. |

## Remarks

Returns information about login policy settings.

## Example

```sql
SELECT LOGINPROPERTY('database_name', 'BadPasswordCount') AS BadPasswordCount;
```
