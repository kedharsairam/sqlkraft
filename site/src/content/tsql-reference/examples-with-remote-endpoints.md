---
name: "Examples with remote endpoints"
title: "Examples with remote endpoints"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

## Create an EXTERNAL MODEL with Azure OpenAI using

## Managed Identity

### Cognitive

### Services OpenAI Contributor

### managed identity enabled by Azure Arc

### Role-based access

### control for Azure OpenAI in Azure AI Foundry Models

This example creates an external model of the

type using Azure OpenAI and uses

Managed Identity

for authentication.

In SQL Server 2025 (17.x) and later versions, you must

connect your SQL Server to Azure Arc

and

enable the primary managed identity.

Create access credentials to Azure OpenAI using a managed identity:

Create the external model:

）

Important

If you use Managed Identity with Azure OpenAI and SQL Server 2025 (17.x), the

role must be granted to

's system-assigned. For more information, see.

## Create an external model with Azure OpenAI using API keys

## and parameters

## Create an EXTERNAL MODEL with Ollama and an explicit

## owner

This example creates an external model of the

type using Azure OpenAI and uses

API Keys for authentication. The example also uses

to set the dimensions

parameter at the endpoint to 725.

Create access credentials to Azure OpenAI using a key:

Create the external model:

This example creates an external model of the

type using Ollama hosted locally for

development purposes.

## Create an EXTERNAL MODEL with OpenAI

`EMBEDDINGS`

```sql
SELECT
*
FROM sys.external_models;
```

```sql
CREATE
DATABASE
SCOPED CREDENTIAL [https://my-azure-openai-
endpoint.cognitiveservices.azure.com/]
WITH
IDENTITY
=
'Managed Identity'
, secret =
'{"resourceid":"https://cognitiveservices.azure.com"}'
;
GO
CREATE
EXTERNAL
MODEL
MyAzureOpenAIModel
AUTHORIZATION CRM_User
WITH (
LOCATION =
'https://my-azure-openai-
endpoint.cognitiveservices.azure.com/openai/deployments/text-embedding-ada-
002/embeddings?api-version=2024-02-01'
,
API_FORMAT =
'Azure OpenAI'
,
MODEL_TYPE = EMBEDDINGS,
```

`EMBEDDINGS`

`PARAMETERS`

`EMBEDDINGS`

```sql
MODEL
=
'text-embedding-ada-002'
,
CREDENTIAL = [https://my-azure-openai-endpoint.cognitiveservices.azure.com/]
);
```

```sql
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
AUTHORIZATION CRM_User
WITH (
LOCATION =
'https://my-azure-openai-
endpoint.cognitiveservices.azure.com/openai/deployments/text-embedding-3-
small/embeddings?api-version=2024-02-01'
,
API_FORMAT =
'Azure OpenAI'
,
MODEL_TYPE = EMBEDDINGS,
MODEL
=
'text-embedding-3-small'
,
CREDENTIAL = [https://my-azure-openai-endpoint.cognitiveservices.azure.com/],
PARAMETERS
=
'{"dimensions":725}'
);
```
