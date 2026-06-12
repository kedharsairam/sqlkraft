---
title: "Timestamp Data Type"
topic: "xml-data"
description: "In the transformation, type values are treated as data, and is always Base64 encoded. The"
tags: ["xml-data","timestamp-data-type"]
pubDate: "2025-12-01"
---

In the

transformation,

type values are treated as

data, and is

always Base64 encoded. The XML Schema Definition (XSD) or XML-Data Reduced (XDR)

schema, if requested, reflects this type.

Here's the result set.

XML

FOR XML support for various SQL Server data types

```sql
FOR XML
DROP
TABLE t;
GO
CREATE
TABLE t (
c1
INT
,
c2
TIMESTAMP
);
GO
INSERT t
VALUES (1,
NULL
);
GO
SELECT
*
FROM t
FOR
XML
AUTO
, XMLDATA;
GO
<Schema name
=
"Schema1"
xmlns
=
"urn:schemas-microsoft-com:xml-data"
xmlns:dt
=
"urn:schemas-microsoft-com:datatypes"
>
<ElementType name
=
"t"
content
=
"empty"
model
=
"closed"
>
<AttributeType name
=
"c1"
dt:type
=
"i4"
/>
<AttributeType name
=
"c2"
dt:type
=
"bin.base64"
/>
<attribute type
=
"c1"
/>
<attribute type
=
"c2"
/>
</ElementType>
</Schema>
<t xmlns
=
"x-schema:#Schema1"
c1
=
"1"
c2
=
"AAAAAAAACGE="
/>
```
