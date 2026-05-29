---
name: 'sys.extended_procedures'
title: 'sys.extended_procedures'
category: 'compatibility'
description: 'Contains a row for each object that is an extended stored procedure, with . Because extended stored procedures are installed into the database, they''re only visible from that database context. Selecting from the view in any other database context returns an empty result set. For a list of columns that this view inherits, see Name, including path, of the DLL for this extended The visibility of the '
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: 'sys.extended_procedures'
---

## Description

Contains a row for each object that is an extended stored procedure, with . Because extended stored procedures are installed into the database, they're only visible from that database context. Selecting from the view in any other database context returns an empty result set. For a list of columns that this view inherits, see Name, including path, of the DLL for this extended The visibility of the metadata in catalog views is limited to securables that a user either owns,

## Syntax

```sql
sys.extended_procedures
```

## Permissions

Article • 04/12/2024 Applies to: SQL Server Contains a row for each object that is an extended stored procedure, with = . Because extended stored procedures are installed into the database, they're only visible from that database context. Selecting from the view in any other database context returns an empty result set. Description Columns inherited from For a list of columns that this view inherits, see sys.objects . Name, including path, of the DLL for this extended stored procedure. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) System catalog views (Transact-SQL) ﾉ Expand table Related content
