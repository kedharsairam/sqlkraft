---
title: "Basic Syntax"
topic: "xml-data"
description: "The FOR XML mode can be RAW, AUTO, EXPLICIT, or PATH. It determines the shape of the resulting XML. F"
tags: ["xml-data","basic-syntax"]
pubDate: "2025-12-01"
---

The FOR XML mode can be RAW, AUTO, EXPLICIT, or PATH. It determines the shape of the

resulting XML.

Following is the basic syntax that is described in

FOR Clause (Transact-SQL).

）

Important

The

directive to the FOR XML option is. Use XSD generation in the

case of RAW and AUTO modes. There is no replacement for the XMLDATA directive in

EXPLICT mode. This feature will be removed in a future version of SQL Server. Avoid using

this feature in new development work, and plan to modify applications that currently use

this feature.

```sql
[
FOR
{
BROWSE
|
<XML>
} ]
<XML>
::=
XML
{
{
RAW
[ (
'ElementName'
) ] |
AUTO
}
[
<CommonDirectives>
[ , {
XMLDATA
|
XMLSCHEMA
[ (
'TargetNameSpaceURI'
) ]} ]
[ ,
ELEMENTS
[
XSINIL
|
ABSENT
]
]
|
EXPLICIT
[
<CommonDirectives>
[ ,
XMLDATA
]
]
|
PATH
[ (
'ElementName'
) ]
[
<CommonDirectives>
[ ,
ELEMENTS
[
XSINIL
|
ABSENT
] ]
]
}
<CommonDirectives>
::=
[ ,
BINARY
BASE
64 ]
```
