---
name: "sys.conversation_priorities"
title: "sys.conversation_priorities"
category: "compatibility"
description: "Contains a row for each conversation priority created in the current database, as shown in the A number that uniquely identifies the conversation priority. Not Name of the conversation priority. Not NULLABLE. The identifier of the contract that is specified for the conversation priority. This can be joined on the service_contract_id column in sys.service_contracts. NULLABLE. The identifier of the "
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT scp.name AS priority_name,
  ssc.name AS contract_name,
---

## Description

Contains a row for each conversation priority created in the current database, as shown in the A number that uniquely identifies the conversation priority. Not Name of the conversation priority. Not NULLABLE. The identifier of the contract that is specified for the conversation priority. This can be joined on the service_contract_id column in sys.service_contracts. NULLABLE. The identifier of the service that is specified as the local service

## Syntax

```sql
SELECT scp.name AS priority_name,
ssc.name AS contract_name,
```

## Examples

### Example 1

```sql
SELECT scp.name AS priority_name,
ssc.name AS contract_name,
```

### Example 2

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
