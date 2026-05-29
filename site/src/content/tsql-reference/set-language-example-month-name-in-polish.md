---
name: 'SET LANGUAGE example: Month name in Polish'
title: 'SET LANGUAGE example: Month name in Polish'
category: 'statements'
description: 'Azure SQL Managed Instance'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Code example of SET LANGUAGE

Article

•

11/18/2022

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

Use caution when allowing conversion of your CHARACTER strings into DATE data types. The

reason is that such conversions are often

nondeterministic

.

You control these nondeterministic conversions by accounting for the settings of

SET

LANGUAGE

and

SET DATEFORMAT

.

A character string can be the name of a month. But is the name in English, or Polish, or

Croatian, or in another language? And, will the user's session be set to the correct

corresponding LANGUAGE?

For example, consider the word

listopad

, which is the name of a month. But which month it is

depends on the language the SQL system believes is being used:

If Polish, then

listopad

translates to month 11 (

November

in English).

If Croatian, then

listopad

translates to month 10 (

October

in English).

SQL

### dmy

### mdy

### ymd

### ymd

### ydm

### dmy

### 'dd-mm-yyyy'

### dmy

### mdy

```sql
SET LANGUAGE Polish;
```

```sql
--SELECT alias FROM sys.syslanguages ORDER BY alias;
DECLARE
@yourInputDate
NVARCHAR
(32) =
'28 listopad 2018'
;
SET
LANGUAGE
Polish;
SELECT
CONVERT
(
DATE
, @yourInputDate)
AS
[SL_Polish];
SET
LANGUAGE
Croatian;
SELECT
CONVERT
(
DATE
, @yourInputDate)
AS
[SL_Croatian];
SET
LANGUAGE
English;
/***  Actual output:  For the two months, note the 11 versus the 10.
```
