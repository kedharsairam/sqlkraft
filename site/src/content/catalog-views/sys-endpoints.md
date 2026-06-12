---
name: "sys.endpoints"
title: "sys.endpoints"
category: "compatibility"
description: "Returns one row per endpoint created in the system. There's always exactly one SYSTEM Name of the endpoint. Unique within the server. Not nullable."
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: "sys.database_mirroring_endpoints"
---

## Description

Returns one row per endpoint created in the system. There's always exactly one SYSTEM Name of the endpoint. Unique within the server. Not nullable.

## Syntax

`sys.database_mirroring_endpoints`

## Permissions

Values correspond to the endpoint payload types in sys.endpoints system catalog view. If any other integer value is provided, stored procedure returns. (success) or (failure). Description Public key of the certificate, in binary format If authentication type configured on the endpoint isn't certificate-based, stored procedure returns error. User must have permission on the endpoint to execute. ﾉ Expand table
