---
name: "sys.fn_helpcollations"
title: "sys.fn_helpcollations"
category: "system"
description: "To list the SQL Server collations supported by your server, execute the following query. CREATE DATABASE DECLARE @local_variable sys.fn_helpcollations For Sort Order ID 80, use any of the Window collations with the code page of 1250, and binary order. For example: Albanian_BIN, Croatian_BIN, Czech_BIN, Romanian_BIN, Slovak_BIN, Slovenian_BIN."
tags: ["system","function"]
pubDate: "2026-05-29"
syntax: |
  SELECT
    Name
    , Description
    FROM
    fn_helpcollations()
    WHERE
    Name
    like
    'L%'
    AND
    Description
    LIKE
    '% binary sort'
    ;
    Name                   Description
    Lao_100_BIN            Lao-100, binary sort
    Latin1_General_BIN     Latin1-General, binary sort
    Latin1_General_100_BIN Latin1-General-100, binary sort
    Latvian_BIN            Latvian, binary sort
    Latvian_100_BIN        Latvian-100, binary sort
    Lithuanian_BIN         Lithuanian, binary sort
    Lithuanian_100_BIN     Lithuanian-100, binary sort
    (7 row(s) affected)
---

## Description

To list the SQL Server collations supported by your server, execute the following query. CREATE DATABASE DECLARE @local_variable sys.fn_helpcollations For Sort Order ID 80, use any of the Window collations with the code page of 1250, and binary order. For example: Albanian_BIN, Croatian_BIN, Czech_BIN, Romanian_BIN, Slovak_BIN, Slovenian_BIN.

## Syntax

```sql
SELECT
Name
, Description
FROM fn_helpcollations()
WHERE
Name like
'L%'
AND
Description
LIKE
'% binary sort'
;
Name Description
------------------- ------------------------------------
Lao_100_BIN Lao-100, binary sort
Latin1_General_BIN Latin1-General, binary sort
Latin1_General_100_BIN Latin1-General-100, binary sort
Latvian_BIN Latvian, binary sort
Latvian_100_BIN Latvian-100, binary sort
Lithuanian_BIN Lithuanian, binary sort
Lithuanian_100_BIN Lithuanian-100, binary sort (7 row(s) affected)
```

## Remarks

To list the SQL Server collations supported by your server, execute the following query.

ALTER TABLE

CREATE DATABASE

CREATE TABLE

DECLARE @local_variable

sys.fn_helpcollations

For Sort Order ID 80, use any of the Window collations with the code page of 1250, and

binary order. For example: Albanian_BIN, Croatian_BIN, Czech_BIN, Romanian_BIN,

Slovak_BIN, Slovenian_BIN.

## Examples

### Example 1

```sql
L
```

### Example 2

```sql
fn_helpcollations ()
```

### Example 3

```sql
SELECT
Name
, Description
FROM fn_helpcollations()
WHERE
Name like
'L%'
AND
Description
LIKE
'% binary sort'
;
Name Description
------------------- ------------------------------------
Lao_100_BIN Lao-100, binary sort
Latin1_General_BIN Latin1-General, binary sort
Latin1_General_100_BIN Latin1-General-100, binary sort
Latvian_BIN Latvian, binary sort
Latvian_100_BIN Latvian-100, binary sort
Lithuanian_BIN Lithuanian, binary sort
Lithuanian_100_BIN Lithuanian-100, binary sort (7 row(s) affected)
```

### Example 4

```sql
SELECT name
,
description
FROM fn_helpcollations();
```
