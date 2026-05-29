---
name: "sys.all_objects"
title: "sys.all_objects"
category: "objects"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Shows the UNION of all schema-scoped user-defined objects and system objects. Object identification number. Is unique within a database. ID of the individual owner if different from the schema owner. By default, schema-contained objects are owned by the schema owner. However, another owner can be specified by using the ALTER AUTHORIZ"
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.extended_procedures"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Shows the UNION of all schema-scoped user-defined objects and system objects. Object identification number. Is unique within a database. ID of the individual owner if different from the schema owner. By default, schema-contained objects are owned by the schema owner. However, another owner can be specified by using the ALTER AUTHORIZATION statement to change ownership.

## Syntax

```sql
sys.extended_procedures
```

## Permissions

Article • 04/12/2024 Applies to: SQL Server Contains a row for each object that is an extended stored procedure, with = . Because extended stored procedures are installed into the database, they're only visible from that database context. Selecting from the view in any other database context returns an empty result set. Description Columns inherited from For a list of columns that this view inherits, see sys.objects . Name, including path, of the DLL for this extended stored procedure. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) System catalog views (Transact-SQL) ﾉ Expand table Related content System catalog views (Transact-SQL) sys.all_objects (Transact-SQL) sys.system_objects (Transact-SQL) sys.triggers (Transact-SQL) Object Catalog Views (Transact-SQL) Querying the SQL Server System Catalog FAQ sys.internal_tables (Transact-SQL) Related content This view provides visibility into the classification state of the database. It can be used for managing the database classifications, as well as for generating reports. Currently only classification of database columns is supported. The following example returns a table that lists the table name, column name, label, label ID, information type, information type ID, rank, and rank description for each classified column in the database. SQL Requires the permission. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . ７ Note Label is a keyword for Azure Synapse Analytics.
