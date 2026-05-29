---
name: 'sys.backup_devices'
title: 'sys.backup_devices'
category: 'compatibility'
description: '105 = A permanent backup device. All permanent device names and device numbers can be Physical block size used to write the media family. Can be Mirror number (0-3). RESTORE VERIFYONLY FROM WITH LOADHISTORY populates the columns of the table with the appropriate values from the media-set header. To reduce the number of rows in this table and in other backup and history tables, execute the sp_delet'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  sp_helpdevice [ [ @devname = ]
  N
  'devname'
  ]
  [ ; ]
---

## Description

105 = A permanent backup device. All permanent device names and device numbers can be Physical block size used to write the media family. Can be Mirror number (0-3). RESTORE VERIFYONLY FROM WITH LOADHISTORY populates the columns of the table with the appropriate values from the media-set header. To reduce the number of rows in this table and in other backup and history tables, execute the sp_delete_backuphistory stored procedure. Backup and Restore Tables (Transact-SQL) backupfile (Transact-SQL) backupfilegroup (Transact-SQL) backupmediaset (Transact-SQL) backupset (Transact-SQL) System Tables (Transact-SQL) Deprecated feature BACKUP { DATABASE | LOG } TO device_that_is_a_disk Korean_Wansung_Unicode Lithuanian_Classic SQL_AltDiction_CP1253_CS_AS None. These collations exist in SQL Server 2005

## Syntax

```sql
sp_helpdevice [ [ @devname = ]
N
'devname'
]
[ ; ]
```

## Remarks

Description

105 = A permanent backup device.

Can be NULL.

All permanent device names and device numbers can be

Physical block size used to write the media family. Can be

Mirror number (0-3).

RESTORE VERIFYONLY FROM

backup_device

WITH LOADHISTORY populates the columns of the

table with the appropriate values from the media-set header.

To reduce the number of rows in this table and in other backup and history tables, execute the

sp_delete_backuphistory

stored procedure.

Backup and Restore Tables (Transact-SQL)

backupfile (Transact-SQL)

backupfilegroup (Transact-SQL)

backupmediaset (Transact-SQL)

backupset (Transact-SQL)

System Tables (Transact-SQL)

Deprecated feature

Replacement

Feature name

BACKUP { DATABASE | LOG } TO

device_that_is_a_disk

Korean_Wansung_Unicode

Lithuanian_Classic

SQL_AltDiction_CP1253_CS_AS

None. These collations exist in SQL Server 2005

(9.x), but aren't visible through

fn_helpcollations.

Korean_Wansung_Unico

Lithuanian_Classic

SQL_AltDiction_CP1253_

These collations exist in SQL Server 2005 (9.x)

and higher, but aren't visible through

fn_helpcollations. Use Macedonian_FYROM_90

and Indic_General_90 instead.

Azeri_Latin_90

Azeri_Cyrilllic_90

Azeri_Latin_100

Azeri_Cyrilllic_100

Azeri_Latin_90

Azeri_Cyrilllic_90

Configuration

database option

database option

database option

CONCAT_NULLS_YIELDS_NULL are always set to

will be unavailable.

data type syntax

Ability to insert null values into

'text in row' table option

varchar(max)

nvarchar(max)

varbinary(max)

data types. For more

information, see

sp_tableoption

Text in row table option

Data types:

varchar(max)

nvarchar(max)

varbinary(max)

data types.

Data types:

statement with the

option. To rebuild multiple log files,

when one or more have a new location, use the

sp_attach_single_file_db

sp_bindefault

CREATE_DROP_DEFAULT
