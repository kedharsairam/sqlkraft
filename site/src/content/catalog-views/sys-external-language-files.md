---
name: 'sys.external_language_files'
title: 'sys.external_language_files'
category: 'databases-files'
description: 'SQL Server 2019 (15.x)'
tags: ["catalog-view", "databases-files"]
pubDate: 2026-05-29
---

Article

•

12/15/2022

Applies to:

SQL Server 2019 (15.x)

Azure SQL Managed Instance

This catalog view provides a list of the external language extension files in the database.

and

are reserved names and no external language can be created with those specific

names.

When an external language is created from a file_spec, the extension itself and its properties

are listed in this view. This view will contain one entry per language, per OS.

The catalog view sys.external_language_files lists a row for each external language extension in

the database. Parameters


## Description
external_language_id

int

ID of the external language

content

varbinary(max)

Content of the external language extension file

file_name

sysname

Name of the language extension file

platform

tinyint

ID of the host platform on which SQL Server is installed

platform_desc

nvarchar(60)

Name of the host platform. Valid values are

,

.

parameters

sysname

External language parameters

environment_variables

sysname

External language environment variables

sys.external_languages

CREATE EXTERNAL LANGUAGE

ﾉ

Expand table

See also

```sql
WINDOWS
```

```sql
LINUX
```
