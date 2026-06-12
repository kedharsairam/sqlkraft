---
name: "sys.all_columns"
title: "sys.all_columns"
category: "objects"
description: "Shows the union of all columns belonging to user-defined objects and system objects."
tags: ["objects","catalog-view"]
pubDate: 2026-05-29
syntax: "sp_tableoption 'text in row'"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Shows the union of all columns belonging to user-defined objects and system objects.

## Syntax

```sql
sp_tableoption 'text in row'
```

## Permissions

This view provides visibility into the classification state of the database. It can be used for managing the database classifications, as well as for generating reports. Currently only classification of database columns is supported. The following example returns a table that lists the table name, column name, label, label ID, information type, information type ID, rank, and rank description for each classified column in the database. SQL Requires the permission. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. ７ Note Label is a keyword for Azure Synapse Analytics.
