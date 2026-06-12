---
title: "XML schema collections"
topic: "ssms"
description: "ﾃ Summarize this article for me SQL database projects support automatic generation of XML s"
tags: ["ssms","xml-schema-collections"]
pubDate: "2025-12-01"
---

ﾃ

Summarize this article for me

SQL database projects support automatic generation of XML schema collection objects from

XSD (XML Schema Definition) files. When you include an XSD file in your project with the

appropriate metadata, the build process creates a

statement

that you can use to enforce XML data validation in your database.

XML schema collections provide typed XML columns in SQL Server, enabling the database

engine to validate XML data against defined schemas and optimize query performance.

To generate an XML schema collection from an XSD file, add a

item to your project file

(

) with two required metadata elements:

: The database schema where the XML schema collection is created (for

example,

)

: The name of the resulting XML schema collection object in

the database

The following example shows how to configure an XSD file in a SQL project:

```cmd
CREATE XML SCHEMA COLLECTION
Build.sqlproj dbo
<?xml version="1.0" encoding="utf-8"?>
<Project
DefaultTargets
=
"Build"
>
<Sdk
Name
=
"Microsoft.Build.Sql"
Version
=
"2.1.0"
/>
<PropertyGroup>
<Name>
MyDatabase
</Name>
<DSP>
Microsoft.Data.Tools.Schema.Sql.Sql170DatabaseSchemaProvider
</DSP>
<ModelCollation>
1033, CI
</ModelCollation>
</PropertyGroup>
<ItemGroup>
<Build
Include
=
"OrderSchema.xsd"
>
<RelationalSchema>
dbo
</RelationalSchema>
<XMLSchemaCollectionName>
OrderSchemaCollection
</XMLSchemaCollectionName>
</Build>
</ItemGroup>
</Project>
```
