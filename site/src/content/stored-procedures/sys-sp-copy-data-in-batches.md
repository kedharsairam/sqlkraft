---
name: 'sys.sp_copy_data_in_batches'
title: 'sys.sp_copy_data_in_batches'
category: 'general'
description: 'SQL Server 2022 (16.x)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

A SQL Server client driver, supporting Always Encrypted, automatically calls

to retrieve encryption metadata for parameterized queries

issued by the application. Then, the driver uses the encryption metadata to encrypt the values of

parameters that correspond to database columns protected with Always Encrypted. It substitutes

the plaintext parameter values submitted by the application, with the encrypted parameter

values, before sending the query to the database engine.

Require the

and


## permissions in the database.
The following example truncates the value for

, for display purposes.

SQL

Here's the first result set:

1

5

1

1

Here's the second result set:

1

@c1

1

1

1

1

Always Encrypted

Develop applications using Always Encrypted

ﾉ

Expand table

ﾉ

Expand table

Related content

```sql
sp_describe_parameter_encryption
```

```sql
VIEW ANY COLUMN ENCRYPTION KEY DEFINITION
```

```sql
VIEW ANY COLUMN MASTER KEY
DEFINITION
```

```sql
ENCRYPTED_VALUE
```

```sql
CREATE
COLUMN
MASTER
KEY
[CMK1]
WITH
(
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
VALUES
(
COLUMN_MASTER_KEY = [CMK1],
ALGORITHM =
'RSA_OAEP'
,
ENCRYPTED_VALUE = 0x016E00000163007500720072<...>
-- truncated in this example
);
GO
CREATE
TABLE
t1 (
c1
INT
ENCRYPTED
WITH
(
COLUMN_ENCRYPTION_KEY = [CEK1],
ENCRYPTION_TYPE = Randomized,
ALGORITHM =
'AEAD_AES_256_CBC_HMAC_SHA_256'
)
NULL
,
);
EXECUTE
sp_describe_parameter_encryption
N
'INSERT INTO t1 VALUES(@c1)'
,
N
'@c1 INT'
;
```

```sql
column_encryption_key_ordinal
```

```sql
database_id
```

```sql
column_encryption_key_id
```

```sql
column_encryption_key_version
```

```sql
column_encryption_key_metadata_version
0x99EDA60083A50000
column_encryption_key_encrypted_value
0x016E00000163007500720072<...>
column_master_key_store_provider_name
MSSQL_CERTIFICATE_STORE
column_master_key_path
CurrentUser/my/A66BB0F6DD70BDFF02B62D0F87E340288E6F9305
column_encryption_key_encryption_algorithm_name
RSA_OAEP
```

```sql
parameter_ordinal
```

```sql
parameter_name
```

```sql
column_encryption_algorithm
```

```sql
column_encryption_type
```

```sql
column_encryption_key_ordinal
```

```sql
column_encryption_normalization_rule_version
```
