---
title: "Implement"
topic: "change-data-capture"
description: ""
tags: ["change-data-capture","implement"]
pubDate: "2025-12-01"
---

This topic provides information to help you create DDL triggers, modify DDL triggers, and

disable or drop DDL triggers.

DDL triggers are created by using the Transact-SQL CREATE TRIGGER statement for DDL

triggers.

CREATE TRIGGER (Transact-SQL)

If you have to modify the definition of a DDL trigger, you can either drop and re-create the

trigger or redefine the existing trigger in a single step.

If you change the name of an object that is referenced by a DDL trigger, you must modify the

trigger so that its text reflects the new name. Therefore, before renaming an object, display the

dependencies of the object first to determine whether any triggers are affected by the

proposed change.

A trigger can also be modified to encrypt its definition.

ALTER TRIGGER (Transact-SQL)

）

Important

The ability to return result sets from triggers will be removed in a future version of SQL

Server. Triggers that return result sets may cause unexpected behavior in applications that

are not designed to work with them. Avoid returning result sets from triggers in new

development work, and plan to modify applications that currently do this. To prevent

triggers from returning result sets in SQL Server, set the

to 1. The default setting of this option will be 1 in a future version of SQL Server.
