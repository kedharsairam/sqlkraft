---
title: "Generate an Inline XDR Schema"
topic: "xml-data"
description: "The directive in FOR XML returns an inline XDR schema together with the query result. Howev"
tags: ["xml-data","generate-an-inline-xdr-schema"]
pubDate: "2025-12-01"
---

The

directive in FOR XML returns an inline XDR schema together with the query

result. However, the XDR schema doesn't support all the new data types and other

enhancements introduced in SQL Server 2005 (9.x) and later versions. Instead, you can request

an inline XSD schema by using

the XMLSCHEMA directive.

Also note the following about the inline XDR schema support:

If the FOR XML query result includes columns of

type and you request an inline XDR

schema, an error is returned. Inline XDR doesn't support these types.

The

and

types will be mapped to

and

, respectively.

When compatibility mode is set to 90 or higher,

values are considered as

data, are treated like binary data, and are returned in the result as follows:

Base 64 encoding is used when

is specified.

URL encoding is used in AUTO mode when

isn't specified.

）

Important

The XMLDATA directive to the FOR XML option is deprecated. Use XSD generation in the

case of RAW and AUTO modes. There is no replacement for the XMLDATA directive in

EXPLICIT mode. This feature will be removed in a future version of SQL Server. Avoid using

this feature in new development work, and plan to modify applications that currently use

this feature.
