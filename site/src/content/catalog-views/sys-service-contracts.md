---
name: "sys.service_contracts"
title: "sys.service_contracts"
category: "compatibility"
description: "This catalog view contains a row for each contract in the database."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  ssvc.name AS local_service_name,
  scp.remote_service_name,
  scp.priority AS priority_level
  FROM sys.conversation_priorities AS scp
  INNER JOIN sys.service_contracts AS ssc
  ON scp.service_contract_id = ssc.service_contract_id
  INNER JOIN sys.services AS ssvc
  ON scp.local_service_id = ssvc.service_id
  ORDER BY priority_name, contract_name,
  local_service_name, remote_service_name;
---

## Description

This catalog view contains a row for each contract in the database.

## Syntax

```sql
ssvc.name AS local_service_name,
scp.remote_service_name,
scp.priority AS priority_level
FROM sys.conversation_priorities AS scp
INNER JOIN sys.service_contracts AS ssc
ON scp.service_contract_id = ssc.service_contract_id
INNER JOIN sys.services AS ssvc
ON scp.local_service_id = ssvc.service_id
ORDER BY priority_name, contract_name,
local_service_name, remote_service_name;
```

## Permissions

Article • 02/28/2023 Description Name of the contract, unique within the database. Not NULLABLE. Identifier of the contract. Not NULLABLE. Identifier for the database principal that owns this contract. NULLABLE. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. ﾉ Expand table ALTER BROKER PRIORITY (Transact-SQL) CREATE BROKER PRIORITY (Transact-SQL) DROP BROKER PRIORITY (Transact-SQL) sys.services (Transact-SQL) sys.service_contracts (Transact-SQL) See Also
