---
title: "Add Business Logic"
topic: "xml-data"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Your business logic can be added to XML data in several ways:

  You can write row or column constraints to enforce domain-specific c
tags:
  - "xml-data"
  - "add-business-logic"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Your business logic can be added to XML data in several ways:

You can write row or column constraints to enforce domain-specific constraints during

insertion and modification of XML data.

You can write a trigger on the XML column that fires when you insert or update values in

the column. The trigger can contain domain-specific validation rules or populate property

tables.

The Database Engine includes the ability to execute managed code. You can use this

common language runtime (CLR) integration to write functions in managed code to

which you pass XML values, and use XML processing capabilities provided by the

System.Xml namespace. An example is to apply XSL transformation to XML data.

Alternatively, you can deserialize the XML into one or more managed classes and operate

on them by using managed code.

You can write Transact-SQL stored procedures and functions that start the processing on

the XML column for your business needs.

Consider a CLR function

that accepts an

data type instance and an XSL

transformation stored in a file, applies the transformation to the XML data, and then returns

the transformed XML in the result. Following is a skeleton function that is written in C#:

C#

```sql
TransformXml()
public
static
SqlXml
TransformXml
(SqlXml XmlData,
string
xslPath) {
// Load XSL transformation
XslCompiledTransform xform =
new
XslCompiledTransform();
XPathDocument xslDoc =
new
XPathDocument (xslPath);
xform.Load(xslDoc);
// Load XML data
XPathDocument xDoc =
new
XPathDocument (XmlData.CreateReader());
// Return the transformed value
MemoryStream xsltResult =
new
MemoryStream();
xform.Transform(xDoc,
null
, xsltResult);
SqlXml retSqlXml =
new
SqlXml(xsltResult);
```
