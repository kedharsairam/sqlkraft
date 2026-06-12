---
name: "sys.assemblies"
title: "sys.assemblies"
category: "compatibility"
description: "SQL analytics endpoint in Microsoft Fabric Returns a row for each assembly."
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  EXECUTE
      sp_add_trusted_assembly
      0x8893AD6D78D14EE43DF482E2EAD44123E3A0B684A8873C3F7BF3B5E8D8F09503F3E62370CE742BBC
      96FE3394477214B84C7C1B0F7A04DCC788FA99C2C09DFCCC, N
      'pointudt, version=0.0.0.0,
      culture=neutral, publickeytoken=null, processorarchitecture=msil'
      ;
---

## Description

Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Returns a row for each assembly.

## Syntax

```sql
EXECUTE sp_add_trusted_assembly
0x8893AD6D78D14EE43DF482E2EAD44123E3A0B684A8873C3F7BF3B5E8D8F09503F3E62370CE742BBC
96FE3394477214B84C7C1B0F7A04DCC788FA99C2C09DFCCC, N
'pointudt, version=0.0.0.0,
culture=neutral, publickeytoken=null, processorarchitecture=msil'
;
```

## Permissions

Article • 05/23/2023 Returns a row for each assembly. Description Name of the assembly. Is unique within the database. ID of the principal that owns this assembly. Assembly identification number. Is unique within a database. Canonical string that encodes the simple name, version number, culture, public key, and architecture of the assembly. This value uniquely identifies the assembly on the common language runtime (CLR) side. Permission-set/security-level for assembly. 1 = Safe Access 2 = External Access 3 = Unsafe Access Description for permission-set/security-level for assembly. SAFE_ACCESS EXTERNAL_ACCESS UNSAFE_ACCESS 1 = Assembly is visible to register Transact-SQL entry points. 0 = Assembly is intended only for managed callers. That is, the assembly provides internal implementation for other assemblies in the database. Date the assembly was created or registered. Date the assembly was modified. ﾉ Expand table DROP ASSEMBLY (Transact-SQL) sys.assemblies sys.dm_clr_loaded_assemblies

## Examples

### Example 1

`clr_name`

### Example 2

`sys.assemblies`

### Example 3

`pointudt`

### Example 4

```sql
EXECUTE sp_add_trusted_assembly
0x8893AD6D78D14EE43DF482E2EAD44123E3A0B684A8873C3F7BF3B5E8D8F09503F3E62370CE742BBC
96FE3394477214B84C7C1B0F7A04DCC788FA99C2C09DFCCC, N
'pointudt, version=0.0.0.0,
culture=neutral, publickeytoken=null, processorarchitecture=msil'
;
```
