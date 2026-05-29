---
title: "Preprocess a schema to merge included schemas"
topic: "xml-data"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The W3C XSD
  
  element provides support for schema modularity in which an XML
  
  schema can be pa
tags:
  - "xml-data"
  - "preprocess-a-schema-to-merge-included-schemas"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The W3C XSD

element provides support for schema modularity in which an XML

schema can be partitioned into more than one physical file. SQL Server currently doesn't

support this element. XML schemas that include this element will be rejected by the server.

As a solution, XML schemas that include the

directive can be preprocessed to

copy and merge the contents of any included schemas into a single schema for uploading to

the server. The following C# code can be used for the preprocessing. The comments in the

early part of the code provide information about how to use it.

C#

```sql
<xsd:include>
// XSD Schema Include Normalizer
// To compile:
// csc filename.cs
//
// How to use:
//
// Arguments: [-q] input.xsd [output.xsd]
//
// input.xsd       - file to normalize
// output.xsd      - file to output, default is console
// -q              - quiet
//
// Example:
//
// filename.exe schema.xsd
//
using
System;
using
System.Xml;
using
System.Xml.Schema;
using
System.IO;
using
System.Collections;
public
class
XsdSchemaNormalizer
{
private
static
bool
NormalizeXmlSchema
( String url, TextWriter writer )
{
try
{
XmlTextReader txtRead =
new
XmlTextReader( url );
XmlSchema sch = XmlSchema.Read( txtRead,
null
);
// Compiling Schema
sch.Compile(
null
);
```