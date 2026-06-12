---
title: "Data access from CLR database objects"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  A common language runtime (CLR) routine might easily access data stored in the instance of

  SQL Server in which it runs, and data stored in remote inst
tags:
  - "clr-integration"
  - "data-access-from-clr-database-objects"
pubDate: 2025-12-01
---

Article

•

12/30/2024

SQL Server

A common language runtime (CLR) routine might easily access data stored in the instance of

in which it runs, and data stored in remote instances. The user context in which the

code runs, determines the particular data the routine can access. Access data from within a CLR

database object by using the.NET Framework Data Provider for SQL Server, also referred to as. This is the same provider used by developers accessing SQL Server data from

managed client and middle-tier applications. Because of this, you can use your knowledge of

ADO.NET and

in client and middle-tier applications.

User-defined type methods and user-defined functions aren't allowed to perform data access

by default. You must set the

property of

or

to

to enable read-only data access from user-

defined type (UDT) methods or user-defined functions. Data modification operations aren't

allowed from UDTs or user-defined functions, and throw exceptions at execution time if

attempted.

This section discusses only the specific functional and behavioral differences when accessing

data from within a CLR database object. For more information about the features and

functionality of ADO.NET, see the ADO.NET documentation included in the.NET Framework

SDK.

The following table lists the articles in this section.

Description

Context connection

Describes the context connection to SQL Server.

Impersonation and

credentials for connections

Describes impersonating connections and connection credentials.

in-process specific

extensions to ADO.NET

Discusses the in-process specific

,

,

, and

objects.

CLR integration and

transactions

Describes how the new transaction framework provided in the

System.Transactions namespace integrates with ADO.NET and SQL Server

CLR integration.

XML Serialization from CLR

Database Objects

Explains how to enable XML serialization scenarios of CLR database

objects inside SQL Server.

ﾉ

Expand table

```sql
SqlClient
SqlClient
DataAccess
SqlMethodAttribute
SqlFunctionAttribute
DataAccessKind.Read
SqlPipe
SqlContext
SqlTriggerContext
SqlDataRecord
```
