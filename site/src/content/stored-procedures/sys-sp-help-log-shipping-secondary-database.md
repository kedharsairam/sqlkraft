---
name: 'sys.sp_help_log_shipping_secondary_database'
title: 'sp_help_log_shipping_secondary_database'
category: 'general'
description: 'This stored procedure retrieves the settings for one or more secondary databases. Transact-SQL syntax conventions The name of the secondary database. The ID for the secondary server in the log shipping configuration.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_log_shipping_secondary_database
  [ [ @secondary_database = ]
  N
  'secondary_database'
  ]
  [ , [ @secondary_id = ]
  'secondary_id'
  ]
  [ ; ]
---

## Description

This stored procedure retrieves the settings for one or more secondary databases. Transact-SQL syntax conventions The name of the secondary database. The ID for the secondary server in the log shipping configuration.

## Syntax

```sql
sp_help_log_shipping_secondary_database
[ [ @secondary_database = ]
N
'secondary_database'
]
[ , [ @secondary_id = ]
'secondary_id'
]
[ ; ]
```

## Permissions

If you include the @secondary_database parameter, the result set contains information about that secondary database; if you include the @secondary_id parameter, the result set contains information about all secondary databases associated with that secondary ID. must be run from the database on the secondary server. Only members of the fixed server role can run this procedure. sp_help_log_shipping_secondary_primary (Transact-SQL) About log shipping (SQL Server) System stored procedures (Transact-SQL) Related content sp_help_log_shipping_primary_secondary sp_help_log_shipping_secondary_database sp_help_log_shipping_secondary_primary sp_refresh_log_shipping_monitor About log shipping (SQL Server) System stored procedures (Transact-SQL) Related content
