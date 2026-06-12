---
name: "Code example conventions"
title: "Code example conventions"
category: "statements"
description: "Schema name is omitted."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## Description

Four-part name.

Schema name is omitted.

Database name is omitted.

Database and schema name are omitted.

Server name is omitted.

Server and schema name are omitted.

Server and database name are omitted.

omitted.

When used inline in an article, data types are rendered in lowercase and bold. For example,

,

, and.

When used in Transact-SQL code blocks, data types are rendered in uppercase. For example:

using SQL Server Management Studio and its default settings for the following options:

```sql
<server_name>.<database_name>.<schema_name>.
<object_name>
```

```sql
<server_name>.<database_name>.<object_name>
```

```sql
<server_name>.<schema_name>.<object_name>
```

```sql
<server_name>.<object_name>
```

```sql
<database_name>.<schema_name>.<object_name>
```

```sql
<database_name>.<object_name>
```

```sql
<schema_name>.<object_name>
```

```sql
<object_name>
```

```sql
ANSI_NULLS
ANSI_NULL_DFLT_ON
ANSI_PADDING
```

```sql
DECLARE
@int_example
AS
INT
;
DECLARE
@varchar_example
AS
VARCHAR (255);
DECLARE
@bit_example
AS
BIT
;
```
