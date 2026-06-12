---
name: "sys.messages"
title: "Messages (for errors) - sys.messages"
category: "compatibility"
description: "Contains information about all available SQL Server Agent proxy subsystems. The table is stored in the ID of the subsystem."
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  SELECT
      message_id
      AS
      Error
      ,
      severity
      AS
      Severity,
      [
      Event
      Logged] =
      CASE
      is_event_logged
      WHEN
      0
      THEN
      'No'
      ELSE
      'Yes'
      END
      ,
      [
      text
      ]
      AS
      [Description]
      FROM
      sys.messages
      WHERE
      language_id = 1040
      /* replace 1040 with the desired language ID, such as 1033
      for US English */
      ORDER
      BY
      message_id;
---

## Description

Contains information about all available SQL Server Agent proxy subsystems. The table is stored in the ID of the subsystem.

## Syntax

```sql
SELECT message_id
AS
Error
,
severity
AS
Severity,
[
Event
Logged] =
CASE is_event_logged
WHEN
0
THEN
'No'
ELSE
'Yes'
END
,
[
text
]
AS
[Description]
FROM sys.messages
WHERE language_id = 1040
/* replace 1040 with the desired language ID, such as 1033 for US English */
ORDER
BY message_id;
```

## Arguments

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

Generates an error message and initiates error processing for the session.

reference a user-defined message stored in the

catalog view, or build a message

dynamically. The message is returned as a server error message to the calling application or to

an associated

construct. New applications should use

Syntax for SQL Server, Azure SQL Database, and Azure SQL Managed Instance:

Syntax for Azure Synapse Analytics and Parallel Data Warehouse:

statement doesn't honor. New applications should use

## Permissions

08/29/2025 For more information, see sp_addmessage. Description ID of the message. Is unique across server. Message IDs less than 50,000 are system messages. Language ID for which the text in is used, as defined in. This value is unique for a specified. Severity level of the message, between 0 and 25. This value is the same for all message languages within a. 1 = Message is event-logged when an error is raised. This value is the same for all message languages within a. Text of the message used when the corresponding is active. Requires membership in the role. For more information, see Metadata visibility configuration. THROW (Transact-SQL) System catalog views (Transact-SQL) Exception Message Box Programming Error Messages Database Engine events and errors ﾉ Expand table
## Remarks

Contains information about all available SQL Server Agent proxy subsystems. The

table is stored in the

Description

ID of the subsystem.

Name of the subsystem.

description_id

Message ID of the row in the

catalog view that

contains the subsystem description.

Location of the subsystem DLL.

Full path to the executable that uses the subsystem.

Function that is called when the subsystem is initialized.

Function that is called when a subsystem step is run.

Function that is called when a subsystem finishes running.

Maximum number of concurrent steps for a given subsystem.

Only members of the

fixed server role can access this table.

dbo.sysproxysubsystem (Transact-SQL)

dbo.sysproxies (Transact-SQL)

sys.messages (Transact-SQL)

Expand table

Here's the result set.

sys.messages (Transact-SQL)

TRY.CATCH (Transact-SQL)

ERROR_LINE (Transact-SQL)

ERROR_MESSAGE (Transact-SQL)

ERROR_PROCEDURE (Transact-SQL)

ERROR_SEVERITY (Transact-SQL)

ERROR_STATE (Transact-SQL)

RAISERROR (Transact-SQL)

@@ERROR (Transact-SQL)

Errors and Events Reference (Database Engine)

Here's the result set.

sys.messages (Transact-SQL)

TRY.CATCH (Transact-SQL)

ERROR_LINE (Transact-SQL)

ERROR_MESSAGE (Transact-SQL)

ERROR_PROCEDURE (Transact-SQL)

ERROR_SEVERITY (Transact-SQL)

ERROR_STATE (Transact-SQL)

RAISERROR (Transact-SQL)

@@ERROR (Transact-SQL)

Errors and Events Reference (Database Engine)

sys.messages

TRY.CATCH (Transact-SQL)

ERROR_LINE (Transact-SQL)

ERROR_MESSAGE (Transact-SQL)

ERROR_NUMBER (Transact-SQL)

ERROR_SEVERITY (Transact-SQL)

ERROR_STATE (Transact-SQL)

RAISERROR (Transact-SQL)

@@ERROR (Transact-SQL)

sys.messages (Transact-SQL)

TRY.CATCH (Transact-SQL)

ERROR_LINE (Transact-SQL)

ERROR_MESSAGE (Transact-SQL)

ERROR_NUMBER (Transact-SQL)

ERROR_PROCEDURE (Transact-SQL)

ERROR_SEVERITY (Transact-SQL)

RAISERROR (Transact-SQL)

@@ERROR (Transact-SQL)

Errors and Events Reference (Database Engine)

## Examples

### Example 1

`sys.messages`

### Example 2

```sql
1033
```

### Example 3

```sql
SELECT message_id,
language_id,
severity,
is_event_logged,
text
FROM sys.messages
WHERE language_id = 1033;
```
