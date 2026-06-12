---
title: "Unique particle attribution constraint"
topic: "xml-data"
description: ""
tags: ["xml-data","unique-particle-attribution-constraint"]
pubDate: 2025-12-01
---

In XSD, complex content models are constrained by the unique particle attribution (UPA)

constraint rule. This rule requires that each element in an instance document corresponds

unambiguously to exactly one

or

particle in its parent's content

model. Any schema that contains a type with a potentially ambiguous content model is

rejected.

The most common causes of ambiguity are

wildcard characters and particles that

have variable occurrence ranges, such as minOccurs < maxOccurs. For example, the following

content model is ambiguous, because an

element could match either the

or the

element.

XML

The following content model is also ambiguous:

XML

Although a document such as

can be validated unambiguously,

a document such as

can't, because it isn't clear which

the second

is referring to. Even though some documents can be validated

unambiguously, the schema will be rejected, because of the potential for ambiguity.

```sql
<xsd:element>
<xsd:any>
<xsd:any>
<e1>
<xsd:element>
<xsd:any>
<root><e1/><e2/><e1/></root>
<root><e1/><e1/></root>
<xsd:element>
<e1/>
<xsd:element name
=
"root"
>
<xsd:complexType>
<xsd:choice>
<xsd:element name
=
"e1"
/>
<xsd:any namespace
=
"##any"
/>
</xsd:choice>
</xsd:complexType>
</xsd:element>
<xsd:element name
=
"root"
>
<xsd:complexType>
<xsd:sequence>
<xsd:element name
=
"e1"
maxOccurs
=
"2"
/>
<xsd:element name
=
"e2"
minOccurs
=
"0"
/>
<xsd:element name
=
"e1"
/>
</xsd:sequence>
</xsd:complexType>
</xsd:element>
```
