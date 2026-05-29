---
name: "Use EXECUTE AS CALLER stand-alone statement"
title: "Use EXECUTE AS CALLER stand-alone statement"
category: "statements"
description: "For example, assume the following conditions:"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

For example, assume the following conditions:

group has access to the

database.

is a member of

and therefore has access to the

database.

The user that is creating or altering the module has permissions to create principals.

When the following

statement is run, the

is

implicitly created as a database principal in the

database.

SQL

Use the

stand-alone statement inside a module to set the execution context

to the caller of the module.

Assume the following stored procedure is called by

.

SQL

Windows domain account that is specified in the

clause. This will cause the

execution of the module to fail.

```sql
CompanyDomain\SQLUsers
```

```sql
Sales
```

```sql
CompanyDomain\SqlUser1
```

```sql
SQLUsers
```

```sql
Sales
```

```sql
CREATE PROCEDURE
```

```sql
CompanyDomain\SqlUser1
```

```sql
Sales
```

```sql
EXECUTE AS CALLER
```

```sql
SqlUser2
```

```sql
EXECUTE AS
```

```sql
USE
Sales;
GO
CREATE
PROCEDURE
dbo.usp_Demo
WITH
EXECUTE
AS
'CompanyDomain\SqlUser1'
AS
SELECT
USER_NAME();
GO
```

```sql
CREATE
PROCEDURE
dbo.usp_Demo
WITH
EXECUTE
AS
'SqlUser1'
AS
SELECT
USER_NAME();
-- Shows execution context is set to SqlUser1.
EXECUTE
AS
CALLER;
SELECT
USER_NAME();
-- Shows execution context is set to SqlUser2, the caller of
the module.
REVERT;
```
