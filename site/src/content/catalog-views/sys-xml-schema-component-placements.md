---
name: "sys.xml_schema_component_placements"
title: "sys.xml_schema_component_placements"
category: "xml"
description: "Returns a row per placement for XML schema components."
tags: ["xml", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns a row per placement for XML schema components. ID of the XML schema component that owns this ID of the placement. This is unique within the owning XML ID of the placed XML schema component. 1 = The default value is a fixed value. This value cannot be overridden in an XML instance. 0 = The value can be overridden.(default) Minimum number of placed component occurs. Maximum number of placed component occurs.

## Permissions

Article • 02/28/2023 Applies to: SQL Server Returns a row per placement for XML schema components. Description ID of the XML schema component that owns this placement. ID of the placement. This is unique within the owning XML schema component. ID of the placed XML schema component. 1 = The default value is a fixed value. This value cannot be overridden in an XML instance. 0 = The value can be overridden.(default) Minimum number of placed component occurs. Maximum number of placed component occurs. Default value if one is supplied. Is NULL if a default value is not supplied. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Catalog Views (Transact-SQL) XML Schemas (XML Type System) Catalog Views (Transact-SQL) ﾉ Expand table See Also
