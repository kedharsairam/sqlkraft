---
title: "Example: Retrieving Binary Data"
topic: "xml-data"
description: "The following query returns the product photo stored in a type column. The option is specif"
tags: ["xml-data","example-retrieving-binary-data"]
pubDate: "2025-12-01"
---

The following query returns the product photo stored in a

type column. The

option is specified in the query to return the binary data in base64-encoded

format.

Expect the following result:

XML

Use RAW Mode with FOR XML

```sql
BINARY BASE64
USE
AdventureWorks2022;
GO
SELECT
ProductPhotoID, ThumbNailPhoto
FROM
Production.ProductPhoto
WHERE
ProductPhotoID = 1
FOR
XML
RAW
,
BINARY
BASE64;
GO
<row
ProductModelID
=
"1"
ThumbNailPhoto
=
"base64 encoded binary data"
/>
```
