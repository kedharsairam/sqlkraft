---
title: "Examples: Using OPENXML"
topic: "xml-data"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  The examples in this article show how OPENXML is used to create a rowset view of an XML
  
  document. For 
tags:
  - "xml-data"
  - "examples-using-openxml"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The examples in this article show how OPENXML is used to create a rowset view of an XML

document. For information about the syntax of OPENXML, see

OPENXML (Transact-SQL)

. The

examples show all aspects of OPENXML, but don't specify metaproperties in OPENXML. For

more information about how to specify metaproperties in OPENXML, see

Specify

Metaproperties in OPENXML

.

When retrieving the data,

rowpattern

is used to identify the nodes in the XML document that

determine the rows. Additionally,

rowpattern

is expressed in the XPath pattern language that is

used in the MSXML XPath implementation. For example, if the pattern ends in an element or an

attribute, a row is created for each element or attribute node that is selected by

rowpattern

.

The

flags

value provides default mapping. If no

ColPattern

is specified in the

SchemaDeclaration

, the mapping specified in

flags

is assumed. The

flags

value is ignored if

ColPattern

is specified in

SchemaDeclaration

. The specified

ColPattern

determines the mapping,

attribute-centric or element-centric, and also the behavior in dealing with overflow and

unconsumed data.

The XML document in this example is made up of the

,

, and

elements. The OPENXML statement retrieves customer information in a two-column rowset,

and

, from the XML document.

First, the

stored procedure is called to obtain a document handle.

This document handle is passed to OPENXML.

The OPENXML statement illustrates the following:

rowpattern

(/ROOT/Customer) identifies the

nodes to process.

The

flags

parameter value is set to

and indicates attribute-centric mapping. As a result,

the XML attributes map to the columns in the rowset defined in

SchemaDeclaration

.

In

SchemaDeclaration

, in the WITH clause, the specified

ColName

values match the

corresponding XML attribute names. Therefore, the

ColPattern

parameter isn't specified in

SchemaDeclaration

.

```sql
<Customer>
<Order>
<OrderDetail>
<Customer>
```