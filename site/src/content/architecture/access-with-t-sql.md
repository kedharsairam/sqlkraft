---
title: "Access with T-SQL"
topic: "filestream"
description: "Describes how Transact-SQL data manipulation language (DML) commands work with FileTables. The following considerations apply to Operations on FileT"
tags: ["filestream","access-with-t-sql"]
pubDate: "2025-12-01"
---

Describes how Transact-SQL data manipulation language (DML) commands work with

FileTables.

The following considerations apply to

Operations on FileTables:

All the file attribute columns have NOT NULL constraints. If values are not explicitly set,

then appropriate default values are supplied.

System-defined constraints are enforced if the INSERT statement sets the

,

,

, or file attributes.

The application can obtain the

for a file or directory by providing the file

system path to the

GetPathLocator (Transact-SQL)

function.

The following considerations apply to

operations on FileTables:

Updates to any user-defined data are allowed.

System-defined constraints are enforced if the INSERT statement sets the

,

,

, or file attributes.

Updates can be made to the FILESTREAM data in the

column without

affecting any of the other columns, including the timestamps.

The following considerations apply to

operations on FileTables:

Deleting a row also removes the corresponding file or directory from the file system.

Deleting a row fails if the row corresponds to a directory that contains other files or

directories.
