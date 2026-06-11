---
name: "sys.user_token"
title: "sys.user_token"
category: "security"
description: "SQL database in Microsoft Fabric Returns one row for every database principal that is part of the user token in SQL Server."
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SQL USER
  WINDOWS LOGIN
  WINDOWS GROUP
  ROLE
  APPLICATION ROLE
  DATABASE ROLE
  USER MAPPED TO CERTIFICATE
  USER MAPPED TO ASYMMETRIC KEY
  CERTIFICATE
  ASYMMETRIC KEY
---

## Description

SQL database in Microsoft Fabric Returns one row for every database principal that is part of the user token in SQL Server. ID of the principal. The value is unique within database. Security identifier of the principal if the principal is defined external to the database. For example, this can be a SQL Server login, Windows login, Windows Group login, or a login mapped to a certificate, otherwise, this

## Syntax

```sql
SQL USER
WINDOWS LOGIN
WINDOWS GROUP
ROLE
APPLICATION ROLE
DATABASE ROLE
USER MAPPED TO CERTIFICATE
USER MAPPED TO ASYMMETRIC KEY
CERTIFICATE
ASYMMETRIC KEY
```
