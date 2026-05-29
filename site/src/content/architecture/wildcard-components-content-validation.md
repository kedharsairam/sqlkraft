---
title: "Wildcard components & content validation"
topic: "xml-data"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  Wildcard components are used to increase flexibility in what is allowed to appear in a content
  
  model. 
tags:
  - "xml-data"
  - "wildcard-components-content-validation"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Wildcard components are used to increase flexibility in what is allowed to appear in a content

model. These components are supported in the XSD language in the following ways:

Element wildcard components. These are represented by the

element.

Attribute wildcard components. These are represented by the

element.

Both wildcard character elements,

and

, support the use of a

attribute. This lets you specify a value that indicates how XML applications

handle the validation of document content associated with these wildcard character elements.

These are the different values and their effect:

The

value specifies that the contents are fully validated.

The

value specifies that the contents aren't validated.

The

value specifies that only elements and attributes for which schema definitions are

available are validated.

The XML Schema specification uses

validation for elements of the

type. Because

SQL Server 2005 (9.x) didn't support lax validation, strict validation was applied for elements of

the

. Beginning with SQL Server 2008 (10.0.x), lax validation is supported. Content of

elements of type

will be validated using lax validation.

The following example illustrates the lax validation. The schema element

is of the

type. The example creates typed

variables and illustrates the lax validation of the element

of the

type.

SQL

```sql
<xsd:any>
<xsd:anyAttribute>
<xsd:any>
<xsd:anyAttribute>
processContents
e
CREATE
XML
SCHEMA
COLLECTION SC
AS
'
<schema xmlns="http://www.w3.org/2001/XMLSchema"
targetNamespace="http://ns">
<element name="e" type="anyType"/>
<element name="a" type="byte"/>
```