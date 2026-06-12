---
name: "sys.server_triggers"
title: "sys.server_triggers"
category: "compatibility"
description: "Contains the set of all server-level DDL triggers with object_type of TR or TA. In the case of CLR triggers, the assembly must be loaded into the database. All server-level DDL trigger names exist in a single, global scope. Description of class of parent. Is always: Always 0 for triggers on the SERVER. Description of the class of the object type. Date the trigger was last modified by using an ALTE"
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
              name
              , is_disabled, create_date, modify_date
              FROM
              sys.server_triggers
              WHERE
              type_desc =
              'LOGON'
              ;
              DISABLE TRIGGER trigger_name ON ALL SERVER;
              DROP
              TRIGGER
              trigger_name
              ON
              ALL
              SERVER
              ;
---

## Description

Contains the set of all server-level DDL triggers with object_type of TR or TA. In the case of CLR triggers, the assembly must be loaded into the database. All server-level DDL trigger names exist in a single, global scope. Description of class of parent. Is always: Always 0 for triggers on the SERVER. Description of the class of the object type. Date the trigger was last modified by using an ALTER statement.

## Syntax

```sql
SELECT name
, is_disabled, create_date, modify_date
FROM sys.server_triggers
WHERE type_desc =
'LOGON'
;
DISABLE TRIGGER trigger_name ON ALL SERVER;
DROP
TRIGGER trigger_name
ON
ALL
SERVER
;
```

## Permissions

SQL) Article • 02/28/2023 Contains one row for each assembly module for the server-level triggers of type TA. This view maps assembly triggers to the underlying CLR implementation. You can join this relation to. The assembly must be loaded into the database. The tuple (object_id) is the key for the relation. Description This is a FOREIGN KEY reference back to the object upon which this assembly module is defined. ID of the assembly from which this module was created. The assembly must be loaded into the master database. Name of the class within assembly that defines this module. Name of the method within the class that defines this module. Is NULL for aggregate functions (AF). ID of the EXECUTE AS server principal. NULL by default or if EXECUTE AS CALLER. ID of the specified principal if EXECUTE AS SELF EXECUTE AS <principal>. -2 = EXECUTE AS OWNER. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. ﾉ Expand table See Also
