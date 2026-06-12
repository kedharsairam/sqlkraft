---
name: "sys.dm_db_missing_index_group_stats"
title: "sys.dm_db_missing_index_group_stats"
category: "index"
description: "Average percentage benefit that user queries could experience if this missing index group was implemented. The value means that the query cost would on average drop by this percentage if this missing index group was implemented. Number of seeks caused by system queries, such as auto stats queries, that the recommended index in the group could have been used for. For more information, see Auto Stat"
tags: ["index", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_db_missing_index_group_stats"
---

## Description

Average percentage benefit that user queries could experience if this missing index group was implemented. The value means that the query cost would on average drop by this percentage if this missing index group was implemented. Number of seeks caused by system queries, such as auto stats queries, that the recommended index in the group could have been used for. For more information, see Auto Stats Event Class Number of scans caused by system queries that the recommended index in the group could have been used for.

## Syntax

`sys.dm_db_missing_index_group_stats`

## Remarks

Average percentage benefit that user queries could experience if this

missing index group was implemented. The value means that the

query cost would on average drop by this percentage if this missing

index group was implemented.

Number of seeks caused by system queries, such as auto stats

queries, that the recommended index in the group could have been

used for. For more information, see

Auto Stats Event Class

Number of scans caused by system queries that the recommended

index in the group could have been used for.

Date and time of last system seek caused by system queries that the

recommended index in the group could have been used for.

Date and time of last system scan caused by system queries that the

recommended index in the group could have been used for.

Average cost of the system queries that could be reduced by the

index in the group.

Average percentage benefit that system queries could experience if

this missing index group was implemented. The value means that

the query cost would on average drop by this percentage if this

missing index group was implemented.

Information returned by

is updated by every query

execution, not by every query compilation or recompilation. Usage statistics are not persisted

and are kept only until the database engine is restarted. Database administrators should

periodically make backup copies of the missing index information if they want to keep the

usage statistics after server recycling. Use the

sys.dm_os_sys_info

to find the last database engine startup time.

The result set for this DMV is limited to 600 rows. Each row contains one missing index. If

you have more than 600 missing indexes, you should address the existing missing indexes

so you can then view the newer ones.
