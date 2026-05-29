---
name: "Context switching"
title: "Context switching"
category: "statements"
description: "data types can be specified that allow for"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Specify a user or login name

## Best practices

In SQL Server, the

and

data types can be specified that allow for

character strings to be up to 2 gigabytes of data.

Changes in database context last only until the end of the

statement. For example,

after the

in this following statement is run, the database context is

.

SQL

You can use the

clause to switch the execution context of a

dynamic statement. When the context switch is specified as

, the duration of the context switch is limited to the scope of the query

being executed.

The user or login name specified in

must exist as a principal in

or

respectively, or the statement fails.

Additionally,

## permissions must be granted on the principal. Unless the caller is the

database owner or is a member of the

fixed server role, the principal must exist even

when the user is accessing the database or instance of SQL Server through a Windows group

membership. For example, assume the following conditions:

group has access to the

database.

is a member of

and, therefore, has implicit access to

the

database.

Although

has access to the database through membership in the

group, the statement

fails because

doesn't exist as a principal in the database.

```sql
EXECUTE
```

```sql
EXECUTE
```

```sql
master
```

```sql
AS { LOGIN | USER } = '<name>'
```

```sql
EXECUTE ('string') AS
<context_specification>
```

```sql
AS { LOGIN | USER } = '<name>'
```

```sql
sys.database_principals
```

```sql
sys.server_principals
```

```sql
IMPERSONATE
```

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
CompanyDomain\SqlUser1
```

```sql
SQLUsers
```

```sql
EXECUTE @string_variable AS USER = 'CompanyDomain\SqlUser1'
```

```sql
CompanyDomain\SqlUser1
```

```sql
USE
master
;
EXECUTE
(
'USE AdventureWorks2022; SELECT BusinessEntityID, JobTitle FROM
HumanResources.Employee;'
);
```
