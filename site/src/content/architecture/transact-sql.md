---
title: "Transact-SQL"
topic: "query-processing"
description: "The use of the vardecimal storage format."
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Deprecated feature

Replacement

Feature name

Deprecated feature

Replacement

Feature name

The use of the vardecimal storage format.

Vardecimal storage format is

deprecated. SQL Server 2019 (15.x)

data compression, compresses

decimal values, and other data types.

We recommend that you use data

compression instead of the vardecimal

storage format.

Vardecimal storage format

Use of the

procedure.

Vardecimal storage format is

deprecated. SQL Server 2019 (15.x)

data compression, compresses

decimal values as well as other data

types. We recommend that you use

data compression instead of the

vardecimal storage format.

Use of the

procedure.

Use data compression and the

procedure instead.

Deprecated feature

Replacement

Feature name

WRITETEXT

UPDATETEXT

READTEXT

None

UPDATETEXT or WRITETEXT

READTEXT

TEXTPTR()

TEXTVALID()

None

TEXTPTR

TEXTVALID

Deprecated feature

Replacement

Feature name

function-calling sequence

Replaced by

.

For example, replace

'::' function calling syntax

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

Deprecated feature

Replacement

Feature name

with

.

Three-part and four-part column

references.

Two-part names are the standard-compliant behavior.

More than two-part column

name

A string enclosed in quotation marks

used as a column alias for an

expression in a

list:

'

string_alias

' =

expression

expression

[AS]

column_alias

expression

[AS] [

column_alias

]

expression

[AS] "

column_alias

"

expression

[AS] '

column_alias

'

column_alias

=

expression

String literals as column

aliases

Numbered procedures

None. Don't use.

ProcNums

table_name.index_name

## syntax in

## syntax in

.

with two-part

name

Not ending Transact-SQL statements

with a semicolon.

End Transact-SQL statements with a semicolon (

).

None

Use custom case-by-case solution with

or derived table.

as a column name in DML

statements.

Use $rowguid.

IDENTITYCOL as a column name in

DML statements.

Use $identity.

IDENTITYCOL

Use of #, ## as temporary table and

temporary stored procedure names.

Use at least one additional character.

'#' and '##' as the name of

temporary tables and stored

procedures

Use of @, or @@ as Transact-SQL

identifiers.

Don't use @ or @@ or names that begin with @@ as

identifiers.

'@' and names that start with

'@@' as Transact-SQL

identifiers

Use of

keyword as default

value.

Don't use the word

as a default value.

keyword as a default

value

Use of a space as a separator

between table hints.

Use a comma to separate table hints.

Multiple table hints without

comma

The select list of an aggregate

indexed view must contain

COUNT_BIG (\*) in 90 compatibility

mode

Use COUNT_BIG (\*).

Index view selects list without

COUNT_BIG(\*)

The indirect application of table hints

to an invocation of a multi-statement

table-valued function (TVF) through a

view.

None.

Indirect TVF hints

## syntax:

and

database option

None.

```sql
sys.sql_dependencies
sys.sql_expression_dependencies
sys.sql_dependencies
```

```sql
sp_db_vardecimal_storage_format
```

```sql
sp_db_vardecimal_storage_format
```

```sql
sp_estimated_rowsize_reduction_for_vardecimal
```

```sql
sp_estimate_data_compression_savings
```

```sql
sp_estimated_rowsize_reduction_for_vardecimal
```

```sql
::
```

```sql
SELECT <column_list> FROM sys.<function_name>
()
```

```sql
SELECT * FROM
```

```sql
::fn_virtualfilestats(2,1)
```

```sql
SELECT * FROM
sys.fn_virtualfilestats(2,1)
```

```sql
SELECT
```

```sql
DROP INDEX
<index_name> ON <table_name>
```

```sql
DROP INDEX
```

```sql
DROP INDEX
```

```sql
;
```

```sql
GROUP BY ALL
```

```sql
UNION
```

```sql
GROUP BY ALL
ROWGUIDCOL
```

```sql
ROWGUIDCOL
```

```sql
DEFAULT
```

```sql
DEFAULT
```

```sql
DEFAULT
```

```sql
ALTER DATABASE
```

```sql
MODIFY FILEGROUP READONLY
MODIFY FILEGROUP READWRITE
MODIFY FILEGROUP READ_ONLY
MODIFY FILEGROUP READ_WRITE
MODIFY FILEGROUP READONLY
MODIFY FILEGROUP READWRITE
SET ANSI_NULLS OFF
```

```sql
ANSI_NULLS
OFF
```

```sql
SET ANSI_NULLS OFF
```
