---
name: 'Table variables and row estimates'
title: 'Table variables and row estimates'
category: 'data-types'
description: 'A constraint that enforces entity integrity for a given column or columns through a unique'
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

A constraint that enforces entity integrity for a given column or columns through a unique

index. Only one

constraint can be created per table.

A constraint that provides entity integrity for a given column or columns through a unique

index. A table can have multiple

constraints.

Indicate that a clustered or a nonclustered index is created for the

or

constraint.

constraints use

, and

constraints use

.

can be specified for only one constraint. If

is specified for a

constraint and a

constraint is also specified, the

uses

.

A constraint that enforces domain integrity by limiting the possible values that can be entered

into a column or columns.

logical_expression

A logical expression that returns

or

.

Specifies one or more index options. Indexes can't be created explicitly on table variables, and

no statistics are kept on table variables. SQL Server 2014 (12.x) introduced syntax that allows

you to create certain index types inline with the table definition. Using this syntax, you can

create indexes on table variables as part of the table definition. In some cases, performance

might improve by using temporary tables instead, which provide full index support and

statistics.

For a complete description of these options, see

CREATE TABLE

.

```sql
PRIMARY KEY
```

```sql
UNIQUE
```

```sql
PRIMARY KEY
```

```sql
UNIQUE
```

```sql
PRIMARY KEY
```

```sql
CLUSTERED
```

```sql
UNIQUE
```

```sql
NONCLUSTERED
```

```sql
CLUSTERED
```

```sql
CLUSTERED
```

```sql
UNIQUE
```

```sql
PRIMARY KEY
```

```sql
PRIMARY KEY
```

```sql
NONCLUSTERED
```

```sql
TRUE
```

```sql
FALSE
```
