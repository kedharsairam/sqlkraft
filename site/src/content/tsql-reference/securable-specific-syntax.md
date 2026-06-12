---
name: "Securable-specific Syntax"
title: "Securable-specific Syntax"
category: "statements"
description: "The full syntax of the REVOKE statement is complex. The syntax diagram above was simplified"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

The full syntax of the REVOKE statement is complex. The syntax diagram above was simplified

to draw attention to its structure. Complete syntax for revoking permissions on specific

securables is described in the topics listed in

Securable-specific Syntax

later in this topic.

The REVOKE statement can be used to remove granted permissions, and the DENY statement

can be used to prevent a principal from gaining a specific permission through a GRANT.

Granting a permission removes DENY or REVOKE of that permission on the specified securable.

If the same permission is denied at a higher scope that contains the securable, the DENY takes

precedence. However, revoking the granted permission at a higher scope does not take

precedence.

The sp_helprotect system stored procedure reports permissions on a database-level securable

The REVOKE statement will fail if CASCADE is not specified when you are revoking a permission

from a principal that was granted that permission with GRANT OPTION specified.

Principals with CONTROL permission on a securable can revoke permission on that securable.

Object owners can revoke permissions on the objects they own.

Grantees of CONTROL SERVER permission, such as members of the sysadmin fixed server role,

can revoke any permission on any securable in the server. Grantees of CONTROL permission on

a database, such as members of the db_owner fixed database role, can revoke any permission

on any securable in the database. Grantees of CONTROL permission on a schema can revoke

any permission on any object within the schema.

The following table lists the securables and the topics that describe the securable-specific

## syntax.

Ｕ

Caution

A table-level DENY does not take precedence over a column-level GRANT. This

inconsistency in the permissions hierarchy has been preserved for backward compatibility.

It will be removed in a future release.

Expand table

#### Securable

#### Topic

Application Role

REVOKE Database Principal Permissions (Transact-SQL)

Assembly

REVOKE Assembly Permissions (Transact-SQL)

Asymmetric Key

REVOKE Asymmetric Key Permissions (Transact-SQL)

Availability Group

REVOKE Availability Group Permissions (Transact-SQL)

Certificate

REVOKE Certificate Permissions (Transact-SQL)

Contract

REVOKE Service Broker Permissions (Transact-SQL)

Database

REVOKE Database Permissions (Transact-SQL)

Endpoint

REVOKE Endpoint Permissions (Transact-SQL)

Database Scoped Credential

REVOKE Database Scoped Credential (Transact-SQL)

Full-text Catalog

REVOKE Full-Text Permissions (Transact-SQL)

Full-Text Stoplist

REVOKE Full-Text Permissions (Transact-SQL)

Function

REVOKE Object Permissions (Transact-SQL)

Login

REVOKE Server Principal Permissions (Transact-SQL)

Message Type

REVOKE Service Broker Permissions (Transact-SQL)

Object

REVOKE Object Permissions (Transact-SQL)

Queue

REVOKE Object Permissions (Transact-SQL)

Remote Service Binding

REVOKE Service Broker Permissions (Transact-SQL)

Role

REVOKE Database Principal Permissions (Transact-SQL)

Route

REVOKE Service Broker Permissions (Transact-SQL)

Schema

REVOKE Schema Permissions (Transact-SQL)

Search Property List

REVOKE Search Property List Permissions (Transact-SQL)

Server

REVOKE Server Permissions (Transact-SQL)

Service

REVOKE Service Broker Permissions (Transact-SQL)

Stored Procedure

REVOKE Object Permissions (Transact-SQL)

Symmetric Key

REVOKE Symmetric Key Permissions (Transact-SQL)

Synonym

REVOKE Object Permissions (Transact-SQL)

#### Securable

#### Topic
