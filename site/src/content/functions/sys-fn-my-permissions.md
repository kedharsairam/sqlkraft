---
name: "sys.fn_my_permissions"
title: "sys.fn_my_permissions"
category: "system"
description: "Returns a list of the permissions effectively granted to the principal on a securable. A related The name of the securable. If the securable is the server or a database, this value should be set is a scalar expression of type The name of the class of securable for which permissions are listed. This argument must be one of the followin"
tags: ["system","function"]
pubDate: 2026-05-29
syntax: "REMOTE SERVICE BINDING"
---

## Description

Analytics Platform System (PDW) Returns a list of the permissions effectively granted to the principal on a securable. A related The name of the securable. If the securable is the server or a database, this value should be set is a scalar expression of type The name of the class of securable for which permissions are listed. This argument must be one of the following values:

## Syntax

```sql
REMOTE SERVICE BINDING
```

## Permissions

The function isn't supported in Azure Synapse Analytics dedicated SQL pools. Requires membership in the role. The following example returns a list of the effective permissions of the caller on the server. SQL The following example returns a list of the effective permissions of the caller on the database. SQL The following example returns a list of the effective permissions of the caller on the view in the schema of the database. SQL
