---
title: "FileTable"
topic: "filestream"
description: |
  Article

  •

  10/03/2023

  Applies to:

  SQL Server

  The FileTable feature brings support for the Windows file namespace and compatibility with

  Windows applications to the file data stored in SQL Server.
tags:
  - "filestream"
  - "filetable"
pubDate: 2025-12-01
---

Article

•

10/03/2023

SQL Server

The FileTable feature brings support for the Windows file namespace and compatibility with

Windows applications to the file data stored in SQL Server. FileTable lets an application

integrate its storage and data management components, and provides integrated SQL Server

services - including full-text search and semantic search - over unstructured data and

metadata.

In other words, you can store files and documents in special tables in SQL Server called

FileTables, but access them from Windows applications as if they were stored in the file system,

without making any changes to your client applications.

The FileTable feature builds on top of SQL Server FILESTREAM technology. To learn more about

FILESTREAM, see

FILESTREAM (SQL Server).

The goals of the FileTable feature include the following:

Windows API compatibility for file data stored within a SQL Server database. Windows API

compatibility includes the following:

Non-transactional streaming access and in-place updates to FILESTREAM data.

A hierarchical namespace of directories and files.

Storage of file attributes, such as created date and modified date.

Support for Windows file and directory management APIs.

Compatibility with other SQL Server features including management tools, services, and

relational query capabilities over FILESTREAM and file attribute data.

Thus FileTables remove a significant barrier to the use of SQL Server for the storage and

management of unstructured data that is currently residing as files on file servers. Enterprises

can move this data from file servers into FileTables to take advantage of integrated

administration and services provided by SQL Server. At the same time, they can maintain

Windows application compatibility for their existing Windows applications that see this data as

files in the file system.
