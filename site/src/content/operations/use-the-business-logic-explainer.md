---
title: "Use the business logic explainer"
topic: "profiler"
description: |
  Quickstart: Use the business logic explainer
  
  In this quickstart, you learn how the business logic explainer helps developers understand and
  
  work with complex application logic implemented in SQL, ob
tags:
  - "profiler"
  - "use-the-business-logic-explainer"
pubDate: 2025-12-01
---

Quickstart: Use the business logic explainer

In this quickstart, you learn how the business logic explainer helps developers understand and

work with complex application logic implemented in SQL, object-relational mapping (ORM)

frameworks, or directly in the database. The assistant analyzes SQL code, ORM models, or

existing database schemas to explain the underlying business rules and provide actionable

documentation.

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

GitHub Copilot can help you understand and explain business rules embedded in database

code, ORM models, and application queries. From stored procedures to LINQ queries and

Sequelize expressions, GitHub Copilot provides natural language insights to make complex

logic more accessible.

Here are common use cases and examples of what you can ask via the chat participant:

Use GitHub Copilot to understand and explain Transact-SQL (T-SQL) logic, from stored

procedures to inline conditional statements. Whether you're reviewing discount rules,

procedural logic, or optimization conditions, GitHub Copilot can analyze and document

business rules implemented in T-SQL.

```cmd
@mssql
AdventureWorksLT2022
@mssql
@mssql
```