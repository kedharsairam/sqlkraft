---
name: 'sys.dm_exec_describe_first_result_set'
title: 'sys.dm_exec_describe_first_result_set'
category: 'execution'
description: 'SQL database in Microsoft Fabric This dynamic management function takes a Transact-SQL statement as a parameter and returns the metadata for the first result set of the statement. returns the same result set definition as sys.dm_exec_describe_first_result_set_for_object Transact-SQL syntax conventions One or more Transact-SQL statements. The provides a declaration string for parameters for the Tra'
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: 'sys.dm_exec_describe_first_result_set'
---

## Description

SQL database in Microsoft Fabric This dynamic management function takes a Transact-SQL statement as a parameter and returns the metadata for the first result set of the statement. returns the same result set definition as sys.dm_exec_describe_first_result_set_for_object Transact-SQL syntax conventions One or more Transact-SQL statements. The provides a declaration string for parameters for the Transact-SQL batch, similar to

## Syntax

```sql
sys.dm_exec_describe_first_result_set
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Returns only metadata to the client. Can be used to test the format of the response without actually running the query. Transact-SQL syntax conventions syntaxsql When is , a rowset is returned with the column names, but without any data rows. has no effect when the Transact-SQL batch is parsed. The effect occurs during execution run time. The default value is . Requires membership in the public role. ７ Note Do not use this feature. This feature has been replaced by the following items:
