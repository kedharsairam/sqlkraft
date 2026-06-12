---
name: "sys.external_libraries"
title: "sys.external_libraries"
category: "external"
description: "Summarize this article for me SQL Server 2017 (14.x) and later versions Azure SQL Managed Instance catalog view supports the management of package libraries related to external runtimes such as R, Python, and Java. lists a row for each external library that is uploaded into the database."
tags: ["external", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.external_libraries"
---

## Description

Summarize this article for me SQL Server 2017 (14.x) and later versions Azure SQL Managed Instance catalog view supports the management of package libraries related to external runtimes such as R, Python, and Java. lists a row for each external library that is uploaded into the database.

## Syntax

`sys.external_libraries`

## Remarks

Summarize this article for me

2017 (14.x) and later versions

Azure SQL Managed Instance

catalog view supports the management of package libraries

related to external runtimes such as R, Python, and Java.

lists a row for each external library that is uploaded into the database.

Description

ID of the external library object.

Name of the external library. Is unique within the database per

ID of the principal that owns this external library.

Name of the language or runtime that supports the external library.

Valid values are

for public scope;

for private scope.

Indicates whether the package is public or private.

In SQL Server 2017 (14.x), R language and Windows platform are supported. R, Python, and

Java on the Windows and Linux platforms are supported in SQL Server 2019 (15.x) and later. On

Azure SQL Managed Instance, R and Python are supported.

sys.external_library_files

CREATE EXTERNAL LIBRARY (Transact-SQL)

Install R packages with sqlmlutils

Expand table
