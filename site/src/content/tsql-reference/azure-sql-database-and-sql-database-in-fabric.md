---
name: "Azure SQL Database and SQL database in Fabric"
title: "Azure SQL Database and SQL database in Fabric"
category: "operators"
description: "2025 (17.x)"
tags: ["tsql","operators"]
pubDate: "2026-05-29"
---

### Supplemental

### Terms of Use for Microsoft Azure Previews

### Deprecation notice

### Migrating from earlier vector index versions

## Regional availability

2025 (17.x)

SQL database in Microsoft

Fabric

Create an approximate index on a vector column to improve performances of nearest

neighbors search. To learn more about how vector indexing and vector search works, and the

differences between exact and approximate search, refer to

Vector search and vector indexes in

the SQL Database Engine.

The feature is in preview. Check

Limitations and considerations

before proceeding.

This feature is being deployed across Azure SQL Database and SQL database in Microsoft

Fabric. During the rollout, availability and behavior might vary by region and by index version.

If a feature or syntax isn't available, it becomes available automatically as deployment

completes. For current regional availability status, see

Feature availability by region.

In SQL Server 2025 this function is in preview and is subject to change. In order to use this

feature, you must enable the

database scoped configuration.

７

Note

As a preview feature, the technology presented in this article is subject to.

２

Warning

: Vector indexes created using an earlier data structure are supported

in the current release but will be retired in a future version. To ensure future compatibility

and access to the latest vector search capabilities, migrate existing vector indexes using

the steps in the

section.

2025 Preview feature

### vector

`PREVIEW_FEATURES`
