---
title: "Create Instances"
topic: "xml-data"
description: "This article describes how to generate XML instances."
tags: ["xml-data","create-instances"]
pubDate: 2025-12-01
---

This article describes how to generate XML instances.

In SQL Server, you can generate XML instances in the following ways:

Type casting string instances.

Using the

statement with the

clause.

Using constant assignments.

Using bulk load.

You can parse any of the SQL Server string data types, such as

,

,

,

, and

, into the

data type by casting (

) or converting (

) the

string to the

data type. Untyped XML is checked to confirm that it's well formed. If there's

a schema associated with the

type, validation is also performed. For more information, see

Compare typed XML to untyped XML.

XML documents can be encoded with different encodings (for example, UTF-8, UTF-16,

Windows-1252). The following outlines the rules on how the string and binary source types

interact with the XML document encoding and how the parser behaves.

Since

assumes a 2-byte Unicode encoding such as UTF-16 or UCS-2, the XML parser

treats the string value as a 2-byte Unicode encoded XML document or fragment. The XML

document needs to be encoded in a 2-byte Unicode encoding as well to be compatible with

the source data type. A UTF-16 encoded XML document can have a UTF-16 byte order mark

(BOM), but it doesn't need to, since the context of the source type makes it clear that it can

only be a 2-byte Unicode encoded document.

The content of a

string is treated as a 1-byte encoded XML document/fragment by the

XML parser. Since the

source string has a code page associated, the parser uses that

code page for the encoding if no explicit encoding is specified in the XML itself. If an XML

instance has a BOM or an encoding declaration, the BOM or declaration needs to be consistent

with the code page, otherwise the parser reports an error.

The content of

is treated as a codepoint stream that is passed directly to the XML

parser. Thus, the XML document or fragment needs to provide the BOM or other encoding

information inline. The parser only looks at the stream to determine the encoding. This means

```sql
SELECT
FOR XML
CAST
CONVERT
```
