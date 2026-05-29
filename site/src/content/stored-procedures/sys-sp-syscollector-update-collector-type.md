---
name: "sys.sp_syscollector_update_collector_type"
title: "sp_syscollector_update_collector_type"
category: "general"
description: "Updates a collector type for a collection item. Given the name and GUID of a collector type, updates the collector type configuration, including the collection and upload package, the parameter schema, and the parameter formatter schema. Transact-SQL syntax conventions The GUID for the collector type. is automatically created and returned as OUTPUT. The name of the collector type. The XML schema f"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_update_collector_type
  [ [ @collector_type_uid = ]
  'collector_type_uid'
  ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ , [ @parameter_schema = ]
  N
  'parameter_schema'
  ]
  [ , [ @parameter_formatter = ]
  N
  'parameter_formatter'
  ]
  , [ @collection_package_id = ]
  'collection_package_id'
  , [ @upload_package_id = ]
  'upload_package_id'
  [ ; ]
---

## Description

Updates a collector type for a collection item. Given the name and GUID of a collector type, updates the collector type configuration, including the collection and upload package, the parameter schema, and the parameter formatter schema. Transact-SQL syntax conventions The GUID for the collector type. is automatically created and returned as OUTPUT. The name of the collector type. The XML schema for this collector type.

## Syntax

```sql
sp_syscollector_update_collector_type
[ [ @collector_type_uid = ]
'collector_type_uid'
]
[ , [ @name = ]
N
'name'
]
[ , [ @parameter_schema = ]
N
'parameter_schema'
]
[ , [ @parameter_formatter = ]
N
'parameter_formatter'
]
, [ @collection_package_id = ]
'collection_package_id'
, [ @upload_package_id = ]
'upload_package_id'
[ ; ]
```
