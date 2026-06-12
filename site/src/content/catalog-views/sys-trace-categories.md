---
name: "sys.trace_categories"
title: "sys.trace_categories"
category: "compatibility"
description: "Similar event classes are grouped by a category. Each row in the view identifies a category that is unique across the server. These categories do not change for a given version of the SQL Server Database Engine. For a complete list of supported trace events, see SQL Server Event Class Reference Unique ID of this category. This column is also in the Unique name of this category. This parameter is n"
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
---

## Description

Similar event classes are grouped by a category. Each row in the view identifies a category that is unique across the server. These categories do not change for a given version of the SQL Server Database Engine. For a complete list of supported trace events, see SQL Server Event Class Reference Unique ID of this category. This column is also in the Unique name of this category. This parameter is not localized.

## Permissions

Article • 02/28/2023 Each row in the catalog view identifies a category that is unique across the server. These categories do not change for a given version of the SQL Server Database Engine. For a complete list of supported trace events, see SQL Server Event Class Reference. Description Unique ID of this category. This column is also in the catalog view. Unique name of this category. This parameter is not localized. Category type: 0 = Normal 1 = Connection 2 = Error The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Event catalog views instead. ﾉ Expand table See Also Article • 02/28/2023 The catalog view contains a list of all SQL trace events. These trace events do not change for a given version of the SQL Server Database Engine. For more information about these trace events, see SQL Server Event Class Reference. Description Unique ID of the event. This column is also in the and catalog views. Category ID of the event. This column is also in the catalog view. Unique name of this event. This parameter is not localized. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. Object Catalog Views (Transact-SQL) sys.traces (Transact-SQL) sys.trace_categories (Transact-SQL) sys.trace_columns (Transact-SQL) ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Event catalog views instead. ﾉ Expand table See also
