---
title: "Use smart query builder"
topic: "profiler"
description: |
  Quickstart: Use the smart query builder

  In this quickstart, you learn how the query building assistant helps you craft efficient, accurate,

  and secure queries using either raw SQL or your preferred
tags:
  - "profiler"
  - "use-smart-query-builder"
pubDate: 2025-12-01
---

Quickstart: Use the smart query builder

In this quickstart, you learn how the query building assistant helps you craft efficient, accurate,

and secure queries using either raw SQL or your preferred ORM. Designed for both code-first

and data-first developers, it enables faster generation of production-ready logic aligned with

your connected database schema.

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

GitHub Copilot supports intelligent query construction directly within Visual Studio Code. From

basic SELECTs to complex joins, filters, and aggregations, it generates SQL or ORM queries that

follow best practices and reflect your current schema, so you can focus on your application

logic.

Here are common use cases and examples of what you can ask via the chat participant:

These prompts help analyze trends over time, such as recent sales activity, top performers by

period, or comparisons to historical averages. GitHub Copilot can build queries that calculate

values relative to your data's most recent dates, avoiding assumptions based on the current

system date.

```cmd
@mssql
AdventureWorksLT2022
@mssql
@mssql
```
