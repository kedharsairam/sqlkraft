---
title: "Create Client Applications"
topic: "filestream"
description: |
  Article
  
  •
  
  01/22/2024
  
  Applies to:
  
  SQL Server
  
  You can use Win32 APIs to read and write data to a FILESTREAM BLOB. The following steps are
  
  required:
  
  Read the FILESTREAM file path.
  
  Read the curren
tags:
  - "filestream"
  - "create-client-applications"
pubDate: 2025-12-01
---

Article

•

01/22/2024

Applies to:

SQL Server

You can use Win32 APIs to read and write data to a FILESTREAM BLOB. The following steps are

required:

Read the FILESTREAM file path.

Read the current transaction context.

Obtain a Win32 handle and use the handle to read and write data to the FILESTREAM

BLOB.

When you use FILESTREAM to store binary large object (BLOB) data, you can use Win32 APIs to

work with the files. To support working with FILESTREAM BLOB data in Win32 applications, SQL

Server provides the following functions and API:

PathName

returns a path as a token to a BLOB. An application uses this token to obtain a

Win32 handle and operate on BLOB data.

When the database that contains FILESTREAM data belongs to an Always On availability

group, then the PathName function returns a virtual network name (VNN) instead of a

computer name.

GET_FILESTREAM_TRANSACTION_CONTEXT()

returns a token that represents the current

transaction of a session. An application uses this token to bind FILESTREAM file system

streaming operations to the transaction.

The

OpenSqlFilestream API

obtains a Win32 file handle. The application uses the handle

to stream the FILESTREAM data, and can then pass the handle to the following Win32

APIs:

ReadFile

,

WriteFile

,

TransmitFile

,

SetFilePointer

,

SetEndOfFile

, or

FlushFileBuffers

. If

７

Note

The examples in this topic require the FILESTREAM-enabled database and table that are

created in

and

.