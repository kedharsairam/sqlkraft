---
name: 'sys.numbered_procedures'
title: 'sys.numbered_procedures'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

05/23/2023

Applies to:

SQL Server

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

Contains a row for each SQL Server stored procedure that was created as a numbered

procedure. This does not show a row for the base (number = 1) stored procedure. Entries for

the base stored procedures can be found in views such as

and

.


## Description
ID of the object of the stored procedure.

Number of this procedure within the object, 2 or greater.

The SQL Server text that defines this procedure.

NULL = encrypted.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

）

Important

Numbered procedures are deprecated. Use of numbered procedures is discouraged. A

DEPRECATION_ANNOUNCEMENT event is fired when a query that uses this catalog view is

compiled.

ﾉ

Expand table

７

Note

XML and CLR parameters are not supported for numbered procedures.

See Also

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)
