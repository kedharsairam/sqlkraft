---
title: "Access with File Input-Output APIs"
topic: "filestream"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Describes how file system I/O works on a FileTable.
  
  The primary usage of FileTables is expected to be through the Windows file system and file I/O
  
  AP
tags:
  - "filestream"
  - "access-with-file-input-output-apis"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Describes how file system I/O works on a FileTable.

The primary usage of FileTables is expected to be through the Windows file system and file I/O

APIs. FileTables support non-transactional access through the rich set of available file I/O APIs.

1. File I/O API access typically begins by acquiring a logical UNC path for the file or

directory. Applications can use a Transact-SQL statement with the

GetFileNamespacePath

(Transact-SQL)

function to obtain the logical path for the file or directory. For more

information, see

Work with Directories and Paths in FileTables

.

2. Then the application uses this logical path to obtain a handle to the file or directory and

do something with the object. The path can be passed to any supported file system API

function, such as CreateFile() or CreateDirectory(), to create or open a file and obtain a

handle. The handle can then be used to stream data, to enumerate or organize

directories, to get or set file attributes, to delete files or directories, and so forth.

A file or directory can be created in a FileTable by calling file I/O APIs such as CreateFile or

CreateDirectory.

All creation disposition flags, share modes, and access modes are supported. This

includes file creation, deletion and in-place modification. Also supported are File

Namespace updates i.e. directory creation/deletion, rename and move operations.

The creation of a new file or directory corresponds to the creation of a new row in the

underlying FileTable.

For files, the stream data is stored in the

column; for directories, this column is

null.

For files, the

column contains

. For directories, this column contains

.