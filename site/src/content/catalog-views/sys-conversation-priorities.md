---
name: 'sys.conversation_priorities'
title: 'sys.conversation_priorities'
category: 'objects'
description: 'Contains a row for each conversation priority created in the current database, as shown in the'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Contains a row for each conversation priority created in the current database, as shown in the

following table:


## Description
Priority_id

A number that uniquely identifies the conversation priority. Not

NULLABLE.

name

Name of the conversation priority. Not NULLABLE.

service_contract_id

The identifier of the contract that is specified for the

conversation priority. This can be joined on the

service_contract_id column in sys.service_contracts. NULLABLE.

local_service_id

The identifier of the service that is specified as the local service

for the conversation priority. This column can be joined on the

service_id column in sys.services. NULLABLE.

remote_service_name

The name of the service that is specified as the remote service

for the conversation priority. NULLABLE.

priority

The priority level that is specified in this conversation priority.

Not NULLABLE.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following example lists the conversation priorities by using joins to show the contract and

local service names.

ﾉ

Expand table

ALTER BROKER PRIORITY (Transact-SQL)

CREATE BROKER PRIORITY (Transact-SQL)

DROP BROKER PRIORITY (Transact-SQL)

sys.services (Transact-SQL)

sys.service_contracts (Transact-SQL)

See Also

```sql
SELECT scp.name AS priority_name,
ssc.name AS contract_name,
```

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
