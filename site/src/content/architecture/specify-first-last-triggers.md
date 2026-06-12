---
title: "Specify First & Last Triggers"
topic: "change-data-capture"
description: "You can specify that one of the AFTER triggers associated with a table be either the first AF"
tags: ["change-data-capture","specify-first-last-triggers"]
pubDate: 2025-12-01
---

You can specify that one of the AFTER triggers associated with a table be either the first AFTER

trigger or the last AFTER trigger that is fired for each INSERT, DELETE, and UPDATE triggering

actions. The AFTER triggers that are fired between the first and last triggers are executed in

undefined order.

To specify the order for an AFTER trigger, use the

stored procedure.

has the following options.

Description

Specifies that the DML trigger is the first AFTER trigger fired for a triggering action.

Specifies that the DML trigger is the last AFTER trigger fired for a triggering action.

Specifies that there is no specific order in which the DML trigger should be fired. Used mainly to

reset a trigger from being either first or last.

The following example shows using

:

A table can have INSERT, UPDATE, and DELETE triggers defined on it at the same time. Each

statement type can have its own first and last triggers, but they cannot be the same triggers.

If the first or last trigger defined for a table does not cover a triggering action, such as not

covering FOR UPDATE, FOR DELETE, or FOR INSERT, there is no first or last trigger for the

missing actions.

INSTEAD OF triggers cannot be specified as first or last triggers. INSTEAD OF triggers are fired

before updates are made to the underlying tables. If updates are made by an INSTEAD OF

trigger to underlying tables, the updates occur before any AFTER triggers defined on the table

ﾉ

Expand table

）

Important

The first and last triggers must be two different DML triggers.

```sql
sp_settriggerorder @triggername = 'MyTrigger', @order = 'first', @stmttype =
'UPDATE'
```
