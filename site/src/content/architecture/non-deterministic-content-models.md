---
title: "Non-Deterministic content models"
topic: "xml-data"
description: ""
tags: ["xml-data","non-deterministic-content-models"]
pubDate: 2025-12-01
---

Non-deterministic content models are accepted in SQL Server if the occurrence constraints are

0, 1, or unbounded.

Before SQL Server 2005 (9.x) Service Pack 1 (SP1), SQL Server rejected XML schemas that had

non-deterministic content models.

The following example attempts to create an XML schema with a non-deterministic content

model. The code fails because it isn't clear whether the

element should have a

sequence of two

elements or if the

element should have two sequences, each with

an

element.

The schema can be fixed by moving the occurrence constraint to a unique location. For

example, the constraint can be moved to the containing sequence particle:

XML

Or the constraint can be moved to the contained element:

```sql
<root>
<a>
<root>
<a>
CREATE
XML
SCHEMA
COLLECTION MyCollection
AS
'
<schema xmlns="http://www.w3.org/2001/XMLSchema">
<element name="root">
<complexType>
<sequence minOccurs="1" maxOccurs="2">
<element name="a" type="string" minOccurs="1" maxOccurs="2"/>
</sequence>
</complexType>
</element>
</schema>
'
;
GO
<sequence minOccurs
=
"1"
maxOccurs
=
"4"
>
<element name
=
"a"
type
=
"string"
minOccurs
=
"1"
maxOccurs
=
"1"
/>
</sequence>
```
