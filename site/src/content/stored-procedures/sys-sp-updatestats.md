---
name: "sys.sp_updatestats"
title: "sp_updatestats"
category: "general"
description: "against all user-defined and internal tables in the current database. For more information about UPDATE STATISTICS . For more information about statistics, see UPDATE STATISTICS isn't specified, updates statistics by using the default sampling. The with a default value of , by specifying the keyword, on all user- d"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_updatestats [ [ @resample = ]
              'resample'
              ]
---

## Description

against all user-defined and internal tables in the current database. For more information about UPDATE STATISTICS. For more information about statistics, see UPDATE STATISTICS isn't specified, updates statistics by using the default sampling. The with a default value of , by specifying the keyword, on all user- defined and internal tables in the database. displays messages that indicate its progress. When the update is completed, it reports that statistics are updated for all tables. updates statistics on disabled nonclustered indexes and doesn't update statistics on disabled clustered indexes.

## Syntax

```sql
sp_updatestats [ [ @resample = ]
'resample'
]
```

## Remarks

against all user-defined and internal tables in the current database.

For more information about

UPDATE STATISTICS. For more information

about statistics, see

(success) or

Specifies that

option of the

UPDATE STATISTICS

isn't specified,

updates statistics by using the default sampling. The

argument is

with a default value of

, by specifying the

keyword, on all user-

defined and internal tables in the database.

displays messages that indicate its

progress. When the update is completed, it reports that statistics are updated for all tables.

updates statistics on disabled nonclustered indexes and doesn't update

statistics on disabled clustered indexes.

For disk-based tables,

updates statistics based on the

information in the

sys.dm_db_stats_properties

catalog view, updating statistics where at least
