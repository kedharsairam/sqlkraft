---
name: "sys.sp_mergemetadataretentioncleanup"
title: "sp_mergemetadataretentioncleanup"
category: "general"
description: "Performs a manual cleanup of metadata in the MSmerge_past_partition_mappings MSmerge_current_partition_mappings system tables. This stored procedure is executed at each Publisher and Subscriber in the topology."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_mergemetadataretentioncleanup
  [ [ @num_genhistory_rows = ] num_genhistory_rows
  OUTPUT
  ]
  [ , [ @num_contents_rows = ] num_contents_rows
  OUTPUT
  ]
  [ , [ @num_tombstone_rows = ] num_tombstone_rows
  OUTPUT
  ]
  [ , [ @aggressive_cleanup_only = ] aggressive_cleanup_only ]
  [ ; ]
---

## Description

Performs a manual cleanup of metadata in the MSmerge_past_partition_mappings MSmerge_current_partition_mappings system tables. This stored procedure is executed at each Publisher and Subscriber in the topology.

## Syntax

```sql
sp_mergemetadataretentioncleanup
[ [ @num_genhistory_rows = ] num_genhistory_rows
OUTPUT
]
[ , [ @num_contents_rows = ] num_contents_rows
OUTPUT
]
[ , [ @num_tombstone_rows = ] num_tombstone_rows
OUTPUT
]
[ , [ @aggressive_cleanup_only = ] aggressive_cleanup_only ]
[ ; ]
```
