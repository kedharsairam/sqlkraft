---
title: "Storing data files in Azure"
topic: "collation"
description: "data files in Microsoft Azure SQL Server Data Files in Microsoft Azure enables native support for SQL Server database files stored as blobs."
tags: ["collation","storing-data-files-in-azure"]
pubDate: 2025-12-01
---

data files in Microsoft Azure

Data Files in Microsoft Azure enables native support for SQL Server database files

stored as blobs. It allows you to create a database in SQL Server running in on-premises or in a

virtual machine in Microsoft Azure with a dedicated storage location for your data in Microsoft

Azure Blob storage. It also simplifies the process of moving databases between machines. You

can detach databases from one machine and attach them to another machine. In addition, it

provides an alternative storage location for your database backup files by allowing you to

restore from or to Microsoft Azure Storage. Therefore, it enables several hybrid solutions by

providing several benefits for data virtualization, data movement, security and availability, and

any easy low costs and maintenance for high-availability and elastic scaling.

This article introduces concepts and considerations that are central to storing SQL Server data

files in Microsoft Azure Storage Service.

Ready to get started? Follow this step-by-step workflow to use SQL Server data files with Azure

Blob storage:

）

Important

Storing system databases in Azure Blob Storage is not recommended and is not

supported.

Prerequisites checklist
