---
name: "sys.external_models"
title: "sys.external_models"
category: "external"
description: "Contains a row for each external model in the current database."
tags: ["external", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
  *
  FROM
  sys.external_models;
---

## Description

Contains a row for each external model in the current database. ID of the model, unique within an instance of SQL Server ID of the database principal that owns the external model Server name or file path of the model ID of the database scoped credential object JSON to be appended to the outgoing payload Time the model was updated (if updated), and defaults to The visibility of the metadata in catalog views is limited to securables that a user either owns,

## Syntax

```sql
SELECT
*
FROM sys.external_models;
```

## Permissions

Applies to: SQL Server 2025 (17.x) Contains a row for each external model in the current database. Description ID of the model, unique within an instance of SQL Server Name of the model ID of the database principal that owns the external model object Server name or file path of the model Name of the API format ( , , etc.) ID of the model type. ( , , etc.) Name of the model type. ( , , etc.) Name of the embedding model ( , etc.) ID of the database scoped credential object JSON to be appended to the outgoing payload Create time of the model Time the model was updated (if updated), and defaults to on creation of the model The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user is granted some permission. For more information, see Metadata Visibility Configuration . AI_GENERATE_EMBEDDINGS (Transact-SQL) AI_GENERATE_CHUNKS (Transact-SQL) ﾉ Expand table Related content
