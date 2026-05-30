---
name: "sys.sp_browsemergesnapshotfolder"
title: "sp_browsemergesnapshotfolder"
category: "general"
description: "Returns the complete path for the latest snapshot generated for a merge publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication. , with no default. Full path to the snapshot directory."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_browsemergesnapshotfolder [ @publication = ]
  N
  'publication'
  [ ; ]
---

## Description

Returns the complete path for the latest snapshot generated for a merge publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication. , with no default. Full path to the snapshot directory.

## Syntax

```sql
sp_browsemergesnapshotfolder [ @publication = ]
N
'publication'
[ ; ]
```

## Permissions

is used in merge replication. If the publication is set up to generate snapshot files in both the Publisher working directory and Publisher snapshot folder, the result set contains two rows: the first row contains the publication snapshot folder, and the second row contains the publisher working directory. is useful for determining the directory where the merge snapshot files are generated. This folder/path and its contents can then be copied to removable media, and the snapshot used to synchronize a subscription from an alternate snapshot location. Only members of the fixed server role or fixed database role can execute . System stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Returns the complete path for the latest snapshot generated for a merge publication. This

stored procedure is executed at the Publisher on the publication database.

Transact-SQL syntax conventions

The name of the publication.

@publication

, with no default.

(success) or

Description

Full path to the snapshot directory.

Expand table
