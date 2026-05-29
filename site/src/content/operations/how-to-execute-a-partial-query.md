---
title: "How to: Execute a Partial Query"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  The Transact-SQL Editor allows you to highlight a specific segment of the script and execute it
  
  as a single query. This makes it easy for you to debug sections of complex queries.
  
  1. In
  
tags:
  - "ssb-diagnose"
  - "how-to-execute-a-partial-query"
pubDate: 2025-12-01
---

09/10/2025

The Transact-SQL Editor allows you to highlight a specific segment of the script and execute it

as a single query. This makes it easy for you to debug sections of complex queries.

1. In

SQL Server Object Explorer

, double-click

under

to open it in

Transact-SQL editor.

2. Highlight the

segment in the code, right-click

and select

.

3. All the rows with the specified fields in the

table are returned in the

pane.

```cmd
PerishableFruits
SELECT p.Id, p.Name FROM dbo.Product p
Products
```