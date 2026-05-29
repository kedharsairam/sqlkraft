---
name: 'sys.external_languages'
title: 'sys.external_languages'
category: 'external'
description: 'SQL Server 2019 (15.x)'
tags: ["catalog-view", "external"]
pubDate: 2026-05-29
---

Article

•

12/15/2022

Applies to:

SQL Server 2019 (15.x)

Azure SQL Managed Instance

This catalog view provides a list of the external languages in the database.

and

are

reserved names and no external language can be created with those specific names.

The catalog view sys.external_languages lists a row for each external language in the database.


## Description
external_language_id

int

ID of the external language

language

sysname

Name of the external language. Is unique within the database. R and

Python are reserved names per instance

create_date

datetime2

Date and time of creation

principal_id

int

ID of the principal that owns this external library

sys.external_language_files

CREATE EXTERNAL LANGUAGE

ﾉ

Expand table

See also
