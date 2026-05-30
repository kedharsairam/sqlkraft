---
title: "Load Files"
topic: "filestream"
description: |
  Article

  •

  07/09/2024

  Applies to:

  SQL Server

  Describes how to load or migrate files into FileTables.

  The method that you choose for loading or migrating files into a FileTable depends on where

  t
tags:
  - "filestream"
  - "load-files"
pubDate: 2025-12-01
---

Article

•

07/09/2024

Applies to:

SQL Server

Describes how to load or migrate files into FileTables.

The method that you choose for loading or migrating files into a FileTable depends on where

the files are currently stored.

Files are currently stored

in the file system.

SQL Server has no

knowledge of the files.

Since a FileTable appears as a folder in the Windows file system, you can easily

load files into a new FileTable by using any of the available methods for

moving or copying files. These methods include Windows Explorer,

command-line options including

and

, and custom scripts or

applications.

You can't convert an existing folder to a FileTable.

Files are currently stored

in the file system.

SQL Server contains a

table of metadata that

contains pointers to the

files.

The first step is to move or copy the files by using one of the preceding

methods mentioned.

The second step is to update the existing table of metadata to point to the

new location of the files.

For more information, see

Example: Migrate files from the file system into a

FileTable

in this article.

You can use the following methods to load files into a FileTable:

Drag and drop files from the source folders to the new FileTable folder in Windows

Explorer.

Use command-line options such as

,

,

, or

from the command

prompt or in a batch file or script.

ﾉ

Expand table

```sql
move copy xcopy robocopy
```
