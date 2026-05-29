---
name: 'Example with ONNX Runtime running locally'
title: 'Example with ONNX Runtime running locally'
category: 'queries'
description: 'This example creates an external model of the'
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

## Security considerations

This example creates an external model of the

type using the OpenAI

and HTTP header based credentials for authentication.

SQL

ONNX Runtime

is an open-source inference engine that allows you to run machine learning

models locally, making it ideal for integrating AI capabilities into SQL Server environments.

This example guides you through setting up SQL Server 2025 (17.x) with ONNX Runtime to

enable local AI-powered text embedding generation. It only applies on Windows.

）

Important

This feature requires that

SQL Server Machine Learning Services

is installed.

### Implement strong access controls

### Monitor and audit access

### Conduct regular security assessments

## Step 1: Enable developer preview features on SQL Server 2025

## Step 2: Enable the local AI runtime on SQL Server 2025

You can use the AI Runtime Host feature to configure and use your own LLMs and ONNX

libraries with SQL Server. Because Microsoft does not validate or monitor third-party models

and libraries, you are responsible for selecting appropriate models and libraries, filtering

content, securing the runtime, and ensuring compliance with any applicable policies and

regulations.

To mitigate these risks, consider the following security best practices:

: Ensure that only authorized users have access to

sensitive data and ONNX Runtime models. Validate all models before loading them into

SQL Server. Use the

principle of least privilege

, as well as database roles and privileges.

: Regularly monitor and audit access to the database and

function calls to detect suspicious activity.

: Perform vulnerability scans and security reviews to

identify and mitigate potential risks.

Run the following Transact-SQL (T-SQL) command to enable SQL Server 2025 (17.x) preview

features in the database you would like use for this example:

SQL

Enable external AI runtimes by running the following T-SQL query:

SQL

Ｕ

Caution

A malicious or compromised ONNX model could exfiltrate data or execute unauthorized

code. Only use models from trusted, verified sources.

#### PowerShell

#### PowerShell

## Step 3: Set up the ONNX Runtime library

## Step 4: Set up the tokenization library

### tokenizers_cpp.dll

## Step 5: Download the ONNX model

Create a directory on the SQL Server instance to hold the ONNX Runtime library files. In this

example,

is used.

You can use the following commands to create the directory:

Next, download a version of

ONNX Runtime

(1.19 or greater) that's appropriate for your

operating system. After unzipping the download, copy the

(located in the lib

directory) to the

directory that was created.

Download and build

the tokenizers-cpp library

from GitHub. Once the dll is created, place

the tokenizer in the

directory.

Start by creating the

directory in

.

This example uses the

model, which can be downloaded from

Hugging

Face

.

Clone the repository into the

directory with the following

git

command:

７

Note

Ensure the created dll is named

#### Console

#### PowerShell

### The 'PARAMETERS' value used here is a placeholder needed for SQL Server 2025 (17.x).

## Step 6: Set directory permissions

## Step 7: Create the external model

If not installed, you can download git from the following

download link

or via winget (winget

install Microsoft.Git)

Use the following PowerShell script to provide the MSSQLLaunchpad user access to the ONNX

Runtime directory:

Run the following query to register your ONNX model as an external model object:

SQL

should point to the directory containing

and

files.

should point to directory containing

and

files.

#### Output

## Step 8: Generate embeddings

## Enable XEvent system logging

Use the

function to test the model by running the following query:

SQL

This command launches the

, load the required DLLs, and processes the input

text.

The result from the previous query is an array of embeddings:

Run the following query to enable system logging for troubleshooting.

SQL

Next, use this query see the captured system logs:

SQL

#### PowerShell

## Clean up

To remove the external model object, run the following T-SQL statement:

SQL

To remove the directory permissions, run the following PowerShell commands:

Finally, delete the

directory.

ALTER EXTERNAL MODEL (Transact-SQL)

DROP EXTERNAL MODEL (Transact-SQL)

AI_GENERATE_EMBEDDINGS (Transact-SQL)

AI_GENERATE_CHUNKS (Transact-SQL)

sys.external_models

Create and deploy an Azure OpenAI in Azure AI Foundry Models resource

Related content

Server configuration options

Role-based access control for Azure OpenAI in Azure AI Foundry Models

）

Note:

The author created this article with assistance from AI.

Learn more

Last updated on 04/07/2026

```sql
EMBEDDINGS
```

```sql
API_FORMAT
```

```sql
CREATE
EXTERNAL
MODEL
MyOllamaModel
AUTHORIZATION AI_User
WITH
(
LOCATION =
'https://localhost:11435/api/embed'
,
API_FORMAT =
'Ollama'
,
MODEL_TYPE = EMBEDDINGS,
MODEL
=
'all-minilm'
);
```

```sql
-- Create access credentials
CREATE
DATABASE
SCOPED CREDENTIAL [https://openai.com]
WITH
IDENTITY
=
'HTTPEndpointHeaders'
, secret =
'{"Bearer":"YOUR_OPENAI_KEY"}'
;
GO
-- Create the external model
CREATE
EXTERNAL
MODEL
MyAzureOpenAIModel
AUTHORIZATION CRM_User
WITH
(
LOCATION =
'https://api.openai.com/v1/embeddings'
,
API_FORMAT =
'OpenAI'
,
MODEL_TYPE = EMBEDDINGS,
MODEL
=
'text-embedding-ada-002'
,
CREDENTIAL = [https://openai.com]
);
```

