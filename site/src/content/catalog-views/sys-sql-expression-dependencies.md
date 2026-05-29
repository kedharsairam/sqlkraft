---
name: 'sys.sql_expression_dependencies'
title: 'sys.sql_expression_dependencies'
category: 'compatibility'
description: 'Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains one row for each by-name dependency on a user-defined entity in the current database. This includes dependencies between natively compiled, scalar user-defined functions and other SQL Server modules. A dependency between two entities is created when one entity, , appears by name in a persisted SQL expression of ano'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: 'sys.sql_expression_dependencies'
---

## Description

Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains one row for each by-name dependency on a user-defined entity in the current database. This includes dependencies between natively compiled, scalar user-defined functions and other SQL Server modules. A dependency between two entities is created when one entity, , appears by name in a persisted SQL expression of another entity,

## Syntax

```sql
sys.sql_expression_dependencies
```
