---
name: "Database User Permissions"
title: "Database User Permissions"
category: "statements"
description: "Database_user_mapped_to_Windows_User"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Database_user_mapped_to_Windows_User

: SQL Server 2008 (10.0.x) and later

Specifies a database user mapped to a Windows user.

Database_user_mapped_to_Windows_Group

: SQL Server 2008 (10.0.x) and later

Specifies a database user mapped to a Windows group.

Database_user_mapped_to_certificate

: SQL Server 2008 (10.0.x) and later

Specifies a database user mapped to a certificate.

Database_user_mapped_to_asymmetric_key

: SQL Server 2008 (10.0.x) and later

Specifies a database user mapped to an asymmetric key.

Database_user_with_no_login

Specifies a database user with no corresponding server-level principal.

A database user is a database-level securable contained by the database that is its parent in

the permissions hierarchy. The most specific and limited permissions that can be revoked on a

database user are listed in the following table, together with the more general permissions that

include them by implication.

CONTROL

CONTROL

CONTROL

IMPERSONATE

CONTROL

CONTROL

ALTER

CONTROL

ALTER ANY USER

VIEW DEFINITION

CONTROL

VIEW DEFINITION

Expand table

#### Database role permission

#### Implied by database role permission

#### Implied by database permission

#### Application role

#### permission

#### Implied by application role

#### permission

#### Implied by database

#### permission

### db_owner
