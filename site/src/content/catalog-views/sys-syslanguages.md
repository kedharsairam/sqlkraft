---
name: "sys.syslanguages"
title: "sys.syslanguages"
category: "compatibility"
description: "Contains one row for each language present in the instance of SQL Server. for Tuesday, and so on, through Official language name, for example, Alternative language name, for example, Comma-separated list of full-length month names in order from January through December, with each name having up to 20 characters."
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: "SELECT * from dbo.syslanguages;"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains one row for each language present in the instance of SQL Server. for Tuesday, and so on, through Official language name, for example, Alternative language name, for example, Comma-separated list of full-length month names in order from January through December, with each name having up to 20 characters. Comma-separated list of short-month names in order from January

## Syntax

```sql
SELECT * from dbo.syslanguages;
```

## Examples

### Example 1

```sql
SET LANGUAGE Polish;
```

### Example 2

```sql
--SELECT alias FROM sys.syslanguages ORDER BY alias;
DECLARE
@yourInputDate
NVARCHAR (32) =
'28 listopad 2018'
;
SET
LANGUAGE
Polish;
SELECT
CONVERT (
DATE
, @yourInputDate)
AS
[SL_Polish];
SET
LANGUAGE
Croatian;
SELECT
CONVERT (
DATE
, @yourInputDate)
AS
[SL_Croatian];
SET
LANGUAGE
English;
/*** Actual output: For the two months, note the 11 versus the 10.
```
