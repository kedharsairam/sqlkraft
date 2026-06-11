---
name: "sys.security_predicates"
title: "sys.security_predicates"
category: "security"
description: "SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns a row for each security predicate in the database."
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
syntax: "[dbo].[fn_securitypredicate]([wing], [startTime], [endTime])"
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns a row for each security predicate in the database. ID of the security policy that contains this predicate. Predicate ID within this security policy. ID of the object on which the security predicate is bound. Fully qualified name of the function that will be used as a security predicate, including the arguments. Note that the

## Syntax

```sql
[dbo].[fn_securitypredicate]([wing], [startTime], [endTime])
```
