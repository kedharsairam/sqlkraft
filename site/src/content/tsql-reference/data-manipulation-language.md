---
name: 'Data Manipulation Language'
title: 'Data Manipulation Language'
category: 'statements'
description: 'Azure SQL Managed Instance'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

A SQL statement is an atomic unit of work and either completely succeeds or completely fails.

A SQL statement is a set of instruction that consists of identifiers, parameters, variables, names,

data types, and SQL reserved words that compiles successfully. Analysis Services creates an

implicit

transaction for a SQL statement if a

command does not specify the

start of a transaction. Analysis Services always commits an implicit transaction if the statement

succeeds, and rolls back an implicit transaction if the command fails.

There are many types of statements. Perhaps the most important is the

SELECT

that retrieves

rows from the database and enables the selection of one or many rows or columns from one or

many tables in SQL Server. This article summarizes the categories of statements for use with

Transact-SQL (T-SQL) in addition to the

statement. You can find all of the statements

listed in the left-hand navigation.

The backup and restore statements provide ways to create backups and restore from backups.

For more information, see the

Backup and restore overview

.

Data Definition Language (DDL) statements defines data structures. Use these statements to

create, alter, or drop data structures in a database. These statements include:

ALTER

Collations

CREATE

DROP

DISABLE TRIGGER

ENABLE TRIGGER

RENAME

UPDATE STATISTICS

TRUNCATE TABLE

```sql
BeginTransaction
```

```sql
SELECT
```
