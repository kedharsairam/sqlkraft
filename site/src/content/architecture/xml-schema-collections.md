---
title: "XML Schema Collections"
topic: "xml-data"
description: ""
tags: ["xml-data","xml-schema-collections"]
pubDate: "2025-12-01"
---

As described in the

xml (Transact-SQL)

article, SQL Server provides native storage of XML data

through the

data type. You can optionally associate XSD schemas with a variable or a

column of

type through an XML schema collection. The XML schema collection stores the

imported XML schemas and is then used to do the following:

Validate XML instances

Type the XML data as it is stored in the database

The XML schema collection is a metadata entity like a table in the database. You can create,

modify, and drop them. Schemas specified in a

CREATE XML SCHEMA COLLECTION (Transact-

SQL)

statement are automatically imported into the newly created XML schema collection

object. You can import additional schemas or schema components into an existing collection

object in the database by using the

ALTER XML SCHEMA COLLECTION (Transact-SQL)

statement.

As described in the article,

Typed vs. Untyped XML

, the XML stored in a column or variable that

a schema is associated with is referred to as

XML, because the schema provides the

necessary data type information for the instance data. SQL Server uses this type information to

optimize data storage.

The query-processing engine also uses the schema for type checking and to optimize queries

and data modification.

Also, SQL Server uses the associated XML schema collection, with typed

, to validate the

XML instance. If the XML instance complies with the schema, the database allows the instance

to be stored in the system with their type information. Otherwise, it rejects the instance.

You can use the intrinsic function XML_SCHEMA_NAMESPACE to retrieve the schema collection

that is stored in the database. For more information, see

View a Stored XML Schema Collection.

You can also use the XML schema collection to type XML variables, parameters, and columns.

You can create XML schema collections in the database and associate them with variables and

columns of

type. To manage schema collections in the database, SQL Server provides the

following DDL statements:
