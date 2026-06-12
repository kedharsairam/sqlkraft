---
title: "Index Properties F1 Help"
topic: "filestream"
description: "The sections in this topic refer to various index properties that are available by using SQL"
tags: ["filestream","index-properties-f1-help"]
pubDate: 2025-12-01
---

The sections in this topic refer to various index properties that are available by using SQL

Server Management Studio dialogs.

Index Properties General Page

Select (Index) Columns Dialog Box

Index Properties Storage Page

Index Properties Spatial Page

Index Properties Filter Page

Use the General page to view or modify index properties for the selected table or view. The

options for each page may change based on the type of index selected.

Displays the name of the table or view that the index was created on. This field is read-only. To

select a different table, close the Index Properties page, select the correct table, and then open

the Index Properties page again.

Spatial indexes cannot be specified on indexed views. Spatial indexes can be defined only for a

table that has a primary key. The maximum number of primary key columns on the table is 15.

The combined per-row size of the primary-key columns is limited to a maximum of 895 bytes.

Displays the name of the index. This field is read-only for an existing index. When creating a

new index, type the name of the index.

Indicates the type of index. For new indexes, indicates the type of index selected when opening

the dialog box. Indexes can be:

,

,

,

,

,

, or.

Note

Only one clustered index is allowed for each table. Only one xVelocity memory optimized

columnstore index is allowed for each table.
