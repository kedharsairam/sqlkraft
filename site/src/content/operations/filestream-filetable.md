---
title: "FILESTREAM & FileTable"
topic: "high-availability"
description: |
  Article

  •

  10/03/2023

  Applies to:

  SQL Server

  - Windows only

  This article contains information about the using the FILESTREAM and FileTable features with

  Always On availability groups in SQL Serv
tags:
  - "high-availability"
  - "filestream-filetable"
pubDate: 2025-12-01
---

Article

•

10/03/2023

SQL Server

- Windows only

This article contains information about the using the FILESTREAM and FileTable features with

Always On availability groups in SQL Server.

All FILESTREAM functionality is supported. After a failover, FILESTREAM data is accessible on

both readable secondary replicas and on the new primary.

FileTable functionality is partially supported. After a failover, FileTable data is accessible on the

primary replica, but FileTable data isn't accessible on readable secondary replicas.

Before adding a database that uses FILESTREAM, with or without FileTable, to an

availability group, ensure that FILESTREAM is enabled on every server instance that hosts

an availability replica for the availability group. For more information, see

Enable and

Configure FILESTREAM.

On a Windows Server 2012-based failover cluster, you should apply the hotfix discussed

in

Can't access VNN FILESTREAM share when you use the FILESTREAM and FileTable

features on a Windows Server 2012-based failover cluster

to access file share using

Virtual Network Name (VNN). This hotfix is also available at

Microsoft Update Catalog.

When you enable FILESTREAM on an instance of SQL Server, an instance-level share is created

to provide access to the FILESTREAM data. You access this share by using the computer name

in the following format:

In an Always On availability group, however, the name of the computer is virtualized by using a

Virtual Network Name, or VNN. When the computer is the primary replica in an availability

group, and databases in the availability group contain FILESTREAM data, then a VNN-scoped

share is also created to provide access to the FILESTREAM data. This doesn't affect Transact-

```cmd
\\<computer_name>\<filestream_share_name>
```
