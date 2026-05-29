---
title: "Compare Typed to Untyped XML"
topic: "xml-data"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  You can create variables, parameters, and columns of the
  
  type. You can optionally
  
  associate a collect
tags:
  - "xml-data"
  - "compare-typed-to-untyped-xml"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

You can create variables, parameters, and columns of the

type. You can optionally

associate a collection of XML schemas with a variable, parameter, or column of

type. In this

case, the

data type instance is called

typed

. Otherwise, the XML instance is called

untyped

.

The

data type implements the ISO standard

data type. Therefore, it can store well-

formed XML version 1.0 documents and also so-called XML content fragments with text nodes

and an arbitrary number of top-level elements in an untyped XML column. The system checks

that the data is well-formed, doesn't require the column to be bound to XML schemas, and

rejects data that isn't well-formed in the extended sense. This is true also of untyped XML

variables and parameters.

An XML schema provides the following:

Whenever a typed xml instance is assigned to or modified, SQL

Server validates the instance.

Schemas provide information about the types of attributes and

elements in the

data type instance. The type information provides more precise

operational semantics to the values contained in the instance than is possible with

untyped

. For example, decimal arithmetic operations can be performed on a decimal

value, but not on a string value. Because of this, typed XML storage can be made

significantly more compact than untyped XML.

Use untyped

data type in the following situations:

You don't have a schema for your XML data.

You have schemas, but you don't want the server to validate the data. This is sometimes

the case when an application performs client-side validation before storing the data at