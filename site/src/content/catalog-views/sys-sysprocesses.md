---
name: "sys.sysprocesses"
title: "sys.sysprocesses"
category: "compatibility"
description: "Associates up to 128 bytes of binary information with the current session or connection. constant, or a constant that is implicitly convertible to , to associate with the current session or connection. variable holding a context value to associate with the current session , SET CONTEXT_INFO affects the current session. T"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SET
  CONTEXT_INFO 0x1256698456;
  GO
  SELECT
  CONTEXT_INFO();
  GO
---

## Description

Associates up to 128 bytes of binary information with the current session or connection. constant, or a constant that is implicitly convertible to , to associate with the current session or connection. variable holding a context value to associate with the current session , SET CONTEXT_INFO affects the current session. The preferred way to retrieve the context information for the current session is to use the CONTEXT_INFO function. Session context information is also stored in the columns in the following system

## Syntax

```sql
SET
CONTEXT_INFO 0x1256698456;
GO
SELECT
CONTEXT_INFO();
GO
```

## Remarks

Azure SQL Database

Azure SQL Managed Instance

Associates up to 128 bytes of binary information with the current session or connection.

constant, or a constant that is implicitly convertible to

, to associate with the

current session or connection.

variable holding a context value to associate with the current session

or connection.

SET Statements

, SET CONTEXT_INFO affects the current session. The preferred way to

retrieve the context information for the current session is to use the CONTEXT_INFO function.

Session context information is also stored in the

columns in the following system

(deprecated)

## Examples

### Example 1

```sql
0x1256698456
```

### Example 2

`CONTEXT_INFO`

### Example 3

```sql
SET
CONTEXT_INFO 0x1256698456;
GO
SELECT
CONTEXT_INFO();
GO
```
