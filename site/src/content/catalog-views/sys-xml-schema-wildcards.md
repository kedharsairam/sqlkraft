---
name: "sys.xml_schema_wildcards"
title: "sys.xml_schema_wildcards"
category: "xml"
description: "Returns a row per XML schema component that is an Attribute-Wildcard ( Indicates how contents are processed. S = Strict validation (must validate) L = Lax validation (validate if possible) Description of how contents are processed: sys.xml_schema_wildcard_namespaces 1 = Namespaces are the only ones disallowed."
tags: ["xml", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns a row per XML schema component that is an Attribute-Wildcard ( Indicates how contents are processed. S = Strict validation (must validate) L = Lax validation (validate if possible) Description of how contents are processed: sys.xml_schema_wildcard_namespaces 1 = Namespaces are the only ones disallowed. The visibility of the metadata in catalog views is limited to securables that a user either owns,

## Permissions

Article • 02/28/2023 Applies to: SQL Server Returns a row per XML schema component that is an Attribute-Wildcard ( of ) or Element-Wildcard ( of ), both with of . Description Inherits columns from sys.xml_schema_components . Indicates how contents are processed. S = Strict validation (must validate) L = Lax validation (validate if possible) P = Skip validation Description of how contents are processed: 0 = Namespaces enumerated in sys.xml_schema_wildcard_namespaces are the only ones allowed. 1 = Namespaces are the only ones disallowed. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Catalog Views (Transact-SQL) XML Schemas (XML Type System) Catalog Views (Transact-SQL) ﾉ Expand table See Also
