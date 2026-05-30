---
title: "Requirements & Limitations"
topic: "xml-data"
description: |
  Article

  •

  04/15/2024

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The XML schema definition language (XSD) validation has some limitations regarding SQL

  columns that us
tags:
  - "xml-data"
  - "requirements-limitations"
pubDate: 2025-12-01
---

Article

•

04/15/2024

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The XML schema definition language (XSD) validation has some limitations regarding SQL

columns that use the

data type. The following table provides details about those

limitations and guidelines for modifying your XSD schema so it can work with SQL Server. The

articles in this section provide additional information about specific limitations and guidance

for working with them.

and

The values for

and

attributes must fit into

4-byte integers. Schemas that don't conform are rejected by the

server.

SQL Server rejects schemas that have an

particle

without children, unless the particle is defined with a

attribute value of zero.

Currently, SQL Server doesn't support this element. XML schemas

that include this element are rejected by the server.

As a solution, XML schemas that include the

directive can be preprocessed to copy and merge the contents of

any included schemas into a single schema for upload to the

server. For more information, see

Preprocess a Schema to Merge

Included Schemas

.

,

, and

Currently, SQL Server doesn't support these XSD-based

constraints for enforcing uniqueness or establishing keys and key

references. XML schemas that contain these elements can't be

registered.

SQL Server doesn't support this element. For information about

another way to update schemas, see

The <xsd:redefine> Element

.

values

SQL Server only supports millisecond precision for simple types

that have second components other than

and

, and 100-nanosecond precision for

and

. SQL Server puts limitations on all recognized XSD

simple type enumerations.

ﾉ

Expand table
