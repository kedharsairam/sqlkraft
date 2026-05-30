---
name: "sys.procedures"
title: "sys.procedures"
category: "compatibility"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each object that is a procedure of some kind, with For a list of columns that this view inherits, see 1 = Procedure is auto-executed at the server startup; otherwise, 0. Can only be set for procedures in the master Execution of this procedure is replicated. Replication of the procedure execution is done only when t"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each object that is a procedure of some kind, with For a list of columns that this view inherits, see 1 = Procedure is auto-executed at the server startup; otherwise, 0. Can only be set for procedures in the master Execution of this procedure is replicated. Replication of the procedure execution is done only when the

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains a row for each object that is a procedure of some kind, with = P, X, RF, and PC. Description For a list of columns that this view inherits, see sys.objects (Transact-SQL) 1 = Procedure is auto-executed at the server startup; otherwise, 0. Can only be set for procedures in the master database. Execution of this procedure is replicated. Replication of the procedure execution is done only when the transaction can be serialized. During execution, the procedure skips constraints marked NOT FOR REPLICATION. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) Last updated on 11/18/2025 ﾉ Expand table See Also Article • 05/23/2023 Applies to: SQL Server Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric Contains a row for each SQL Server stored procedure that was created as a numbered procedure. This does not show a row for the base (number = 1) stored procedure. Entries for the base stored procedures can be found in views such as and . Description ID of the object of the stored procedure. Number of this procedure within the object, 2 or greater. The SQL Server text that defines this procedure. NULL = encrypted. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . ） Important Numbered procedures are deprecated. Use of numbered procedures is discouraged. A DEPRECATION_ANNOUNCEMENT event is fired when a query that uses this catalog view is compiled. ﾉ Expand table ７ Note XML and CLR parameters are not supported for numbered procedures. See Also
