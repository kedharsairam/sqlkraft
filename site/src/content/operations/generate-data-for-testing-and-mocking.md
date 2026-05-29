---
title: "Generate data for testing and mocking"
topic: "profiler"
description: |
  Quickstart: Generate data for testing and
  
  In this quickstart, you learn how to use GitHub Copilot to create realistic and themed datasets
  
  to support application development, testing, and demos. By a
tags:
  - "profiler"
  - "generate-data-for-testing-and-mocking"
pubDate: 2025-12-01
---

Quickstart: Generate data for testing and

In this quickstart, you learn how to use GitHub Copilot to create realistic and themed datasets

to support application development, testing, and demos. By analyzing the schema and context

of your database, GitHub Copilot can generate mock data aligned with real-world formats,

simulate edge cases, and reduce the manual effort of seeding databases, making testing faster

and more representative of actual scenarios.

Make sure you're connected to a database and have an active editor window open with the

MSSQL extension. When you connect, the

chat participant understands the context of

your database environment and can give accurate, context-aware suggestions. If you don't

connect to a database, the chat participant doesn't have the schema or data context to provide

meaningful responses.

The following examples use the

sample database, which you can

download from the

Microsoft SQL Server Samples and Community Projects

home page.

For best results, adjust table and schema names to match your own environment.

Make sure the chat includes the

prefix. For example, type

followed by your

question or prompt. This prefix ensures that the chat participant understands you're asking for

SQL-related assistance.

GitHub Copilot can help you generate test and mock data directly from your SQL schema or

JSON samples. It offers contextual suggestions to help reduce time and improve coverage,

whether you're preparing datasets for demos, testing edge cases, or seeding your

development environment with themed or randomized data. These suggestions are especially

useful in scenarios where manual data entry would be slow or inconsistent.

Here are common use cases and examples of what you can ask via the chat participant.

```cmd
@mssql
AdventureWorksLT2022
@mssql
@mssql
```