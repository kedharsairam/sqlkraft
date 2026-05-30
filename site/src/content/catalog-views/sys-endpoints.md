---
name: "sys.endpoints"
title: "sys.endpoints"
category: "compatibility"
description: "Returns one row per endpoint created in the system. There's always exactly one SYSTEM Name of the endpoint. Unique within the server. Not nullable. ID of the endpoint. Unique within the server. An endpoint with an ID less than 65536 is a system endpoint. Not nullable. ID of the server principal that created and owns this endpoint. 5 = Virtual Interface Adapter (VIA) Description of the endpoint pro"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.database_mirroring_endpoints"
---

## Description

Returns one row per endpoint created in the system. There's always exactly one SYSTEM Name of the endpoint. Unique within the server. Not nullable. ID of the endpoint. Unique within the server. An endpoint with an ID less than 65536 is a system endpoint. Not nullable. ID of the server principal that created and owns this endpoint. 5 = Virtual Interface Adapter (VIA) Description of the endpoint protocol. Nullable. One of the following

## Syntax

```sql
sys.database_mirroring_endpoints
```

## Permissions

Values correspond to the endpoint payload types in sys.endpoints system catalog view. If any other integer value is provided, stored procedure returns . (success) or (failure). Description Public key of the certificate, in binary format If authentication type configured on the endpoint isn't certificate-based, stored procedure returns error. User must have permission on the endpoint to execute . ﾉ Expand table
