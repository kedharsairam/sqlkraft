---
name: 'sys.procedures'
title: 'sys.procedures'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Contains a row for each object that is a procedure of some kind, with

= P, X,

RF, and PC.


## Description
For a list of columns that this view inherits, see

sys.objects

(Transact-SQL)

1 = Procedure is auto-executed at the server startup;

otherwise, 0. Can only be set for procedures in the master

database.

Execution of this procedure is replicated.

Replication of the procedure execution is done only when the

transaction can be serialized.

During execution, the procedure skips constraints marked

NOT FOR REPLICATION.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Last updated on 11/18/2025

ﾉ

Expand table

See Also
