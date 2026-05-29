---
title: 'Server Configuration Options'
topic: 'io-fundamentals'
description: 'A master key must exist and password must be correct.'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Deprecated feature

Replacement

Feature name

sp_dropapprole

sp_droplogin

sp_droprole

or

A master key must exist and password must be correct.

sp_revokelogin

USER_ID

DATABASE_PRINCIPAL_ID

USER_ID

These stored procedures return information that was correct in

SQL Server 2000 (8.x). The output doesn't reflect changes to

the permissions hierarchy implemented in SQL Server 2008.

For more information, see


## Permissions of Fixed Server Roles
.

,

, and

-specific permissions.

ALL Permission


## PERMISSIONS intrinsic function
Query

instead.


## PERMISSIONS
SETUSER

SETUSER

RC4 and

encryption

algorithms

Use another algorithm such as AES.

algorithm

```sql
sp_addapprole
sp_dropapprole
CREATE APPLICATION ROLE
DROP APPLICATION ROLE
sp_addapprole
```

```sql
sp_addlogin
sp_droplogin
CREATE LOGIN
DROP LOGIN
sp_addlogin
```

```sql
sp_adduser
sp_dropuser
CREATE USER
DROP USER
sp_adduser
sp_dropuser
sp_grantdbaccess
sp_revokedbaccess
CREATE USER
DROP USER
sp_grantdbaccess
sp_revokedbaccess
sp_addrole
sp_droprole
CREATE ROLE
DROP ROLE
sp_addrole
```

```sql
sp_approlepassword
sp_password
ALTER APPLICATION ROLE
ALTER LOGIN
sp_approlepassword
sp_password
sp_changedbowner
ALTER AUTHORIZATION
sp_changedbowner
sp_changeobjectowner
ALTER SCHEMA
```

```sql
ALTER AUTHORIZATION
sp_changeobjectowner
sp_control_dbmasterkey_password
```

```sql
sp_control_dbmasterkey_password
sp_defaultdb
sp_defaultlanguage
ALTER LOGIN
sp_defaultdb
sp_defaultlanguage
sp_denylogin
sp_grantlogin
sp_revokelogin
ALTER LOGIN DISABLE
CREATE LOGIN
DROP LOGIN
sp_denylogin
sp_grantlogin
```

```sql
sp_srvrolepermission
sp_dbfixedrolepermission
```

```sql
sp_srvrolepermission
sp_dbfixedrolepermission
GRANT ALL
DENY ALL
REVOKE ALL
GRANT
```

```sql
DENY
```

```sql
REVOKE
```

```sql
sys.fn_my_permissions
```

```sql
EXECUTE AS
```

```sql
DESX
```

```sql
DESX
```
