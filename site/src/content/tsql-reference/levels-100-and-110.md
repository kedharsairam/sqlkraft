---
name: "levels 100 and 110"
title: "Levels 100 and 110"
category: "operators"
description: "value to a string value. This"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

value to a string value. This

behavior is specific only to the

type. See example B in the

## Examples

section.

Recursive references on the

right-hand side of an

clause create an infinite loop.

Example C in the

## Examples

section demonstrates this

behavior.

Recursive references in an

clause generate an error in

compliance with the ANSI SQL standard.

Recursive common table

expression (CTE) allows

duplicate column names.

Recursive CTE doesn't allow duplicate column names.

Disabled triggers are enabled if

the triggers are altered.

Altering a trigger doesn't change the state (enabled or disabled) of the

trigger.

The

table clause

ignores the

and allows

explicit values to be inserted.

You can't insert explicit values for an identity column in a table when

is set to

.

When the database

containment is set to partial,

validating the

field in

the

clause of a

statement can return a collation

error.

The collation of the values returned by the

clause of a

statement is the database collation instead of the server collation and

a collation conflict error isn't returned.

A

statement

always creates a single-

threaded insert operation.

A

statement can create a parallel insert operation. When

inserting a large number of rows, the parallel operation can improve

performance.

This section describes new behaviors introduced with compatibility level 110. This section also

applies to compatibility levels above 110.

Expand table

#### Compatibility level setting of 100 or lower

#### Compatibility level setting of at least 110

#### string-length

#### substring

#### string-length

#### substring

#### smalldatetime

#### smalldatetime

#### smalldatetime

#### smalldatetime

#### smalldatetime

Common language runtime (CLR) database

objects are executed with version 4 of the CLR.

However, some behavior changes introduced in

version 4 of the CLR are avoided. For more

information, see

What's new in CLR integration?

CLR database objects are executed with version 4 of

the CLR.

The XQuery functions

and

count each surrogate as two

characters.

The XQuery functions

and

count each surrogate as one character.

is allowed in a recursive common table

expression (CTE) query. However, the query

## returns incorrect results when there are multiple

rows per grouping.

isn't allowed in a recursive common table

expression (CTE) query. An error is returned.

The RC4 algorithm is only supported for

backward compatibility. New material can only

be encrypted using RC4 or RC4_128 when the

database is in compatibility level 90 or 100. (Not

recommended.) In SQL Server 2012 (11.x),

material encrypted using RC4 or RC4_128 can be

decrypted in any compatibility level.

New material can't be encrypted using RC4 or

RC4_128. Use a newer algorithm such as one of the

AES algorithms instead. In SQL Server 2012 (11.x),

material encrypted using RC4 or RC4_128 can be

decrypted in any compatibility level.

The default style for

and

operations on

and

data types is

121 except when either type is used in a

computed column expression. For computed

columns, the default style is 0. This behavior

impacts computed columns when they are

created, used in queries involving auto-

parameterization, or used in constraint

definitions.

Example D in the

## Examples

section shows the

difference between styles 0 and 121. It doesn't

demonstrate the behavior described above. For

more information about

and

styles,

see

CAST and CONVERT

.

Under compatibility level 110, the default style for

and

operations on

and

data types is always 121. If your query relies on the

old behavior, use a compatibility level less than 110,

or explicitly specify the 0 style in the affected query.

Upgrading the database to compatibility level 110

won't change user data that has been stored to disk.

You must manually correct this data as appropriate.

For example, if you used

to create a

table from a source that contained a computed

column expression described above, the data (using

style 0) would be stored rather than the computed

column definition itself. You would need to manually

update this data to match style 121.

The

- (Addition)

operator can be applied to an

operand of type

,

,

, or

if the other operand has type

or

.

Attempting to apply the addition operator to an

operand of type

,

,

, or

and an operand of type

or

will cause error 402.

Any columns in remote tables of type

that are referenced in a

partitioned view are mapped as

.

Corresponding columns in local tables (in the

Any columns in remote tables of type

that are referenced in a partitioned view are mapped

as

. Corresponding columns in local

tables (in the same ordinal position in the select list)

`EXCEPT`

`EXCEPT`

```sql
OUTPUT INTO
```

```sql
IDENTITY_INSERT
SETTING = OFF
```

`IDENTITY_INSERT`

`OFF`

```sql
$action
```

`OUTPUT`

`MERGE`

```sql
$action
```

`MERGE`

```sql
SELECT INTO
```

```sql
SELECT INTO
```

`PIVOT`

`PIVOT`

`CAST`

`CONVERT`

`CAST`

`CONVERT`

```sql
SELECT INTO
```
