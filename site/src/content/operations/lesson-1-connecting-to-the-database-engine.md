---
title: "Lesson 1: Connecting to the Database Engine"
topic: "configuration"
description: |
  Applies to:
  
  SQL Server
  
  When you install the SQL Server Database Engine, the tools that are installed depend upon the
  
  edition and your setup choices. This lesson describes the principal tools, and d
tags:
  - "configuration"
  - "lesson-1-connecting-to-the-database-engine"
pubDate: 2025-12-01
---

Applies to:

SQL Server

When you install the SQL Server Database Engine, the tools that are installed depend upon the

edition and your setup choices. This lesson describes the principal tools, and demonstrates

how to connect to the Database Engine and perform an essential function (authorizing more

users).

In this lesson, learn the following:

Tools to get started

Connecting with Management Studio

Authorizing extra connections

The SQL Server Database Engine ships with various tools. This article describes the first tools

you need and helps you select the right tool for a job. All tools can be accessed from the

menu. Some tools, such as

SQL Server Management Studio (SSMS)

, aren't installed by default.

Select the tools that you want as components during setup. SQL Server Express contains only a

subset of the tools.

The following table describes some of the more common tools.

GUI

Windows

CLI

Windows, macOS, Linux

sqlcmd

CLI

Windows, macOS, Linux

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

ﾉ

Expand table

```cmd
AdventureWorks2025
AdventureWorksDW2025
```