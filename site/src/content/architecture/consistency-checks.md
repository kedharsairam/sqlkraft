---
title: "Consistency checks"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  With temporal tables, the system performs several consistency
tags:
  - "tables"
  - "consistency-checks"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

With temporal tables, the system performs several consistency checks to ensure the schema

complies with the requirements for temporal and the data is consistent, and remains

consistent. In addition, temporal checks are available in the

statement.

Before

is set to

, a set of checks is performed on the history table and

the current table. These checks are grouped into schema checks and data checks (if history

table isn't empty). In addition, the system also performs a runtime consistency check.

When creating or alter a table to become a temporal table, the system verifies that

requirements are met:

1. The names and number of columns is the same in both the current table and the history

table.

2. The datatypes match for each column between the current table and the history table.

3. The period columns are set to.

4. The current table has a primary key constraint and the history table doesn't have a

primary key constraint.

5. No

columns are defined in the history table.

6. No triggers are defined in the history table.

7. No foreign keys are defined in the history table.

8. No table or column constraints are defined on the history table. However, default column

values on the history table are permitted.

9. The history table isn't placed in a read-only filegroup.

10. The history table isn't configured for change tracking or change data capture.

```sql
DBCC CHECKCONSTRAINTS
SYSTEM_VERSIONING
ON
NOT NULL
IDENTITY
```
