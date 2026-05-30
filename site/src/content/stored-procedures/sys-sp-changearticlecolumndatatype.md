---
name: "sys.sp_changearticlecolumndatatype"
title: "sp_changearticlecolumndatatype"
category: "general"
description: "Changes the article column data type mapping for an Oracle publication. This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The name of the Oracle publication. The data type mappings between supported Publisher types are provided by default. Use only when overriding these default settings."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_changearticlecolumndatatype"
---

## Description

Changes the article column data type mapping for an Oracle publication. This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The name of the Oracle publication. The data type mappings between supported Publisher types are provided by default. Use only when overriding these default settings.

## Syntax

```sql
sp_changearticlecolumndatatype
```

## Permissions

is used to override the default data type mappings between supported Publisher types (Oracle and SQL Server). To view these default data type mappings, execute sp_getdefaultdatatypemapping . is only supported for Oracle Publishers. Executing this stored procedure against a SQL Server publication results in an error. must be executed for each article column mapping that must be changed. Only members of the fixed server role or fixed database role can execute . Change Publication and Article Properties Data Type Mapping for Oracle Publishers Replication stored procedures (Transact-SQL) Related content
