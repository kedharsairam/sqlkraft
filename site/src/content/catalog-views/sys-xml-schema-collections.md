---
name: 'sys.xml_schema_collections'
title: 'sys.xml_schema_collections'
category: 'xml'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "xml"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric


## Returns a row per XML schema collection. An XML schema collection is a named set of XSD
definitions. The XML schema collection itself is contained in a relational schema, and it is

identified by a schema-scoped Transact-SQL name. The following tuples are unique:

xml_collection_id, and schema_id and name.


## Description
xml_collection_id

ID of the XML schema collection. Unique within the database.

schema_id

ID of the relational schema that contains this XML schema collection.

principal_id

ID of the individual owner if different from the schema owner. By default,

schema-contained objects are owned by the schema owner. However, an

alternate owner may be specified by using the ALTER AUTHORIZATION

statement to change ownership.

NULL = No alternate individual owner.

name

Name of the XML schema collection.

create_date

Date the XML schema collection was created.

modify_date

Date the XML schema collection was last altered.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Catalog Views (Transact-SQL)

XML Schemas (XML Type System) Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

ﾉ

Expand table

See Also

Last updated on 11/18/2025
