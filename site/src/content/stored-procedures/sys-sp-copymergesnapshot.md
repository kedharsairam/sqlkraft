---
name: "sys.sp_copymergesnapshot"
title: "sp_copymergesnapshot"
category: "general"
description: "Copies the snapshot folder of the specified publication to the folder listed in the @destination_folder . This stored procedure is executed at the Publisher on the publication The name of the publication whose snapshot contents are to be copied. , with no default."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_copymergesnapshot
  [ @publication = ]
  N
  'publication'
  , [ @destination_folder = ]
  N
  'destination_folder'
  [ ; ]
---

## Description

Copies the snapshot folder of the specified publication to the folder listed in the @destination_folder. This stored procedure is executed at the Publisher on the publication The name of the publication whose snapshot contents are to be copied. , with no default.

## Syntax

```sql
sp_copymergesnapshot
[ @publication = ]
N
'publication'
, [ @destination_folder = ]
N
'destination_folder'
[ ; ]
```

## Permissions

is used in merge replication. Only members of the fixed server role or fixed database role can execute. Modify Snapshot Initialization Options for SQL Replication System stored procedures (Transact-SQL)
## Remarks

Azure SQL Managed Instance

Copies the snapshot folder of the specified publication to the folder listed in the

@destination_folder. This stored procedure is executed at the Publisher on the publication

The name of the publication whose snapshot contents are to be copied.

@publication

, with no default.

The name of the folder where the contents of the publication snapshot is to be copied.

@destination_folder

, with no default. The

@destination_folder

alternate location such as on another server, on a network drive, or on removable media (such

as CD-ROMs or removable disks).

(success) or
