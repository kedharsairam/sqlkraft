---
title: "DDL Event Groups"
topic: "change-data-capture"
description: "The following tables list the DDL event groups that can be used to run a DDL trigger or an e"
tags: ["change-data-capture","ddl-event-groups"]
pubDate: "2025-12-01"
---

The following tables list the DDL event groups that can be used to run a DDL trigger or an

event notification, and also the Transact-SQL statements they cover. Note the inclusive nature

of the event groups. For example, a DDL trigger or event notification that specifies FOR

DDL_TABLE_EVENTS (10018) covers the CREATE TABLE, ALTER TABLE and DROP TABLE Transact-

SQL statements. A DDL trigger or event notification that specifies FOR

DDL_TABLE_VIEW_EVENTS (10017) covers all Transact-SQL statements under the types

DDL_TABLE_EVENTS, DDL_VIEW_EVENTS, DDL_INDEX_EVENTS, and DDL_STATISTICS_EVENTS.

The events listed under DDL_DATABASE_LEVEL_EVENTS execute at the server (instance) or

database level. Events listed under DDL_SERVER_LEVEL_EVENTS execute only at the server level.

NULL

296

ALTER_SERVER_CONFIGURATION

NULL

10001

DDL_EVENTS

10001

10016

DDL_DATABASE_LEVEL_EVENTS

10016

10027

DDL_ASSEMBLY_EVENTS

10027

102

ALTER_ASSEMBLY

10027

101

CREATE_ASSEMBLY

10027

103

DROP_ASSEMBLY

７

Note

Certain system stored procedures that perform DDL-like operations can also fire DDL

triggers or event notifications. Test your DDL triggers and event notifications to determine

their responses to system stored procedures that are run. For example, the CREATE TYPE

statement and

stored procedure will both fire a DDL trigger or event

notification that is created on a CREATE_TYPE event.

ﾉ

Expand table
