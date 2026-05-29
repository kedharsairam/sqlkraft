---
title: "Use the security analyzer"
topic: "profiler"
description: |
  Quickstart: Security analyzer
  
  GitHub Copilot helps developers identify and address common security risks in SQL code and
  
  application-layer queries. It detects vulnerabilities like SQL injection, ove
tags:
  - "profiler"
  - "use-the-security-analyzer"
pubDate: 2025-12-01
---

Quickstart: Security analyzer

GitHub Copilot helps developers identify and address common security risks in SQL code and

application-layer queries. It detects vulnerabilities like SQL injection, overexposed data, and

unsafe patterns. Developers without a strong security background can use GitHub Copilot to

get practical, context-aware recommendations during development.

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

GitHub Copilot helps developers detect and fix common security vulnerabilities early in the

development process, before they reach production. Whether you're using raw SQL, object-

relational mapping (ORM) frameworks, or stored procedures, GitHub Copilot can identify

unsafe patterns, explain potential risks, and suggest safer alternatives based on your database

context. This ability is especially useful for developers who don't specialize in security but need

to follow secure coding practices.

The following sections describe common use cases and examples of what you can ask via the

chat participant.

SQL injection is one of the most common and dangerous security vulnerabilities in database

applications. GitHub Copilot can help you identify unparameterized queries, string

SQL injection detection

```cmd
@mssql
AdventureWorksLT2022
@mssql
@mssql
```