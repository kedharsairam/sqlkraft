---
name: 'sys.sp_xtp_merge_checkpoint_files'
title: 'sys.sp_xtp_merge_checkpoint_files'
category: 'general'
description: 'Merges all data and delta files in the transaction range specified.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

error is generated for an invalid transaction ID.

The

upper bound of transactions for a data file as shown in

sys.dm_db_xtp_checkpoint_files

. An error is generated for an invalid transaction ID.

None.

None.

Requires

fixed server role and the

fixed database role.

Merges all data and delta files in the valid range to produce a single data and delta file. This

procedure doesn't honor the merge policy.

System stored procedures (Transact-SQL)

In-Memory OLTP overview and usage scenarios

Related content
