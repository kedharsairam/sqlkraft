---
name: "sys.parameter_type_usages"
title: "sys.parameter_type_usages"
category: "compatibility"
description: "Returns one row for each parameter that is of user-defined type. ID of the object to which this parameter belongs. ID of the parameter. Is unique within the object. To return the name of the type, join to the role. For more information, see Scalar Types Catalog Views (Transact-SQL) This view does not return rows for parameters of numbered procedures."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns one row for each parameter that is of user-defined type. ID of the object to which this parameter belongs. ID of the parameter. Is unique within the object. To return the name of the type, join to the role. For more information, see Scalar Types Catalog Views (Transact-SQL) This view does not return rows for parameters of numbered procedures.

## Permissions

Article • 02/28/2023 Applies to: SQL Server Returns one row for each parameter that is of user-defined type. Description ID of the object to which this parameter belongs. ID of the parameter. Is unique within the object. ID of the user-defined type. To return the name of the type, join to the sys.types catalog view on this column. Requires membership in the role. For more information, see Metadata Visibility Configuration . Scalar Types Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) ７ Note This view does not return rows for parameters of numbered procedures. ﾉ Expand table See Also
