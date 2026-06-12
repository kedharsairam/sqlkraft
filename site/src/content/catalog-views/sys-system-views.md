---
name: "sys.system_views"
title: "sys.system_views"
category: "objects"
description: "Contains one row for each system view that is shipped with SQL Server. All system views are contained in the schemas named For a list of columns that this view inherits, see 1 = View has a replication filter. 1 = VIEW_METADATA option specified for view. For more 1 = Table contains persisted data that depends on an assembly whose definition changed during the last ALTER ASSEMBLY. Will be reset to 0"
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Contains one row for each system view that is shipped with SQL Server. All system views are contained in the schemas named For a list of columns that this view inherits, see 1 = View has a replication filter. 1 = VIEW_METADATA option specified for view. For more 1 = Table contains persisted data that depends on an assembly whose definition changed during the last ALTER ASSEMBLY.

## Permissions

Article • 02/28/2023 Contains one row for each system view that is shipped with SQL Server. All system views are contained in the schemas named or. Description <inherited columns> For a list of columns that this view inherits, see sys.objects (Transact-SQL). 1 = View is replicated. 1 = View has a replication filter. 1 = VIEW_METADATA option specified for view. For more information, see CREATE VIEW (Transact-SQL). 1 = Table contains persisted data that depends on an assembly whose definition changed during the last ALTER ASSEMBLY. Will be reset to 0 after the next successful DBCC CHECKDB or DBCC CHECKTABLE. 1 = WITH CHECK OPTION was specified in the view definition. 1 = View was created automatically by the system to store correlation information between columns. Creation of this view was enabled by setting DATE_CORRELATION_OPTIMIZATION to ON. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) ﾉ Expand table See Also
