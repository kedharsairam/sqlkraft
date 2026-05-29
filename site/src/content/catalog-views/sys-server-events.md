---
name: 'sys.server_events'
title: 'sys.server_events'
category: 'compatibility'
description: 'Contains one row for each event for which a server-level event-notification or server-level DDL uniquely identify the server event. ID of the server-level event notification or server-level DDL Type of the event that causes the event notification or DDL Description of the event that causes the DDL trigger or event Event group on which the trigger or event notification is created, or null if not cr'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Contains one row for each event for which a server-level event-notification or server-level DDL uniquely identify the server event. ID of the server-level event notification or server-level DDL Type of the event that causes the event notification or DDL Description of the event that causes the DDL trigger or event Event group on which the trigger or event notification is created, or null if not created on an event group.

## Permissions

Article • 02/28/2023 Applies to: SQL Server Azure SQL Managed Instance Contains one row for each event for which a server-level event-notification or server-level DDL trigger fires. The columns and uniquely identify the server event. Description ID of the server-level event notification or server-level DDL trigger to fire. Type of the event that causes the event notification or DDL trigger to fire. Description of the event that causes the DDL trigger or event notification to fire. Event group on which the trigger or event notification is created, or null if not created on an event group. Description of the event group on which the trigger or event notification is created, or null if not created on an event group The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) ﾉ Expand table See Also
