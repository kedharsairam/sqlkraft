---
title: "Use Azure Blob Storage with SQL Server databases"
topic: "configuration"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  This tutorial helps you understand how to use the Azure Blob Storage for data files and
  
  backups in SQL Server 2016 (13.x) and later versions.
  
  
tags:
  - "configuration"
  - "use-azure-blob-storage-with-sql-server-databases"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

This tutorial helps you understand how to use the Azure Blob Storage for data files and

backups in SQL Server 2016 (13.x) and later versions.

Support for Azure Blob Storage in SQL Server was introduced in SQL Server 2012 (11.x) Service

Pack 1 CU2, and enhanced in later versions. For an overview of the functionality and benefits of

using this feature, see

SQL Server data files in Microsoft Azure

.

This tutorial shows you how to work with SQL Server data files in Azure Blob Storage in

multiple sections. Each section is focused on a specific task, and you should complete the

sections in sequence. First, you learn how to create a new container in Blob Storage with a

stored access policy and a shared access signature. Then, you learn how to create a SQL Server

credential to integrate SQL Server with Azure Blob Storage. Next, you back up a database to

Blob Storage and restore it to an Azure virtual machine. You then use SQL Server file-snapshot

transaction log backup to restore to a point in time and to a new database. Finally, the tutorial

demonstrates the use of metadata system stored procedures and functions to help you

understand and work with file-snapshot backups.

To complete this tutorial, you must be familiar with SQL Server backup and restore concepts

and T-SQL syntax.

To use this tutorial, you need an Azure storage account, SQL Server Management Studio

(SSMS), access to an instance of SQL Server on-premises, access to an Azure virtual machine

(VM) running an instance of SQL Server 2016 (13.x) or later version, and an

database. Additionally, the account used to issue the

and

commands should

be in the

database role with

permissions.

Get a free

Azure Account

.

Create an

Azure storage account

.

Install

SQL Server 2017 Developer Edition

.

Provision an

Azure VM running SQL Server

.

Install

SQL Server Management Studio

.

Download

AdventureWorks sample databases

.

Assign the user account to the role of

db_backupoperator

and grant

alter any credential

permissions.

```cmd
AdventureWorks2022
BACKUP
RESTORE
```