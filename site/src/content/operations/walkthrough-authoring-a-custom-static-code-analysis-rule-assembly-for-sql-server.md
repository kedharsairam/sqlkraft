---
title: "Walkthrough authoring a custom static Code Analysis rule assembly for SQL Server"
topic: "ssb-diagnose"
description: "This walkthrough demonstrates the steps used to create a SQL Server code analysis rule. The"
tags: ["ssb-diagnose","walkthrough-authoring-a-custom-static-code-analysis-rule-assembly-for-sql-server"]
pubDate: 2025-12-01
---

This walkthrough demonstrates the steps used to create a SQL Server code analysis rule. The

rule created in this walkthrough is used to avoid

statements in stored

procedures, triggers, and functions.

In this walkthrough, you create a custom rule for Transact-SQL static code analysis by using the

following steps:

1. Create a class library project, enable signing for that project, and add the necessary

references.

2. Create two helper C# classes.

3. Create a C# custom rule class.

4. Build the class library project.

5. Install and test the new code analysis rule.

Except for the Visual Studio (SQL Server Data Tools) instructions, the guide focuses on SDK-

style SQL projects.

You need the following components to complete this walkthrough:

A version of Visual Studio installed, which includes SQL Server Data Tools, and supports

C#.NET Framework development.

A SQL Server project that contains SQL Server objects.

An instance of SQL Server to which you can deploy a database project.

This walkthrough is intended for users who are already familiar with the SQL Server features of

Data Tools. You should be familiar with Visual Studio concepts, such as how to

create a class library, add NuGet packages, and how to use the code editor to add code to a

class.

First create a class library. To create a class library project:

1. Create a C# (.NET Framework) class library project named.

2. Rename the file

to.

```cmd
WAITFOR DELAY
SampleRules
Class1.cs
AvoidWaitForDelayRule.cs
```
