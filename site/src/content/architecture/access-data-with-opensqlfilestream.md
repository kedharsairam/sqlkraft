---
title: "Access data with OpenSqlFilestream"
topic: "filestream"
description: "The OpenSqlFilestream API obtains a Win32 compatible file handle for a FILESTREAM binary large object (BLOB) stored in the file system."
tags: ["filestream","access-data-with-opensqlfilestream"]
pubDate: 2025-12-01
---

The OpenSqlFilestream API obtains a Win32 compatible file handle for a FILESTREAM binary

large object (BLOB) stored in the file system. The handle can be passed to any of the following

Win32 APIs:

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

FlushFileBuffers. If

you pass this handle to any other Win32 API, the error ERROR_ACCESS_DENIED is returned. The

handle must be closed by passing it to the Win32

CloseHandle

API before the transaction is

committed or rolled back. Failing to close the handle will cause server-side resource leaks.

You must perform All FILESTREAM data container access in a SQL Server transaction. Transact-

SQL statements can also be executed in the same transaction. This maintains consistency

between the SQL data and FILESTREAM BLOB data.

To access the FILESTREAM BLOB by using Win32,

Windows Authorization

must be enabled.

）

Important

When the file is opened for write access, the transaction is owned by the FILESTREAM

agent. Only Win32 file I/O is allowed until the transaction is released. To release the

transaction, the write handle must be closed.

```sql
HANDLE OpenSqlFilestream (
LPCWSTR FilestreamPath,
SQL_FILESTREAM_DESIRED_ACCESS DesiredAccess,
ULONG OpenOptions,
LPBYTE FilestreamTransactionContext,
SIZE_T FilestreamTransactionContextLength,
PLARGE_INTEGER AllocationSize);
```
