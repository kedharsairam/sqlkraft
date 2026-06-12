---
title: "Compatibility Certification"
topic: "upgrade"
description: |
  06/16/2025

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Compatibility certification allows businesses to upgrade and modernize a SQL Server database

  on-premises, in the c
tags:
  - "upgrade"
  - "compatibility-certification"
pubDate: 2025-12-01
---

06/16/2025

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Compatibility certification allows businesses to upgrade and modernize a SQL Server database

on-premises, in the cloud, and on the edge, eliminating risks of application compatibility.

The same Database Engine powers both SQL Server and Azure SQL Database (including Azure

SQL Managed Instance). This shared Database Engine means that a user database can be

moved seamlessly between on-premises SQL Server and Azure SQL Database, while the

application code that executes in the database as Transact-SQL continues to work as it would in

its source system.

For each new release of SQL Server, the default compatibility level is set to the version of the

Database Engine. But the compatibility level of previous versions is preserved for continued

compatibility of existing applications. This compatibility matrix can be seen

here. Therefore, an

application that was certified to work with a given SQL Server version.

For example, database compatibility level 130 was the default in SQL Server 2016 (13.x).

Because compatibility levels force specific Transact-SQL functional and query optimization

behaviors,. This database can work as-is on a more recent version of SQL

Server (such as SQL Server 2019 (15.x)) and Azure SQL Database, as long as the database

compatibility level is kept as 130.

This is a fundamental principle for Microsoft Azure SQL Database continuous integration

operation model. The Database Engine is continuously improved and upgraded in Azure, but

because existing databases keep their current compatibility level, they continue to work as

designed even after upgrades to the underlying Database Engine.

This is also how SharePoint Server 2016 and SharePoint Server 2019 certify on SQL Server and

Azure SQL Managed Instance. You can deploy any SQL Server Database Engine that uses the

supported database compatibility levels for those SharePoint Server versions. For more

information, see

Hardware and software requirements for SharePoint Server 2016

and

Hardware and software requirements for SharePoint Server 2019.
