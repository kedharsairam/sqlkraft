---
title: "Use the query optimizer assistant"
topic: "profiler"
description: |
  Quickstart: Query optimizer assistant
          
            GitHub Copilot helps developers optimize queries and analyze performance bottlenecks
          
            without needing expertise in database internals, especially developers with
tags: ["profiler","use-the-query-optimizer-assistant"]
pubDate: 2025-12-01
---

Quickstart: Query optimizer assistant

GitHub Copilot helps developers optimize queries and analyze performance bottlenecks

without needing expertise in database internals, especially developers without deep Transact-

SQL (T-SQL) expertise. GitHub Copilot can break down complex SQL, interpret execution plans,

and suggest indexing strategies or refactoring opportunities. Developers can keep their apps

functional and performant, while staying focused on feature delivery.

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

GitHub Copilot offers multiple ways to help developers write performant, production-ready

database code without requiring deep expertise in query tuning or execution plan analysis.

Whether you're building new features or investigating a performance issue, GitHub Copilot can

provide insights, recommend optimizations, and help restructure queries. You can access all

these capabilities within your existing workflow in Visual Studio Code.

The following sections describe common use cases and examples of what you can ask via the

chat participant.

Use GitHub Copilot to identify inefficiencies in SQL or object-relational mapping (ORM) queries

and suggest ways to improve performance. GitHub Copilot helps you apply T-SQL and ORM

```cmd
@mssql
AdventureWorksLT2022
@mssql
@mssql
```
