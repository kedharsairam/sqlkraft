---
name: "sys.sp_upgrade_log_shipping"
title: "sp_upgrade_log_shipping"
category: "general"
description: "stored procedure is invoked automatically for upgrading metadata that is specific to log shipping. Transact-SQL syntax conventions This stored procedure is invoked automatically during SQL Server upgrade for upgrading metadata for log shipping. You don't need to execute this procedure explicitly, unless a problem occurs with the metadata during upgrade. database on the primary, secondary, or fixed"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_upgrade_log_shipping"
---

## Description

stored procedure is invoked automatically for upgrading metadata that is specific to log shipping. Transact-SQL syntax conventions This stored procedure is invoked automatically during SQL Server upgrade for upgrading metadata for log shipping. You don't need to execute this procedure explicitly, unless a problem occurs with the metadata during upgrade. database on the primary, secondary, or fixed server role, or execute permission directly on this

## Syntax

```sql
sp_upgrade_log_shipping
```

## Permissions

06/23/2025 Applies to: SQL Server The stored procedure is invoked automatically for upgrading metadata that is specific to log shipping. Transact-SQL syntax conventions syntaxsql (success) or (failure). None. This stored procedure is invoked automatically during SQL Server upgrade for upgrading metadata for log shipping. You don't need to execute this procedure explicitly, unless a problem occurs with the metadata during upgrade. must be run from the database on the primary, secondary, or monitor server. Requires membership in the fixed server role, or execute permission directly on this stored procedure.
