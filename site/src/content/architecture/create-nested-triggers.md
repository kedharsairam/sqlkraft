---
title: "Create Nested Triggers"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Both DML and DDL triggers are nested when a trigger performs an action that initiates another
tags:
  - "change-data-capture"
  - "create-nested-triggers"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Both DML and DDL triggers are nested when a trigger performs an action that initiates another

trigger. These actions can initiate other triggers, and so on. DML and DDL triggers can be

nested up to 32 levels. You can control whether AFTER triggers can be nested through the

server configuration option. INSTEAD OF triggers (only DML triggers can be

INSTEAD OF triggers) can be nested regardless of this setting.

If nested triggers are allowed and a trigger in the chain starts an infinite loop, the nesting level

is exceeded and the trigger terminates.

You can use nested triggers to perform useful housekeeping functions such as storing a

backup copy of rows affected by a previous trigger. For example, you can create a trigger on

that saves a backup copy of the

rows that the

trigger deleted. With the

trigger in effect, deleting

1965 from

deletes the corresponding row or rows from. To save the data, you can create a DELETE trigger on

that saves the deleted data into another separately created table,. For example:

We do not recommend using nested triggers in an order-dependent sequence. Use separate

triggers to cascade data modifications.

７

Note

Any reference to managed code from a Transact-SQL trigger counts as one level against

the 32-level nesting limit. Methods invoked from within managed code do not count

against this limit.

７

Note

```sql
PurchaseOrderDetail
PurchaseOrderDetail delcascadetrig delcascadetrig
PurchaseOrderID
PurchaseOrderHeader
PurchaseOrderDetail
PurchaseOrderDetail del_save
CREATE TRIGGER Purchasing.savedel
ON Purchasing.PurchaseOrderDetail
FOR DELETE
AS
INSERT del_save
SELECT * FROM deleted;
```
