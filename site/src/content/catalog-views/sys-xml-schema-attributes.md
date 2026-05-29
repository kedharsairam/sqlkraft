---
name: 'sys.xml_schema_attributes'
title: 'sys.xml_schema_attributes'
category: 'xml'
description: 'Returns a row per XML schema component that is an attribute,'
tags: ["catalog-view", "xml"]
pubDate: 2026-05-29
---

Article

•

11/18/2022

Applies to:

SQL Server


## Returns a row per XML schema component that is an attribute,
of

.


## Description
--

Inherits from

sys.xml_schema_components

.

1 = The default value is a fixed value. This value cannot be overridden

in an XML instance.

0 = The default value is not a fixed value for the attribute. (default)

1 = The attribute must be explicitly namespace qualified.

0 = The attribute may be implicitly namespace qualified. (default)

Default value of the attribute. Is NULL if a default value is not

supplied.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

XML Schemas (XML Type System) Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

ﾉ

Expand table

See Also
