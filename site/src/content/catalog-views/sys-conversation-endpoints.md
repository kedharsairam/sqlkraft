---
name: 'sys.conversation_endpoints'
title: 'sys.conversation_endpoints'
category: 'compatibility'
description: 'Each side of a Service Broker conversation is represented by a conversation endpoint. This catalog view contains a row per conversation endpoint in the database. Identifier for this conversation endpoint. Not Identifier for the conversation. This identifier is shared by both participants in the conversation. This together with the is_initiator column is unique within the database. Not NULLABLE. Wh'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Each side of a Service Broker conversation is represented by a conversation endpoint. This catalog view contains a row per conversation endpoint in the database. Identifier for this conversation endpoint. Not Identifier for the conversation. This identifier is shared by both participants in the conversation. This together with the is_initiator column is unique within the database. Not NULLABLE. Whether this endpoint is the initiator or the target
