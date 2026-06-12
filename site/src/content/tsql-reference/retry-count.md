---
name: "Retry count"
title: "Retry count"
category: "statements"
description: "specifies the directory on the local SQL Server instance where the ONNX"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

specifies the directory on the local SQL Server instance where the ONNX

Runtime executables are located.

Requires

or

database permission.

For example:

Or:

To use an external model in an AI function, a principal must be granted the ability to

it.

For example:

If the embeddings call encounters HTTP status codes indicating temporary issues, you can

configure the request to automatically retry. To specify the number of retries, add the following

#### JSON

#### JSON

#### API format

#### Location path format

## Retry count with other parameters

`LOCAL_RUNTIME_PATH`

```sql
ALTER ANY EXTERNAL MODEL
```

```sql
CREATE EXTERNAL MODEL
```

`EXECUTE`

```sql
'{ "dimensions": 1536 }'
```

```sql
GRANT
CREATE
EXTERNAL
MODEL
TO
[<PRINCIPAL>];
GRANT
ALTER
ANY
EXTERNAL
MODEL
TO
[<PRINCIPAL>];
```

```sql
GRANT
EXECUTE
ON
EXTERNAL
MODEL
::MODEL_NAME
TO
[<PRINCIPAL>];
GO
```
