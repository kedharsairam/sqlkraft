---
title: "Use the BINARY BASE64 Option"
topic: "xml-data"
description: "If the BINARY BASE64 option is specified in the query, the binary data is returned in base64 encoding"
tags: ["xml-data","use-the-binary-base64-option"]
pubDate: "2025-12-01"
---

If the BINARY BASE64 option is specified in the query, the binary data is returned in base64

encoding format.

If the BINARY BASE64 option isn't specified in the query, then by default, AUTO mode supports

URL encoding of binary data. A reference to a relative URL to the virtual root of the database is

returned. This reference is to the database where the query was executed. The returned

reference can be used to access the actual binary data in subsequent operations. This access is

achieved by using the SQLXML ISAPI

query. The query must provide enough

information to identify the image. Such information might include the columns of the primary

key.

Don't use an alias for a binary column when you query a view and using the FOR XML AUTO

mode. If you use an alias, the alias is returned in the URL encoding of the binary data. In

subsequent operations, the alias is meaningless. The meaningless alias and the URL encoding

can't be used to retrieve the image.

In a SELECT query, casting any column to a binary large object (BLOB) makes the column a

temporary entity. Being temporary, the BLOB loses its associated table name and column

name. This cast causes AUTO mode queries to generate an error, because the system doesn't

know where to put this value in the XML hierarchy.

For example, consider the following table with its one row.

The following query produces an error, which is caused by the casting to a binary large object

(BLOB):

```sql
dbobject
CREATE
TABLE
MyTable (Col1 int
PRIMARY
KEY
, Col2 binary
)
INSERT
INTO
MyTable
VALUES (1, 0x7);
```
