---
name: "sys.sp_get_endpoint_certificate"
title: "sp_get_endpoint_certificate"
category: "general"
description: "Returns a public key of the certificate used for authentication on endpoint of specified type with certificate-based trust configured. Supported types of endpoints are Database Mirroring endpoint (also used for Link feature of Azure SQL Managed Instance) and Service Broker Type of endpoint for which certificate's public key is required. Arguments for extended stored"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_get_endpoint_certificate [ @endpoint_type = ] endpoint_type
              [ ; ]
---

## Description

Returns a public key of the certificate used for authentication on endpoint of specified type with certificate-based trust configured. Supported types of endpoints are Database Mirroring endpoint (also used for Link feature of Azure SQL Managed Instance) and Service Broker Type of endpoint for which certificate's public key is required.

## Syntax

```sql
sp_get_endpoint_certificate [ @endpoint_type = ] endpoint_type
[ ; ]
```
