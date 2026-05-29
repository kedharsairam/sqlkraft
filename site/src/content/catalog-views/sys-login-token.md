---
name: 'sys.login_token'
title: 'sys.login_token'
category: 'security'
description: 'Returns one row for every server principal that is part of the login token.'
tags: ["catalog-view", "security"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server


## Returns one row for every server principal that is part of the login token.

## Description
ID of the principal. This value is unique within server.

Security identifier of the principal. If this is a Windows principal,

=

Windows SID. If the login is mapped to a certificate,

= GUID from the

certificate.

Name of the principal. This value is unique within server.


## Description of principal type. All types are mapped to
. The value can

be one of the following:

Indicates the principal participates in the evaluation of GRANT or DENY


## permissions, or serves as an authenticator.
This value can be one of the following:

ﾉ

Expand table


## Description
sys.user_token (Transact-SQL)

sys.server_principals (Transact-SQL)

sys.database_principals (Transact-SQL)

Principals (Database Engine)

See Also

```sql
SQL LOGIN
WINDOWS LOGIN
WINDOWS GROUP
SERVER ROLE
LOGIN MAPPED TO CERTIFICATE
LOGIN MAPPED TO ASYMMETRIC KEY
CERTIFICATE
ASYMMETRIC KEY
```

```sql
GRANT OR DENY
DENY ONLY
```

```sql
AUTHENTICATOR
```
