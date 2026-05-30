---
title: "Capture Logon Trigger Event Data"
topic: "change-data-capture"
description: |
  Article

  •

  08/27/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  To capture XML data about

  events for use inside logon triggers, use the

  EVENTDATA

  function. The

  event returns the follo
tags:
  - "change-data-capture"
  - "capture-logon-trigger-event-data"
pubDate: 2025-12-01
---

Article

•

08/27/2024

Applies to:

SQL Server

Azure SQL Managed Instance

To capture XML data about

events for use inside logon triggers, use the

EVENTDATA

function. The

event returns the following event data schema:

XML

Contains

.

Contains the time when a session requests to be established.

The type of login, such as SQL Server login, Windows account, certificate, server role, or

Microsoft Entra ID.

Contains the base 64-encoded binary stream of the security identification number (SID) for the

specified login name.

```sql
LOGON
LOGON
LOGON
<EVENT_INSTANCE>
<EventType>
event_type
</EventType>
<PostTime>
post_time
</PostTime>
<SPID>
spid
</SPID>
<ServerName>
server_name
</ServerName>
<LoginName>
login_name
</LoginName>
<LoginType>
login_type
</LoginType>
<SID>
sid
</SID>
<ClientHost>
client_host
</ClientHost>
<IsPooled>
is_pooled
</IsPooled>
</EVENT_INSTANCE>
```
