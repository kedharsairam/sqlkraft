---
name: "sys.trigger_events"
title: "sys.trigger_events"
category: "compatibility"
description: "Contains a row per event for which a trigger fires. Trigger is marked to be the first to fire for this event. Trigger is marked to be the last to fire for this event. Event group on which the trigger is created, or null if not created on an event group. Description of the event group on which the trigger is created, or null if not created on an event group."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  CREATE
  LOGIN login_test
  WITH
  PASSWORD
  =
  '<password>'
  MUST_CHANGE, CHECK_EXPIRATION =
  ON
  ;
  GO
  GRANT
  VIEW
  SERVER
  STATE
  TO
  login_test;
  GO
  CREATE
  TRIGGER
  connection_limit_trigger
  ON
  ALL
  SERVER
  WITH
  EXECUTE
  AS
  'login_test'
  FOR
  LOGON
  AS
  BEGIN
  IF
  ORIGINAL_LOGIN() =
  'login_test'
  AND
  (
  SELECT
  COUNT
  (*)
  FROM
  sys.dm_exec_sessions
  WHERE
  is_user_process = 1
  AND
  original_login_name =
  'login_test'
  ) > 3
  ROLLBACK
  ;
  END
---

## Description

Contains a row per event for which a trigger fires. Trigger is marked to be the first to fire for this event. Trigger is marked to be the last to fire for this event. Event group on which the trigger is created, or null if not created on an event group. Description of the event group on which the trigger is created, or null if not created on an event group. The visibility of the metadata in catalog views is limited to securables that a user either owns,

## Syntax

```sql
CREATE
LOGIN login_test
WITH
PASSWORD
=
'<password>'
MUST_CHANGE, CHECK_EXPIRATION =
ON
;
GO
GRANT
VIEW
SERVER
STATE
TO login_test;
GO
CREATE
TRIGGER connection_limit_trigger
ON
ALL
SERVER
WITH
EXECUTE
AS
'login_test'
FOR
LOGON
AS
BEGIN
IF
ORIGINAL_LOGIN() =
'login_test'
AND (
SELECT
COUNT (*)
FROM sys.dm_exec_sessions
WHERE is_user_process = 1
AND original_login_name =
'login_test'
) > 3
ROLLBACK
;
END
```

## Permissions
