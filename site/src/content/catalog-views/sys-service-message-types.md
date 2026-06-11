---
name: "sys.service_message_types"
title: "sys.service_message_types"
category: "compatibility"
description: "This catalog view contains a row per message type registered in the service broker."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

This catalog view contains a row per message type registered in the service broker. Name of message type, unique within the database. Not NULLABLE. Identifier of the message type, unique within the database. Not Identifier for the database principal that owns this message type. Validation done by Broker prior to sending messages of this type. Not Description of the validation done by Broker prior to sending

## Permissions

Article • 02/28/2023 Applies to: SQL Server This catalog view contains a row per message type registered in the service broker. Description Name of message type, unique within the database. Not NULLABLE. Identifier of the message type, unique within the database. Not NULLABLE. Identifier for the database principal that owns this message type. NULLABLE. Validation done by Broker prior to sending messages of this type. Not NULLABLE. One of: N = None X = XML E = Empty Description of the validation done by Broker prior to sending messages of this type. NULLABLE. One of: NONE XML EMPTY For validation that uses an XML schema, the identifier for the schema collection used. Otherwise, NULL. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . ﾉ Expand table
