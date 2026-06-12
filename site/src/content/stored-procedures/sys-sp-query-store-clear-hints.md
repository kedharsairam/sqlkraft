---
name: "sys.sp_query_store_clear_hints"
title: "sp_query_store_clear_hints"
category: "general"
description: "2022 (16.x) and later versions SQL database in Microsoft Fabric argument defaults to the local replica (primary or secondary), but you can optionally specify a value matching a value in the to clear a hint for a different replica group. Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_query_store_clear_hints
      [ @query_id = ] query_id
      [ , [ @replica_group_id = ]
      'replica_group_id'
      ]
      [ ; ]
---

## Description

2022 (16.x) and later versions SQL database in Microsoft Fabric argument defaults to the local replica (primary or secondary), but you can optionally specify a value matching a value in the to clear a hint for a different replica group. Arguments for extended stored procedures must be entered in the specific order as section.

## Syntax

```sql
sp_query_store_clear_hints
[ @query_id = ] query_id
[ , [ @replica_group_id = ]
'replica_group_id'
]
[ ; ]
```

## Return Columns

| Column Name | Data Type | Description |

|---|---|---|

| - | - | SQL Server 2022 (16.x) and later versions |

| - | - | Azure SQL Database |

| - | - | SQL Managed Instance |

| - | - | SQL database in Microsoft Fabric |

| - | - | Query Store hints |

| - | - | for a given query ID. |

| - | - | |

| - | - | sys.query_store_query |

| - | - | @replica_group_id |

| - | - | argument defaults to the local replica (primary or secondary), |

| - | - | but you can optionally specify a value matching a value in the |

| - | - | sys.query_store_replicas |

| - | - | to clear a hint for a different replica group. |

| - | - | @replica_group_id |

| - | - | Arguments for extended stored procedures must be entered in the specific order as |

| - | - | described in the |

| - | - | section. If the parameters are entered out of order, an error |
