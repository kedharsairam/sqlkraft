---
name: "SET DATEFORMAT example"
title: "SET DATEFORMAT example"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

## Specific countries/regions

## Code example of SET DATEFORMAT:

## mdy

## versus

## dmy

The preceding

format says that an example date string of '01-03-2018' would be

interpreted to mean

the first day of March in the year 2018.

If instead

was specified, then the same '01-03-2018' string would mean

the third day of

January in 2018.

And if

was specified, there's no guarantee of what the output would be. The numeric

value of '2018' is too large to be a day.

In Japan and China, the DATEFORMAT of

is used. The format's parts are in a sensible

sequence of largest unit to smallest. So, this format sorts well. This format is considered to be

the

international

format. It's international because the four digits of the year are unambiguous,

and no country/region on Earth uses the archaic format of.

In other countries/regions such as Germany and France, the DATEFORMAT is

, meaning. The

format doesn't sort well, but it's a sensible sequence of smallest unit

to largest.

The United States, and the Federated States of Micronesia, are the only countries/regions that

use

, which doesn't sort. The format's mixed sequence matches a pattern of verbal speech

in spoken dates.

The following Transact-SQL code example uses the same date character string with three

different DATEFORMAT settings. A run of the code produces the output shown in the comment:

### ymd

## CONVERT offers explicit codes for

## deterministic

## control of date formats

```sql
SET DATEFORMAT dmy;
```

```sql
SL_Polish
2018-11-28
SL_Croatian
2018-10-28
***/
```

```sql
DECLARE
@yourDateString
NVARCHAR (10) =
'12-09-2018'
;
PRINT @yourDateString + ' = the input.';
```
