---
name: "sys.sp_create_snapshot"
title: "core.sp_create_snapshot"
category: "general"
description: "Inserts a row in the management data warehouse view. This procedure is called every time an upload package starts uploading data to the management data warehouse. The GUID for the collection set. obtain the GUID, query the dbo.syscollector_collection_sets view in the The GUID for a collector type. obtain the GUID, query the dbo.syscollector_collector_types view in t"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  core.sp_create_snapshot [ @collection_set_uid = ]
  'collection_set_uid'
  , [ @collector_type_uid = ]
  'collector_type_uid'
  , [ @machine_name = ]
  'machine_name'
  , [ @named_instance = ]
  'named_instance'
  , [ @log_id = ] log_id
  , [ @snapshot_id = ] snapshot_id
  OUTPUT
  [ ; ]
---

## Description

Inserts a row in the management data warehouse view. This procedure is called every time an upload package starts uploading data to the management data warehouse. The GUID for the collection set. obtain the GUID, query the dbo.syscollector_collection_sets view in the The GUID for a collector type.

## Syntax

```sql
core.sp_create_snapshot [ @collection_set_uid = ]
'collection_set_uid'
, [ @collector_type_uid = ]
'collector_type_uid'
, [ @machine_name = ]
'machine_name'
, [ @named_instance = ]
'named_instance'
, [ @log_id = ] log_id
, [ @snapshot_id = ] snapshot_id
OUTPUT
[ ; ]
```
