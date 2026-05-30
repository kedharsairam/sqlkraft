---
name: "Service Broker Contracts"
title: "Service Broker Contracts"
category: "statements"
description: "Specifies a principal from which the principal executing this query derives its right to revoke"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

AS

revoking_principal

Specifies a principal from which the principal executing this query derives its right to revoke

the permission.

revoking_principal

can be one of the following:

Database user

Database role

Application role

Database user mapped to a Windows login

Database user mapped to a Windows group

Database user mapped to a certificate

Database user mapped to an asymmetric key

Database user not mapped to a server principal

A Service Broker contract is a database-level securable that is contained by the database that is

its parent in the permissions hierarchy. The most specific and limited permissions that can be

revoked on a Service Broker contract are listed in the following table, together with the more

general permissions that include them by implication.

CONTROL

CONTROL

CONTROL

TAKE OWNERSHIP

CONTROL

CONTROL

ALTER

CONTROL

ALTER ANY CONTRACT

REFERENCES

CONTROL

REFERENCES

A cascaded revocation of a permission granted WITH GRANT OPTION will revoke both

GRANT and DENY of that permission.

Expand table

#### Service Broker contract

#### permission

#### Implied by Service Broker contract

#### permission

#### Implied by database

#### permission

#### Service Broker message type

#### permission

#### Implied by Service Broker message

#### type permission

#### Implied by database

#### permission

#### Service Broker remote service

#### binding permission

#### Implied by Service Broker remote

#### service binding permission

#### Implied by database

#### permission
