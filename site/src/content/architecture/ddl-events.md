---
title: "DDL Events"
topic: "change-data-capture"
description: ""
tags: ["change-data-capture","ddl-events"]
pubDate: 2025-12-01
---

The following tables list the DDL events that can be used to fire a DDL trigger or event

notification. Note that each event corresponds to a Transact-SQL statement or stored

procedure, with the statement syntax modified to include an underscore character (\_) between

keywords.

DDL triggers or event notifications can be created to fire in response to the following events

when they occur in the database in which the trigger or event notification is created, or

anywhere in the server instance.

CREATE_APPLICATION_ROLE (Applies to the CREATE APPLICATION ROLE statement and. If a new schema is created, this event also triggers a CREATE_SCHEMA event.)

ALTER_APPLICATION_ROLE (Applies to the ALTER APPLICATION ROLE statement and.)

DROP_APPLICATION_ROLE (Applies to the DROP APPLICATION ROLE statement and.)

CREATE_ASSEMBLY

ALTER_ASSEMBLY

DROP_ASSEMBLY

CREATE_ASYMMETRIC_KEY

）

Important

System stored procedures that perform DDL-like operations also fire DDL triggers and

event notifications. Test your DDL triggers and event notifications to determine their

responses to system stored procedures that are run. For example, the CREATE TYPE

statement and

stored procedure will both fire a DDL trigger or event

notification that is created on a CREATE_TYPE event.
