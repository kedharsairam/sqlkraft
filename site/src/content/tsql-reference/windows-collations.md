---
name: "Windows collations"
title: "Windows collations"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Description

Collation uses the Latin1 General dictionary sorting rules and maps to

code page

. It's a version

collation, and is case-insensitive

(

) and accent-sensitive (

).

Collation uses the Estonian dictionary sorting rules and maps to code

page

. It's a version

collation (implied by no version number

in the name), and is case-sensitive (

) and accent-sensitive (

).

Collation uses binary code point sorting rules and maps to code page

. It's a version

collation, and the Japanese Bushu Kakusu

dictionary sorting rules are ignored.

To list the Windows collations supported by your instance of SQL Server, execute the following

query.

Collation and Unicode support

ALTER TABLE (Transact-SQL)

Constants (Transact-SQL)

CREATE DATABASE

CREATE TABLE (Transact-SQL)

DECLARE @local_variable (Transact-SQL)

Table (Transact-SQL)

sys.fn_helpcollations

Last updated on 11/18/2025

Related content

`Latin1_General_100_CI_AS`

```sql
1252
```

```sql
_100
```

`CI`

`AS`

`Estonian_CS_AS`

```sql
1257
```

```sql
_80
```

`CS`

`AS`

`Japanese_Bushu_Kakusu_140_BIN2`

```sql
932
```

```sql
_140
```

```sql
SELECT
*
FROM sys.fn_helpcollations()
WHERE
[
name
]
NOT
LIKE
N
'SQL%'
;
```
