---
name: "sys.symmetric_keys"
title: "sys.symmetric_keys"
category: "compatibility"
description: "Returns one row for every symmetric key created with the CREATE SYMMETRIC KEY statement."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  EXECUTE
  sp_configure
  'external rest endpoint enabled'
  , 1;
  RECONFIGURE
  WITH
  OVERRIDE;
  GO
  IF NOT EXISTS (
  SELECT
  *
  FROM
  sys.symmetric_keys
  WHERE
  [
  name
  ] =
  '##MS_DatabaseMasterKey##'
  )
  BEGIN
  CREATE
  MASTER
  KEY
  ENCRYPTION
  BY
  PASSWORD
  = N
  '<password>'
  ;
  END
  GO
  CREATE
  DATABASE
  SCOPED CREDENTIAL [https://my-azure-openai-
  endpoint.cognitiveservices.azure.com/]
  WITH
  IDENTITY
  =
  'HTTPEndpointHeaders'
  , secret =
  '{"api-
  key":"YOUR_AZURE_OPENAI_KEY"}'
  ;
  GO
  CREATE
  EXTERNAL
  MODEL
  MyAzureOpenAIModel
  WITH
  (
  LOCATION =
  'https://my-azure-openai-
  endpoint.cognitiveservices.azure.com/openai/deployments/text-embedding-ada-
  002/embeddings?api-version=2023-05-15'
  ,
  API_FORMAT =
  'Azure OpenAI'
  ,
  MODEL_TYPE = EMBEDDINGS,
  MODEL
  =
  'text-embedding-ada-002'
  ,
---

## Description

Analytics Platform System (PDW) Returns one row for every symmetric key created with the CREATE SYMMETRIC KEY statement.

## Syntax

```sql
EXECUTE sp_configure
'external rest endpoint enabled'
, 1;
RECONFIGURE
WITH
OVERRIDE;
GO
IF NOT EXISTS (
SELECT
*
FROM sys.symmetric_keys
WHERE
[
name
] =
'##MS_DatabaseMasterKey##'
)
BEGIN
CREATE
MASTER
KEY
ENCRYPTION
BY
PASSWORD
= N
'<password>'
;
END
GO
CREATE
DATABASE
SCOPED CREDENTIAL [https://my-azure-openai-
endpoint.cognitiveservices.azure.com/]
WITH
IDENTITY
=
'HTTPEndpointHeaders'
, secret =
'{"api-
key":"YOUR_AZURE_OPENAI_KEY"}'
;
GO
CREATE
EXTERNAL
MODEL
MyAzureOpenAIModel
WITH (
LOCATION =
'https://my-azure-openai-
endpoint.cognitiveservices.azure.com/openai/deployments/text-embedding-ada-
002/embeddings?api-version=2023-05-15'
,
API_FORMAT =
'Azure OpenAI'
,
MODEL_TYPE = EMBEDDINGS,
MODEL
=
'text-embedding-ada-002'
,
```

## Examples

### Example 1

```sql
##MS_DatabaseMasterKey##
```

### Example 2

```sql
CREATE
MASTER
KEY
ENCRYPTION
BY
PASSWORD
=
'<strong password>'
;
GO
SELECT
*
FROM sys.symmetric_keys;
GO
```

### Example 3

`ALTER`

### Example 4

`SamInventory42`

### Example 5

`HamidS`

### Example 6

`HamidS`

### Example 7

`ALTER`

### Example 8

```sql
USE
AdventureWorks2022;
REVOKE
ALTER
ON
SYMMETRIC
KEY
::SamInventory42
TO
HamidS
CASCADE
;
GO
```
