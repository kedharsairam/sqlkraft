---
name: "xquery-functions-related-to-qnames-expanded-qname"
title: "XQuery - Functions Related to QNames - expanded-QName"
category: "xquery"
description: "XQuery Language Reference: Functions Related to QNames - expanded-QName"
syntax: "<e> expanded-QName(...) </e>"
tags: ["xquery","functions-related-to-qnames-expanded-qname"]
pubDate: "2025-12-01"
---

Returns a value of the xs:QName type with the namespace URI specified in the

$paramURI

and

the local name specified in the

$paramLocal. If

$paramURI

is the empty string or the empty

sequence, it represents no namespace.

$paramURI

Is the namespace URI for the QName.

$paramLocal

Is the local name part of the QName.

The following applies to the

function:

If the

$paramLocal

value specified is not in the correct lexical form for xs:NCName type,

the empty sequence is returned and represents a dynamic error.

Conversion from xs:QName type to any other type is not supported in SQL Server.

Because of this, the

function cannot be used in XML construction.

For example, when you are constructing a node, such as

,

the value has to be untyped. This would require that you convert the xs:QName type

value returned by

to xdt:untypedAtomic. However, this is not

supported. A solution is provided in an example later in this topic.

```sql
<e> expanded-QName(.) </e>
expanded-QName() fn:expanded-QName($paramURI as xs:string?, $paramLocal as xs:string?) as xs:QName?
```
