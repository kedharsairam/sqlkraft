---
name: "COLLATIONPROPERTY"
title: "COLLATIONPROPERTY"
category: "statements"
description: "Returns information about a specified collation."
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---
## Syntax

```sql
COLLATIONPROPERTY ( 'collation_name' , 'property' )
```

## Return Type

sql_variant

## Property Descriptions

| Property | Return Type | Description |
|----------|-------------|-------------|
| CodePage | int | Code page of the collation. |
| LCID | int | Windows LCID of the collation. |
| ComparisonStyle | int | Windows comparison style of the collation. |
| Version | int | Version of the collation. |
| SortOrder | tinyint | Sort order ID of the collation (SQL Server collations only). |

## Remarks

Returns information about a specified collation.

## Example

```sql
SELECT COLLATIONPROPERTY('database_name', 'CodePage') AS CodePage;
```
