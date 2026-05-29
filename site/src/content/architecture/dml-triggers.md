---
title: "DML Triggers"
topic: "change-data-capture"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The DML trigger is a special type of stored procedure that automatically takes effect when a
  
tags:
  - "change-data-capture"
  - "dml-triggers"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The DML trigger is a special type of stored procedure that automatically takes effect when a

data manipulation language (DML) event takes place that affects the table or view defined in

the trigger. DML events include

,

, or

statements. DML triggers can be

used to enforce business rules and data integrity, query other tables, and include complex

Transact-SQL statements. The trigger and the statement that fires it are treated as a single

transaction, which can be rolled back from within the trigger. If a severe error is detected (for

example, insufficient disk space), the entire transaction automatically rolls back.

DML triggers are similar to constraints in that they can enforce entity integrity or domain

integrity. In general, entity integrity should always be enforced at the lowest level by indexes

that are part of

and

constraints or are created independently of

constraints. Domain integrity should be enforced through

constraints, and referential

integrity (RI) should be enforced through

constraints. DML triggers are most

useful when the features supported by constraints can't meet the functional needs of the

application.

The following list compares DML triggers with constraints and identifies when DML triggers

have benefits over constraints.

DML triggers can cascade changes through related tables in the database; however, these

changes can be executed more efficiently using cascading referential integrity constraints.

constraints can validate a column value only with an exact match to a value

in another column, unless the

clause defines a cascading referential action.

They can guard against malicious or incorrect

,

, and

operations and

enforce other restrictions that are more complex than restrictions defined with

constraints.

Unlike

constraints, DML triggers can reference columns in other tables. For

example, a trigger can use a

from another table to compare to the inserted or

updated data and to perform other actions, such as modify the data or display a user-

defined error message.

They can evaluate the state of a table before and after a data modification and take

actions based on that difference.

```sql
INSERT
UPDATE
DELETE
PRIMARY KEY
UNIQUE
CHECK
FOREIGN KEY
FOREIGN KEY
REFERENCES
INSERT
UPDATE
DELETE
CHECK
CHECK
SELECT
```