---
name: "PRINT"
title: "PRINT"
category: "statements"
description: "Returns a user-defined message to the client application."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---
## Syntax

```sql
PRINT msg_str | @local_variable | string_expr
```

## Arguments

### msg_str

A string or character variable containing the message. Maximum length is 8000 characters.

### @local_variable

A variable of any valid character data type.

### string_expr

An expression that returns a string. Can include concatenated values and variables.

## Remarks

PRINT uses RAISERROR with a severity of 0 and state of 1. The message is returned to the client as an informational message.

## Examples

```sql
-- Print a simple message
PRINT 'Hello, World!';
GO

-- Print a variable value
DECLARE @msg nvarchar(100) = N'Current date: ' + CAST(GETDATE() AS nvarchar(50));
PRINT @msg;
```
