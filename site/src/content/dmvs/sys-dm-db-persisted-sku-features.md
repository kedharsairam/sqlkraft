---
name: "sys.dm_db_persisted_sku_features"
title: "sys.dm_db_persisted_sku_features"
category: "execution"
description: "SQL database in Microsoft Some features of the Database Engine change the way that information is stored in the database files. These features are restricted to specific editions of SQL Server. A database that contains these features can't be moved to an edition of SQL Server that doesn't support"
tags: ["execution","dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_db_persisted_sku_features"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Some features of the Database Engine change the way that information is stored in the database files. These features are restricted to specific editions of SQL Server. A database that contains these features can't be moved to an edition of SQL Server that doesn't support them. dynamic management view to list edition-specific features that are enabled in the current database. External name of the feature that is enabled in the database but not supported on the all the editions of SQL Server. This feature must be removed before the database can be migrated to all available editions of SQL Feature ID that is associated with the feature. Identified for informational purposes only. Not supported. Future compatibility is not guaranteed.

## Syntax

`sys.dm_db_persisted_sku_features`

## Remarks

Analytics Platform System (PDW)

SQL database in Microsoft

Some features of the Database Engine change the way that information is stored in the

database files. These features are restricted to specific editions of SQL Server. A database that

contains these features can't be moved to an edition of SQL Server that doesn't support them.

dynamic management view to list edition-specific

features that are enabled in the current database.

External name of the feature that is enabled in the database but not

supported on the all the editions of SQL Server. This feature must be

removed before the database can be migrated to all available editions of SQL

Feature ID that is associated with the feature. Identified for informational

purposes only. Not supported. Future compatibility is not guaranteed.

For SQL Server 2019 (15.x) and previous versions, requires VIEW DATABASE STATE permission

on the database.

For SQL Server 2022 (16.x) and later versions, requires VIEW DATABASE PERFORMANCE STATE

permission on the database.

If there are no features that may be restricted by a specific edition in the database, the view

returns no rows.

may list the following database-changing features as

restricted to specific SQL Server editions:
