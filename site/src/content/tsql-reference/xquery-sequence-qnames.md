---
name: "xquery-sequence-qnames"
title: "XQuery - Sequence & QNames"
category: "xquery"
description: "XQuery Language Reference: Sequence & QNames"
syntax: ","
tags: ["xquery","sequence-qnames"]
pubDate: 2025-12-01
---

This topic describes the following fundamental concepts of XQuery:

Sequence

QNames and predefined namespaces

In XQuery, the result of an expression is a sequence that is made up of a list of XML nodes and

instances of XSD atomic types. An individual entry in a sequence is referred to as an item. An

item in a sequence can be either of the following:

A node such as an element, attribute, text, processing instruction, comment, or document

An atomic value such as an instance of an XSD simple type

For example, the following query constructs a sequence of two element-node items:

This is the result:

In the previous query, the comma (

) at the end of the

construction is the sequence

constructor and is required. The white spaces in the results are added for illustration only and

are included in all the example results in this documentation.

Following is additional information that you should know about sequences:

```sql
,
<step1>
SELECT Instructions.query('
<step1> Step 1 description goes here</step1>,
<step2> Step 2 description goes here </step2>
') AS Result
FROM Production.ProductModel
WHERE ProductModelID=7;
<step1> Step 1 description goes here </step1>
<step2> Step 2 description goes here </step2>
```
