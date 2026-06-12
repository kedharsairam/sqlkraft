---
title: "Files page"
topic: "collation"
description: "Use this page to create a new database, or view or modify properties for the selected database."
tags: ["collation","files-page"]
pubDate: "2025-12-01"
---

Use this page to create a new database, or view or modify properties for the selected database.

This topic applies to the

for existing databases, and to the.

Add or display the name of the database.

Specify the owner of the database by selecting from the list.

This check box is checked and disabled because full-text indexing is always enabled in SQL

Server. For more information, see

Full-Text Search.

Add, view, modify, or remove database files for the associated database. Database files have

the following properties:

Enter or modify the name of the file.

Select the file type from the list. The file type can be

,

, or. You cannot

modify the file type of an existing file.

Select

if you are adding files (containers) to a memory-optimized filegroup.

To add files (containers) to a Filestream data filegroup, FILESTREAM must be enabled. You can

enable FILESTREAM by using the

Server Properties (Advanced Page)

dialog box.

Select the filegroup for the file from the list. By default, the filegroup is PRIMARY. You can

create a new filegroup by selecting

and entering information about the

filegroup in the

dialog box. A new filegroup can also be created on the

page. You cannot modify the filegroup of an existing file.
