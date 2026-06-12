---
name: "sys.sp_altermessage"
title: "sp_altermessage"
category: "general"
description: "Alters the state of user-defined or system messages in an instance of the SQL Server Database Engine. User-defined messages can be viewed using the The error number of the message to alter from to indicate that the message is to be written to the Windows , the message is written to the Windows application message isn't always written to the Windows application log,"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_altermessage
              [ @message_id = ] message_id
              , [ @parameter = ]
              N
              'parameter'
              , [ @parameter_value = ]
              'parameter_value'
              [ ; ]
---

## Description

Alters the state of user-defined or system messages in an instance of the SQL Server Database Engine. User-defined messages can be viewed using the The error number of the message to alter from to indicate that the message is to be written to the Windows , the message is written to the Windows application message isn't always written to the Windows application log, but might be written depending

## Syntax

```sql
sp_altermessage
[ @message_id = ] message_id
, [ @parameter = ]
N
'parameter'
, [ @parameter_value = ]
'parameter_value'
[ ; ]
```
