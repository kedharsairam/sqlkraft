---
title: "Table Column Properties"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  SQL database in Microsoft Fabric

  The
tags:
  - "tables"
  - "table-column-properties"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

These properties appear in the bottom pane of Table Designer. Unless otherwise noted, you

can edit these properties in the Properties window when the column is selected. The

can be displayed in categories or alphabetically. Many properties only appear or can

only be changed for certain data types.

Expands to show

,

,

,

,

,

,

and.

Displays the name of the selected column.

Indicates whether this column allows nulls. To edit this property, click the Allow Nulls checkbox

corresponding to the column in the top pane of Table Designer.

Displays the data type for the selected column. To edit this property, click its value, expand the

drop-down list, and choose another value.

Displays the default for this column whenever no value is specified for this column. The value

of this field can be either the value of a SQL Server default constraint or the name of a global

constraint to which the column is bound. The drop-down list contains all global defaults

defined in the database. To bind the column to a global default, select from the drop-down list.

Alternatively, to create a default constraint for the column, type the default value directly as

text.

７

Note

If the table is published for replication, you must make schema changes using the

Transact-SQL statement

or SQL Server Management Objects (SMO). When

schema changes are made using the Table Designer or the Database Diagram Designer, it

attempts to drop and recreate the table. You cannot drop published objects, therefore the

schema change will fail.
