---
name: "Object identification and name resolution"
title: "Object identification and name resolution"
category: "operators"
description: "Azure SQL Managed Instance"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes scalar functions that return information about the database and database

objects.

All metadata functions are

nondeterministic

. They don't always return the same results every

time they're called, even with the same set of input values.

Find out where you're running (instance and database) and who you're running as or through

(client application, database principal). Use this information for environment-aware scripts and

diagnostics.

## Description

SERVERPROPERTY

## Returns properties of the SQL Server instance such as edition, collation, or

product level.

DB_ID

## Returns the ID of a database.

DB_NAME

## Returns the name of a database given the ID.

DATABASEPROPERTYEX

## Returns database-level property values, such as collation and status.

ORIGINAL_DB_NAME

## Returns the original database name before a restore sequence.

APP_NAME

## Returns the application name for the current session.

DATABASE_PRINCIPAL_ID

## Returns the principal ID for a database security principal.

VERSION

## Returns the version string for Azure Synapse Analytics and Analytics Platform

System (PDW).

: Azure Synapse Analytics and Analytics Platform System (PDW) only

Resolve IDs to names across objects and schemas, and parse multipart identifiers. These

functions provide core support for introspection and dynamic SQL.

Expand table

1

#### Function

#### Function

#### Function
