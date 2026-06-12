---
name: "sys.sp_helplanguage"
title: "sp_helplanguage"
category: "general"
description: "Reports information about a particular alternative language or about all languages in SQL The name of the alternative language for which to display information. is specified, information about the specified language is returned. If language isn't specified, information about all languages in the compatibility view is returned. Langua"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helplanguage [ [ @language = ]
              N
              'language'
              ]
              [ ; ]
---

## Description

Reports information about a particular alternative language or about all languages in SQL The name of the alternative language for which to display information. is specified, information about the specified language is returned. If language isn't specified, information about all languages in the compatibility view is returned. Language identification number.

## Syntax

```sql
sp_helplanguage [ [ @language = ]
N
'language'
]
[ ; ]
```

## Examples

### Example 1

`Italian`

### Example 2

```sql
@@LANGID
```

### Example 3

```sql
@@
LANGID
```

### Example 4

```sql
SET
LANGUAGE
'Italian'
SELECT
@@LANGID
AS
'Language ID'
```

### Example 5

```sql
Changed language setting to Italiano.
Language ID
-----------
6
```

### Example 6

```sql
@@
LANGUAGE
```

### Example 7

```sql
SELECT
@@
LANGUAGE
AS
'Language Name'
;
Language Name
------------------------------
```

### Example 8

`us_english`
