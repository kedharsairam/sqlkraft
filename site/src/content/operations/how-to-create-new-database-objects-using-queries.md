---
title: "How to: Create New Database Objects Using Queries"
topic: "ssb-diagnose"
description: |
  09/10/2025

  If you prefer to use scripts to create or edit views, stored procedures, functions, triggers, or

  user-defined-types, you can use the Transact-SQL Editor. The Transact-SQL Editor provides

tags:
  - "ssb-diagnose"
  - "how-to-create-new-database-objects-using-queries"
pubDate: 2025-12-01
---

09/10/2025

If you prefer to use scripts to create or edit views, stored procedures, functions, triggers, or

user-defined-types, you can use the Transact-SQL Editor. The Transact-SQL Editor provides

IntelliSense and other language support. For more information, see

Use Transact-SQL Editor to

edit and execute scripts

.

The Transact-SQL Editor is invoked when you use the

contextual menu to open a

database entity in a connected database or a project. It automatically opens when you use the

contextual menu from the SQL Server Object Explorer, or when you add a new

script object to a database project. If you aren't connected to a database but want to execute a

query against it, you can also use the

dialog box by selecting

SQL Editor

menu from the

SQL

menu to connect to a database and launch the Transact-SQL

Editor.

1. Right-click the

database node and select

.

2. In the script pane, paste in this code:

SQL

3. Select the

button in the Transact-SQL Editor toolbar to run this query.

4. Right-click the

database in

SQL Server Object Explorer

and select

. A new

table has been added to the database.

1. Replace the code in the current Transact-SQL Editor with the following script:

```cmd
Trade
Trade
Fruits
CREATE
TABLE
[dbo].[Fruits]
(
[
Id
]
INT
NOT
NULL
,
[Perishable]
BIT
DEFAULT
((1))
NULL
,
PRIMARY
KEY
CLUSTERED ([
Id
]
ASC
),
FOREIGN
KEY
([
Id
])
REFERENCES
[dbo].[Products] ([
Id
])
);
```
