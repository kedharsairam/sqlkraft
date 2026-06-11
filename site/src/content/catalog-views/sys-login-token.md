---
name: "sys.login_token"
title: "sys.login_token"
category: "security"
description: "Returns one row for every server principal that is part of the login token."
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SQL LOGIN
  WINDOWS LOGIN
  WINDOWS GROUP
  SERVER ROLE
  LOGIN MAPPED TO CERTIFICATE
  LOGIN MAPPED TO ASYMMETRIC KEY
  CERTIFICATE
  ASYMMETRIC KEY
---

## Description

Returns one row for every server principal that is part of the login token. ID of the principal. This value is unique within server. Security identifier of the principal. If this is a Windows principal, Windows SID. If the login is mapped to a certificate, Name of the principal. This value is unique within server. Description of principal type. All types are mapped to Indicates the principal participates in the evaluation of GRANT or DENY

## Syntax

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
