---
name: "Examples: Azure Synapse Analytics"
title: "Examples: Azure Synapse Analytics"
category: "statements"
description: ": SQL Server 2019 (15.x)."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## A: Basic procedure execution

: SQL Server 2019 (15.x).

The following example passes a command string to an external data source pointing to

compute pool in SQL Server Big Data Cluster (BDC). The example creates a data source

against a data pool in BDC and executes a

statement against the data

source.

: SQL Server 2019 (15.x).

The following example passes a command string to an external data source pointing to

compute pool in SQL Server Big Data Cluster. The example creates a data source

against a data pool in SQL Server Big Data Cluster and executes a

statement against the data source.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

Execute a stored procedure:

## B: Execute strings

## C: Procedures with parameters

Call a stored procedure with name determined at runtime:

Call a stored procedure from within a stored procedure:

Execute a SQL string:

Execute a nested string:

Execute a string variable:

The following example creates a procedure with parameters and demonstrates three ways to

execute the procedure:

Execute using positional parameters:

Execute using named parameters in order:

Execute using named parameters out of order:

@@NESTLEVEL (Transact-SQL)

DECLARE @local_variable (Transact-SQL)

EXECUTE AS clause (Transact-SQL)

osql Utility

Principals (Database Engine)

REVERT (Transact-SQL)

sp_addlinkedserver (Transact-SQL)
