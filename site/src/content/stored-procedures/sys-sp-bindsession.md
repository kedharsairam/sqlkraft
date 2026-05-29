---
name: "sys.sp_bindsession"
title: "sp_bindsession"
category: "general"
description: "Binds or unbinds a session to other sessions in the same instance of the SQL Server Database Engine. Binding sessions allows two or more sessions to participate in the same transaction and Transact-SQL syntax conventions The token that identifies the transaction originally obtained by using This feature will be removed in a future version of SQL Server. Avoid using this feature in new development "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_bindsession {
  'bind_token'
  |
  NULL
  }
---

## Description

Binds or unbinds a session to other sessions in the same instance of the SQL Server Database Engine. Binding sessions allows two or more sessions to participate in the same transaction and Transact-SQL syntax conventions The token that identifies the transaction originally obtained by using This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_bindsession {
'bind_token'
|
NULL
}
```

## Examples

### Example 1

```sql
SELECT
```

### Example 2

```sql
sp_bindsession
```

### Example 3

```sql
sp_getbindtoken
```

### Example 4

```sql
sp_bindsession
```

### Example 5

```sql
sp_bindsession
```

### Example 6

```sql
--COMMIT TRANSACTION;
--COMMIT TRANSACTION;
Token1
------
PKb'gN5<9aGEedk_16>8U=5---/5G=--
Token2
------
PKb'gN5<9aGEedk_16>8U=5---/5G=--
```

### Example 7

```sql
DECLARE
@bind_token
AS
VARCHAR
(255);
BEGIN
TRANSACTION
;
EXECUTE
sp_getbindtoken @bind_token
OUTPUT
;
```

### Example 8

```sql
SELECT
@bind_token
AS
Token;
--COMMIT TRANSACTION;
Token
-----
\0]---5^PJK51bP<1F<-7U-]ANZ
```
