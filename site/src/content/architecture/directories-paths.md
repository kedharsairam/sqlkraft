---
title: "Directories & Paths"
topic: "filestream"
description: |
  Article

  •

  10/03/2023

  Applies to:

  SQL Server

  Describes the directory structure in which the files are stored in FileTables.

  You can use the following three functions to work with FileTable direct
tags:
  - "filestream"
  - "directories-paths"
pubDate: 2025-12-01
---

Article

•

10/03/2023

Applies to:

SQL Server

Describes the directory structure in which the files are stored in FileTables.

You can use the following three functions to work with FileTable directories in Transact-SQL:

Get the root-level UNC path for a specific FileTable or for the current

database.

FileTableRootPath (Transact-SQL)

Get an absolute or relative UNC path for a file or directory in a

FileTable.

GetFileNamespacePath

(Transact-SQL)

Get the path locator ID value for the specified file or directory in a

FileTable, by providing the path.

GetPathLocator (Transact-SQL)

To keep code and applications independent of the current computer and database, avoid

writing code that relies on absolute file paths. Instead, get the complete path for a file at run

time by using the

FileTableRootPath (Transact-SQL)

and

GetFileNamespacePath (Transact-SQL)

)

functions together, as shown in the following example. By default, the

function returns the relative path of the file under the root path for the database.

SQL

ﾉ

Expand table

```sql
GetFileNamespacePath
USE
database_name;
DECLARE
@root
NVARCHAR
(100);
DECLARE
@fullpath
NVARCHAR
(1000);
SELECT
@root = FileTableRootPath();
SELECT
@fullpath = @root + file_stream.GetFileNamespacePath()
```
