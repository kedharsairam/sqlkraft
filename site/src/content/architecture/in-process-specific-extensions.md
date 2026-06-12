---
title: "In-Process Specific Extensions"
topic: "clr-integration"
description: |
  SQL Server in-process specific extensions

  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  There are four main functional extensions to ADO.NET that are specifically for in-process use.

  The followin
tags:
  - "clr-integration"
  - "in-process-specific-extensions"
pubDate: 2025-12-01
---

in-process specific extensions

Article

•

12/30/2024

SQL Server

There are four main functional extensions to ADO.NET that are specifically for in-process use.

The following articles will cover these extensions in detail.

Description

SqlContext object

This class provides access to the other extensions by abstracting the context of a

caller of a SQL Server routine that executes managed code in-process.

SqlPipe object

This class contains routines to send tabular results and messages to the client.

SqlTriggerContext

object

This class provides information on the context in which a trigger is run.

SqlDataRecord

object

The

class represents a single row of data, along with its related

metadata, and allows stored procedures to return custom result sets to the client.

ﾉ

Expand table

`SqlDataRecord`
