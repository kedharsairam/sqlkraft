---
title: "Large object (LOB) parameters"
topic: "clr-integration"
description: "Use and to pass large object (LOB) binary type ( ) and LOB character type ( ) parameters, respectively."
tags: ["clr-integration","large-object-lob-parameters"]
pubDate: "2025-12-01"
---

Use

and

to pass large object (LOB) binary type (

) and LOB

character type (

) parameters, respectively. These types allow streaming the LOB

values from the database to the common language runtime (CLR) routine, instead of copying

the entire value into managed space.

and

should be used only for small

binary and character string values.

data types in the.NET Framework

```sql
SqlBytes
SqlChars
SqlBinary
SqlString
```
