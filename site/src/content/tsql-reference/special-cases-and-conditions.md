---
name: "Special Cases and Conditions"
title: "Special Cases and Conditions"
category: "operators"
description: ""
tags: ["tsql","operators"]
pubDate: "2026-05-29"
---

If the target entity is not a database and the entity is being transferred to a new owner, all

## permissions on the target will be dropped.

Also, note the following:

The following table lists special cases, exceptions, and conditions that apply to altering

authorization.

OBJECT

Cannot change ownership of triggers, constraints, rules, defaults, statistics,

system objects, queues, indexed views, or tables with indexed views.

SCHEMA

When ownership is transferred, permissions on schema-contained objects that

do not have explicit owners will be dropped. Cannot change the owner of sys,

dbo, or information_schema.

TYPE

Cannot change ownership of a TYPE that belongs to sys or information_schema.

CONTRACT, MESSAGE

TYPE, or SERVICE

Cannot change ownership of system entities.

SYMMETRIC KEY

Cannot change ownership of global temporary keys.

CERTIFICATE or

ASYMMETRIC KEY

Cannot transfer ownership of these entities to a role or group.

ENDPOINT

The principal must be a login.

７

Note

Schemas aren't equivalent to database users. Use

to identify any

differences between database users and schemas.

）

Important

The only reliable way to find the owner of an object is to query the

catalog

view. The only reliable way to find the owner of a type is to use the TYPEPROPERTY

function.

Expand table

### Requirements for the new owner:

### Requirements for the person executing the ALTER AUTHORIZATION statement:

### sysadmin

### Requirements for the new owner:

### Requirements for the person executing the ALTER AUTHORIZATION statement:
