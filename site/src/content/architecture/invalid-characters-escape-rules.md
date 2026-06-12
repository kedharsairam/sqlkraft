---
title: "Invalid Characters & escape rules"
topic: "xml-data"
description: ""
tags: ["xml-data","invalid-characters-escape-rules"]
pubDate: "2025-12-01"
---

This article describes how invalid XML characters are handled by the FOR XML clause, and lists

the escape rules for characters that are invalid in XML names.

entitizes invalid XML characters when they're returned within FOR XML queries that

don't use the TYPE directive.

Although XML 1.0 conformant parsers raise parse errors regardless of whether these characters

are entitized or not, the entitized form is better aligned with XML 1.1. The entitized form is also

potentially better aligned with future versions of the XML standard. Additionally, it makes

debugging simpler, because the code point of the invalid character becomes visible.

For users of XML tools, no workaround is required, because the XML parser will fail either way

at the point where the invalid characters occur in the data stream. If you use non-XML tools,

this change can require you to update your programming logic to search for these characters

as entitized values.

The following white space characters are entitized differently in FOR XML queries to preserve

their presence through round-tripping:

In element content and attributes:

(carriage return)

In attribute content:

(tab),

(line feed)

These characters are preserved in output, and a parser won't normalize them.

names that contain characters that are invalid in XML names, such as spaces, are

translated into XML names in a way in which the invalid characters are translated into escaped

numeric entity encoding.

There are only two non-alphabetic characters that can occur within an XML name: the colon

(

) and the underscore (

). Because the colon is already reserved for namespaces, the

underscore is chosen as the escape character. Following are the escape rules that are used for

encoding:

```sql
hex(0D) hex(09) hex(0A)
:
_
```
