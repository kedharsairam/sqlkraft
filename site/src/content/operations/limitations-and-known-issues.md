---
title: "Limitations and known issues"
topic: "profiler"
description: |
  This article outlines the limitations and known constraints of GitHub Copilot integration with

  the MSSQL extension for Visual Studio Code. This experience is designed for application

  developers buil
tags:
  - "profiler"
  - "limitations-and-known-issues"
pubDate: 2025-12-01
---

This article outlines the limitations and known constraints of GitHub Copilot integration with

the MSSQL extension for Visual Studio Code. This experience is designed for application

developers building with SQL databases, not for database administrators managing

infrastructure or production environments. Understanding these boundaries ensures proper

expectations and supports a productive development workflow.

GitHub Copilot. Developers must manually

review and execute all generated SQL or object-relational mapping (ORM) code.

The

chat participant

through the editor to

provide schema-aware suggestions.

before use. GitHub Copilot might produce

incorrect or suboptimal recommendations.

This experience is

, not for database or system administrators.

While it can generate SQL scripts for administrative tasks, GitHub Copilot does

such as configuring backup/restore, managing

user permissions, or handling SQL Agent jobs.

GitHub Copilot sessions

(for example,

changing files or databases). New context resets the chat memory.

The chat participant works. Cross-

database operations aren't supported.

The integration is. Legacy or deprecated features might be unsupported.

and its Dedicated SQL pool (formerly SQL DW) features

by this GitHub Copilot integration.

GitHub Copilot provides the best suggestions when it has access to rich context. Keep

your database connection active and relevant code or queries open in the editor. The

more context GitHub Copilot has, the more accurate and relevant its suggestions are.

```cmd
@mssql
```
