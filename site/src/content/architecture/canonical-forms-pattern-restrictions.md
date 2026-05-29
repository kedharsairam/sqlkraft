---
title: "Canonical forms & pattern restrictions"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The XSD pattern facet allows for the restriction of the lexical space of simple types. When a
tags:
  - "xml-data"
  - "canonical-forms-pattern-restrictions"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The XSD pattern facet allows for the restriction of the lexical space of simple types. When a

pattern restriction is put on a type for which there's more than one possible lexical

representation, some values could cause unexpected behavior upon validation.

This behavior occurs because lexical representations of these values aren't stored in the

database. Therefore, the values are converted to their canonical representations when

serialized as output. If a document contains a value whose canonical form doesn't comply with

the pattern restriction for its type, the document is rejected if a user tries to reinsert it.

To prevent this, SQL Server rejects any XML document that contains values that can't be

reinserted, because of the violation of pattern restrictions by their canonical forms. For

example, the value "33.000" doesn't validate against a type derived from

with a

pattern restriction of "33\.0+". Although "33.000" complies with this pattern, the canonical

form, "33", doesn't.

Therefore, you should be careful when you apply pattern facets to types derived from the

following primitive types:

,

,

,

,

,

,

,

,

and

. SQL Server issues a warning when you add any such components to a

schema collection.

Imprecise serialization of floating-point values has a similar problem. Because of the floating-

point serialization algorithm used by SQL Server, it's possible for similar values to share the

same canonical form. When a floating-point value is serialized and then reinserted, its value

may change slightly. In rare cases, this may result in a value that violates any of the following

facets for its type on reinsertion:

,

,

,

, or

. To prevent this, SQL Server rejects any values of types derived from

or

that can't be serialized and reinserted.

Requirements and Limitations for XML Schema Collections on the Server

Last updated on 11/18/2025

```sql
xs:float
xs:double
```
