---
title: "EXPLICIT Mode"
topic: "xml-data"
description: "As described in the article, Constructing XML Using FOR XML , RAW and AUTO mode don't provide much c"
tags: ["xml-data","explicit-mode"]
pubDate: 2025-12-01
---

As described in the article,

Constructing XML Using FOR XML

, RAW and AUTO mode don't

provide much control over the shape of the XML generated from a query result. However,

EXPLICIT mode provides the most flexibility in generating the XML you want from a query

result.

The EXPLICIT mode query must be written in a specific way so that the additional information

about the required XML, such as expected nesting in the XML, is explicitly specified as part of

the query. Depending on the XML you request, writing EXPLICIT mode queries can be

cumbersome. You may find that

Using PATH Mode

with nesting is a simpler alternative to

writing EXPLICIT mode queries.

Because you describe the XML you want as part of the query in EXPLICIT mode, you must

ensure that the generated XML is well formed and valid.

The EXPLICIT mode transforms the rowset that results from the query execution into an XML

document. In order for EXPLICIT mode to produce the XML document, the rowset must have a

specific format. This requires that you write the SELECT query to produce the rowset, the

, with a specific format so the processing logic can then produce the XML you

want.

First, the query must produce the following two metadata columns:

The first column must provide the tag number, integer type, of the current element, and

the column name must be. Your query must provide a unique tag number for each

element that will be constructed from the rowset.

The second column must provide a tag number of the parent element, and this column

name must be. In this way, the Tag and the Parent column provide hierarchy

information.

These metadata column values, together with the information in the column names, are used

to produce the XML you want. Your query must provide column names in a specific way. Also

note that a 0 or NULL in the

column indicates that the corresponding element has no

parent. The element is added to the XML as a top-level element.
