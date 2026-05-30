---
name: "sys.dm_column_encryption_enclave"
title: "sys.dm_column_encryption_enclave"
category: "io"
description: "SQL Server 2019 (15.x) and later - Windows only Returns performance counters for the secure enclave for Always Encrypted. For more Always Encrypted with secure enclaves If the enclave is configured and has been correctly initialized after the last restart of SQL Server, the view contains exactly one row. If the enclave is not configured or it has not been correctly initialized, the view returns no"
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT
  *
  FROM
  sys.dm_column_encryption_enclave;
---

## Description

SQL Server 2019 (15.x) and later - Windows only Returns performance counters for the secure enclave for Always Encrypted. For more Always Encrypted with secure enclaves If the enclave is configured and has been correctly initialized after the last restart of SQL Server, the view contains exactly one row. If the enclave is not configured or it has not been correctly initialized, the view returns no rows.

## Syntax

```sql
SELECT
*
FROM
sys.dm_column_encryption_enclave;
```

## Examples

### Example 1

```sql
VIEW SERVER STATE
```

### Example 2

```sql
SELECT
*
FROM
sys.dm_column_encryption_enclave;
```
