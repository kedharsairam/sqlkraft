---
name: "Catalog view"
title: "Catalog view"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Because a collation rule is set at the database level, the following logic applies to keep the

database collation rule and the RFC rules consistent. (The described rule could potentially be

more restrictive than the RFC rules, for example if the database is set to use a case-sensitive

collation.)

1. Check if the URL and credential match using the RFC, which means:

Check the scheme and host using a case-insensitive collation

(

)

Check all other segments of the URL are compared in a case-sensitive collation

(

)

2. Check that the URL and credential match using the database collation rules (and without

doing any URL encoding).

To use the

managed identity

of the Arc/VM host as a database level credential in SQL Server

2025 (17.x), you must enable the option by using

with a user that is

granted the

ALTER SETTINGS server-level permission

.

Views created with

that reference an external model (such as a

statement using

) can't be dropped, and the Database Engine raises an

error. To remove dependencies referencing an external model, you must first modify or drop

the view definition.

You can view external model metadata by querying the

sys.external_models

catalog view. You

must have access to a model to view its metadata.

`Latin1_General_100_CI_AS_KS_WS_SC`

`Latin1_General_100_BIN2`

`sp_configure`

`SCHEMABINDING`

`SELECT`

`AI_GENERATE_EMBEDDINGS`

```sql
EXECUTE sp_configure
'allow server scoped db credentials'
, 1;
RECONFIGURE
WITH
OVERRIDE;
```
