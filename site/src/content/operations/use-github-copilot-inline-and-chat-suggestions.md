---
title: "Use GitHub Copilot inline and chat suggestions"
topic: "profiler"
description: |
  Quickstart: Use chat and inline GitHub

  GitHub Copilot provides both inline suggestions while typing in the code editor and an

  interactive chat experience. You can ask the chat participant questions
tags:
  - "profiler"
  - "use-github-copilot-inline-and-chat-suggestions"
pubDate: 2025-12-01
---

Quickstart: Use chat and inline GitHub

GitHub Copilot provides both inline suggestions while typing in the code editor and an

interactive chat experience. You can ask the chat participant questions or provide prompts by

typing

followed by your prompt.

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

Use the

chat participant in GitHub Copilot Chat to bring intelligent, context-aware

assistance into your SQL development workflow, all directly within Visual Studio Code. Whether

you're writing queries, evolving your schema, or integrating with application code, GitHub

Copilot can help you design and understand relational models, generate or optimize T-SQL

code, create seed data, scaffold ORM migrations, and even explain business logic or security

concerns using natural language, all tailored to your connected database context.

Here are common use cases and examples of what you can ask via the chat participant:

Ask questions about tables, columns, schemas, and object metadata in your database.

```cmd
@mssql
@mssql
AdventureWorksLT2022
@mssql
@mssql
```
