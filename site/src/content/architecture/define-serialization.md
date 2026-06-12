---
title: "Define serialization"
topic: "xml-data"
description: ""
tags: ["xml-data","define-serialization"]
pubDate: 2025-12-01
---

When casting the

data type explicitly or implicitly to a SQL string or binary type, the

content of the

data type will be serialized according to the rules outlined in this article.

If the SQL target type is VARBINARY, the result is serialized in UTF-16 with a UTF-16-byte order

mark in front, but without an XML declaration. If the target type is too small, an error is raised.

For example:

This is the result:

Console

If the SQL target type is NVARCHAR or NCHAR, the result is serialized in UTF-16 without the

byte order mark in front and without an XML declaration. If the target type is too small, an

error is raised.

For example:

This is the result:

Console

If the SQL target type is VARCHAR or CHAR, the result is serialized in the encoding that

corresponds to the database's collation code page without a byte order mark or XML

```sql
select
CAST (
CAST (N
'<Δ/>'
as
XML
) as
VARBINARY(
MAX
))
0xFFFE3C0094032F003E00 select
CAST (
CAST (N
'<Δ/>'
as
XML
) as
NVARCHAR (
MAX
))
<Δ/>
```
