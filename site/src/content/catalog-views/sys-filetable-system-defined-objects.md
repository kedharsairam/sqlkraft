---
name: 'sys.filetable_system_defined_objects'
title: 'sys.filetable_system_defined_objects'
category: 'objects'
description: 'Displays a list of the system-defined objects that are related to FileTables. Contains one row for'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Displays a list of the system-defined objects that are related to FileTables. Contains one row for

each system-defined object.

When you create a FileTable, related objects such as constraints and indexes are created at the

same time. You cannot alter or drop these objects; they disappear only when the FileTable itself

is dropped.

For more information about FileTables, see

FileTables (SQL Server)

.


## Description
Object ID of the system-defined object related to a FileTable.

References the object in

.

Object ID of the parent FileTable.

References the object in

.

Create, Alter, and Drop FileTables

Manage FileTables

ﾉ

Expand table

See Also
