---
title: "Logon Triggers"
topic: "change-data-capture"
description: "Logon triggers fire stored procedures in response to a event."
tags: ["change-data-capture","logon-triggers"]
pubDate: "2025-12-01"
---

Logon triggers fire stored procedures in response to a

event. This event is raised when a

user session is established with an instance of SQL Server. Logon triggers fire after the

authentication phase of logging in finishes, but before the user session is established.

Therefore, all messages originating inside the trigger that would typically reach the user, such

as error messages and messages from the

statement, are diverted to the SQL Server

error log. Logon triggers don't fire if authentication fails.

You can use logon triggers to audit and control server sessions, such as by tracking login

activity, restricting logins to SQL Server, or limiting the number of sessions for a specific login.

For example, in the following code, the logon trigger denies sign-in attempts to SQL Server

initiated by login

if there are already three user sessions created by that login.

The

event corresponds to the

SQL Trace event, which can be used in

Event

Notifications. The primary difference between triggers and event notifications is that triggers

are raised synchronously with events, whereas event notifications are asynchronous. This

means, for example, that if you want to stop a session from being established, you must use a

logon trigger. An event notification on an

event can't be used for this purpose.

```sql
LOGON
PRINT login_test
LOGON
AUDIT_LOGIN
AUDIT_LOGIN
USE master
;
GO
CREATE
LOGIN login_test
WITH
PASSWORD
= N
'3KHJ6dhx(0xVYsdf'
MUST_CHANGE,
CHECK_EXPIRATION =
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
N
'login_test'
FOR
LOGON
AS
BEGIN
IF
ORIGINAL_LOGIN() = N
'login_test'
AND (
SELECT
COUNT (*)
FROM sys.dm_exec_sessions
WHERE is_user_process = 1
AND original_login_name = N
'login_test'
) > 3
ROLLBACK
;
END
;
```