```sql
AI_GENERATE_EMBEDDINGS
```

```sql
ALTER
DATABASE
SCOPED CONFIGURATION
SET
PREVIEW_FEATURES =
ON
;
```

```sql
EXECUTE
sp_configure
'external AI runtimes enabled'
, 1;
RECONFIGURE
WITH
OVERRIDE;
```

```sql
C:\onnx_runtime
```

```sql
onnxruntime.dll
```

```sql
C:\onnx_runtime
```

```sql
C:\onnx_runtime
```

```sql
model
```

```sql
C:\onnx_runtime\
```

```sql
all-MiniLM-L6-v2-onnx
```

```sql
C:\onnx_runtime\model
```

```sql
cd C:\
mkdir onnx_runtime
```

```sql
cd C:\onnx_runtime
mkdir model
```

```sql
LOCATION
```

```sql
model.onnx
```

```sql
tokenizer.json
```

```sql
LOCAL_RUNTIME_PATH
```

```sql
onnxruntime.dll
```

```sql
tokenizer_cpp.dll
```

```sql
cd C:\onnx_runtime\model
git clone https://huggingface.co/nsense/all-MiniLM-L6-v2-onnx
```

```sql
$AIExtPath =
"C:\onnx_runtime"
;
$Acl =
Get-Acl
-Path
$AIExtPath
$AccessRule =
New-Object
System.Security.AccessControl.FileSystemAccessRule(
"MSSQLLaunchpad"
,
"FullControl"
,
"ContainerInherit,ObjectInherit"
,
"None"
,
"Allow"
)
$Acl.AddAccessRule($AccessRule)
Set-Acl
-Path
$AIExtPath
-AclObject
$Acl
```

```sql
CREATE
EXTERNAL
MODEL
myLocalOnnxModel
WITH
(
LOCATION =
'C:\onnx_runtime\model\all-MiniLM-L6-v2-onnx'
,
API_FORMAT =
'ONNX Runtime'
,
MODEL_TYPE = EMBEDDINGS,
MODEL
=
'allMiniLM'
,
PARAMETERS
=
'{"valid":"JSON"}'
,
LOCAL_RUNTIME_PATH =
'C:\onnx_runtime\'
);
```

```sql
ai_generate_embeddings
```

```sql
AIRuntimeHost
```

```sql
SELECT
AI_GENERATE_EMBEDDINGS(N
'Test Text'
USE
MODEL
myLocalOnnxModel);
[0.320098,0.568766,0.154386,0.205526,-0.027379,-0.149689,-0.022946,-0.385856,-0.039
183...]
```

```sql
CREATE
EVENT
SESSION
newevt
ON
SERVER
ADD
EVENT
ai_generate_embeddings_airuntime_trace
(
ACTION
(sqlserver.sql_text, sqlserver.session_id)
)
ADD
TARGET package0.ring_buffer
WITH
(
MAX_MEMORY = 4096 KB,
EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
MAX_DISPATCH_LATENCY = 30
SECONDS
,
TRACK_CAUSALITY =
ON
,
STARTUP_STATE =
OFF
);
GO
ALTER
EVENT
SESSION
newevt
ON
SERVER
STATE =
START
;
GO
```

```sql
C:/onnx_runtime
```

```sql
SELECT
event_data.value(
'(@name)[1]'
,
'varchar(100)'
)
AS
event_name,
event_data.value(
'(@timestamp)[1]'
,
'datetime2'
)
AS
[
timestamp
],
event_data.value(
'(data[@name = "model_name"]/value)[1]'
,
'nvarchar(200)'
)
AS
model_name,
event_data.value(
'(data[@name = "phase_name"]/value)[1]'
,
'nvarchar(100)'
)
AS
phase,
event_data.value(
'(data[@name = "message"]/value)[1]'
,
'nvarchar(max)'
)
AS
message,
event_data.value(
'(data[@name = "request_id"]/value)[1]'
,
'nvarchar(max)'
)
AS
session_id,
event_data.value(
'(data[@name = "error_code"]/value)[1]'
,
'bigint'
)
AS
error_code
FROM
(
SELECT
CAST
(target_data
AS
XML
)
AS
target_data
FROM
sys.dm_xe_sessions
AS
s
INNER
JOIN
sys.dm_xe_session_targets
AS
t
ON
s.address = t.event_session_address
WHERE
s.name =
'newevt'
AND
t.target_name =
'ring_buffer'
)
AS
data
CROSS
APPLY
target_data.nodes(
'//RingBufferTarget/event'
)
AS
XEvent(event_data);
```

```sql
DROP
EXTERNAL
MODEL
myLocalOnnxModel;
$Acl.RemoveAccessRule($AccessRule)
Set-Acl
-Path
$AIExtPath
-AclObject
$Acl
```
