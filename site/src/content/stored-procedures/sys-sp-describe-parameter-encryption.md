---
name: "sys.sp_describe_parameter_encryption"
title: "sp_describe_parameter_encryption"
category: "general"
description: "2016 (13.x) and later Analyzes the specified Transact-SQL statement and its parameters, to determine which parameters correspond to database columns that are protected by using the Always Encrypted feature. Returns encryption metadata for the parameters that correspond to encrypted columns. One or more Transact-SQL statements."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_describe_parameter_encryption
              [ @tsql = ]
              N
              'tsql'
              [ , [ @params = ]
              N
              '@parameter_name data_type [ , ... n ]'
              ]
              [ ; ]
---

## Description

2016 (13.x) and later Analyzes the specified Transact-SQL statement and its parameters, to determine which parameters correspond to database columns that are protected by using the Always Encrypted feature. Returns encryption metadata for the parameters that correspond to encrypted columns. One or more Transact-SQL statements. provides a declaration string for parameters for A string that contains the definitions of all parameters that are embedded in the Transact-

## Syntax

```sql
sp_describe_parameter_encryption
[ @tsql = ]
N
'tsql'
[ , [ @params = ]
N
'@parameter_name data_type [ ,. n ]'
]
[ ; ]
```

## Examples

### Example 1

`sp_describe_parameter_encryption`

### Example 2

```sql
VIEW ANY COLUMN ENCRYPTION KEY DEFINITION
```

### Example 3

```sql
VIEW ANY COLUMN MASTER KEY
DEFINITION
```

### Example 4

`ENCRYPTED_VALUE`

### Example 5

```sql
CREATE
COLUMN
MASTER
KEY
[CMK1]
WITH (
KEY_STORE_PROVIDER_NAME = N
'MSSQL_CERTIFICATE_STORE'
,
KEY_PATH = N
'CurrentUser/my/A66BB0F6DD70BDFF02B62D0F87E340288E6F9305'
);
GO
CREATE
COLUMN
ENCRYPTION
KEY
[CEK1]
WITH
VALUES (
COLUMN_MASTER_KEY = [CMK1],
ALGORITHM =
'RSA_OAEP'
,
ENCRYPTED_VALUE = 0x016E00000163007500720072<.>
-- truncated in this example
);
GO
CREATE
TABLE t1 (
c1
INT
ENCRYPTED
WITH (
COLUMN_ENCRYPTION_KEY = [CEK1],
ENCRYPTION_TYPE = Randomized,
ALGORITHM =
'AEAD_AES_256_CBC_HMAC_SHA_256'
)
NULL
,
);
EXECUTE sp_describe_parameter_encryption
N
'INSERT INTO t1 VALUES(@c1)'
,
N
'@c1 INT'
;
```
