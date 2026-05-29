---
name: "sys.fulltext_document_types"
title: "sys.fulltext_document_types"
category: "full-text"
description: "Returns a row for each document type that is available for full-text indexing operations. Each row represents the IFilter interface that is registered in the instance of SQL Server. The file extension of the supported document type. This value can be used to identify the filter that will be used during full-text indexing of columns of type GUID of the IFilter class that supports file extension. Th"
tags: ["full-text", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns a row for each document type that is available for full-text indexing operations. Each row represents the IFilter interface that is registered in the instance of SQL Server. The file extension of the supported document type. This value can be used to identify the filter that will be used during full-text indexing of columns of type GUID of the IFilter class that supports file extension. The path to the IFilter DLL. The path is only visible to members of

## Permissions

Article • 02/28/2023 Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Returns a row for each document type that is available for full-text indexing operations. Each row represents the IFilter interface that is registered in the instance of SQL Server. Description The file extension of the supported document type. This value can be used to identify the filter that will be used during full-text indexing of columns of type or . GUID of the IFilter class that supports file extension. The path to the IFilter DLL. The path is only visible to members of the fixed server role. Version of the IFilter DLL. Name of the IFilter manufacturer. Note: Only documents with the manufacturer as Microsoft are supported on SQL Database. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. Catalog Views (Transact-SQL) ﾉ Expand table See Also
