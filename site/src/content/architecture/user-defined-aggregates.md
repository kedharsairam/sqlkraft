---
title: "User-defined aggregates"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  Aggregate functions perform a calculation on a set of values and return a single value.

  Traditionally, SQL Server supported only built-in aggregate fu
tags:
  - "clr-integration"
  - "user-defined-aggregates"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

Aggregate functions perform a calculation on a set of values and return a single value.

Traditionally, SQL Server supported only built-in aggregate functions, such as

or

, that

operate on a set of input scalar values and generate a single aggregate value from that set.

SQL Server integration with the .NET Framework common language runtime (CLR) now allows

developers to create custom aggregate functions in managed code, and to make these

functions accessible to Transact-SQL or other managed code.

The following table lists the articles in this section.

Description

Requirements for CLR user-defined

aggregates

Provides an overview of the requirements for implementing CLR

user-defined aggregate functions.

Invoke CLR user-defined

aggregate functions

Explains how to invoke user-defined aggregates.

ﾉ

Expand table

```sql
SUM
MAX
```
