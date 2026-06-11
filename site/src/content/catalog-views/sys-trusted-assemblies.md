---
name: "sys.trusted_assemblies"
title: "sys.trusted_assemblies (T-SQL)"
category: "compatibility"
description: "Azure SQL Managed Instance Contains a row for each trusted assembly for the server. Transact-SQL syntax conventions SHA2_512 hash of the assembly content. Optional user-defined description of the assembly. We recommend using the canonical name that encodes the simple name, version number, culture, public key, and architecture of the assembly to trust."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  sys.assemblies.
  create_date
---

## Description

Azure SQL Managed Instance Contains a row for each trusted assembly for the server. Transact-SQL syntax conventions SHA2_512 hash of the assembly content. Optional user-defined description of the assembly. We recommend using the canonical name that encodes the simple name, version number, culture, public key, and architecture of the assembly to trust. This value uniquely identifies the assembly on the common language runtime (CLR) side and is the same as the Date the assembly was added to the list of trusted assemblies. Login name of the principal who added the assembly to the list. SQL Server 2019 (15.x) and previous versions require permission on the SQL Server 2022 (16.x) and later versions require sys.sp_add_trusted_assembly sys.sp_drop_trusted_assembly assemblies from sys.sp_add_trusted_assembly

## Syntax

```sql
sys.assemblies.
create_date
```

## Remarks

Applies to:

Azure SQL Managed Instance

Contains a row for each trusted assembly for the server.

Transact-SQL syntax conventions

Description

SHA2_512 hash of the assembly content.

Optional user-defined description of the assembly. We recommend

using the canonical name that encodes the simple name, version

number, culture, public key, and architecture of the assembly to trust.

This value uniquely identifies the assembly on the common language

runtime (CLR) side and is the same as the

Date the assembly was added to the list of trusted assemblies.

Login name of the principal who added the assembly to the list.

SQL Server 2019 (15.x) and previous versions require

permission on the

SQL Server 2022 (16.x) and later versions require

permission on

the server.

sys.sp_add_trusted_assembly

to add, and

sys.sp_drop_trusted_assembly

assemblies from

sys.sp_add_trusted_assembly

sys.sp_drop_trusted_assembly

Expand table

Related content
