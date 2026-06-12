---
name: "sys.sp_syscollector_create_collector_type"
title: "sp_syscollector_create_collector_type"
category: "general"
description: "Creates a collector type for the data collector. A collector type is a logical wrapper around the SSIS packages that provide the actual mechanism for collecting data and uploading it to the The GUID for the collector type. is an OUTPUT parameter of type it will be automatically created and returned as The name of the collector type. The XML schema for this collector"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_create_collector_type
              [ [ @collector_type_uid = ]
              'collector_type_uid'
              OUTPUT
              ]
              , [ @name = ]
              N
              'name'
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

Creates a collector type for the data collector. A collector type is a logical wrapper around the SSIS packages that provide the actual mechanism for collecting data and uploading it to the The GUID for the collector type. is an OUTPUT parameter of type it will be automatically created and returned as The name of the collector type. The XML schema for this collector type.

## Syntax

```sql
sp_syscollector_create_collector_type
[ [ @collector_type_uid = ]
'collector_type_uid'
OUTPUT
]
, [ @name = ]
N
'name'
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
