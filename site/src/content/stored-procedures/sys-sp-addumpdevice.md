---
name: "sys.sp_addumpdevice"
title: "sp_addumpdevice"
category: "general"
description: "Adds a backup device to an instance of SQL Server. , with no default, and can be one of the Hard disk file as a backup device. Any tape devices supported by Microsoft Windows. : Support for tape backup devices will be removed in a future version of SQL Server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addumpdevice
  [ @devtype = ]
  'devtype'
  , [ @logicalname = ]
  N
  'logicalname'
  , [ @physicalname = ]
  N
  'physicalname'
  [ , [ @cntrltype = ] cntrltype ]
  [ , [ @devstatus = ]
  'devstatus'
  ]
  [ ; ]
---

## Description

Adds a backup device to an instance of SQL Server. , with no default, and can be one of the Hard disk file as a backup device. Any tape devices supported by Microsoft Windows. : Support for tape backup devices will be removed in a future version of SQL Server.

## Syntax

```sql
sp_addumpdevice
[ @devtype = ]
'devtype'
, [ @logicalname = ]
N
'logicalname'
, [ @physicalname = ]
N
'physicalname'
[ , [ @cntrltype = ] cntrltype ]
[ , [ @devstatus = ]
'devstatus'
]
[ ; ]
```

## Arguments

Rewinds and closes specified tape devices that were left open by BACKUP or RESTORE

statements executed with the NOREWIND option. This command is supported only for tape

Specifies the logical or physical backup devices to use for the restore operation.

logical_backup_device_name

logical_backup_device_name_var

Is the logical name, which must follow the rules for identifiers, of the backup devices created by

from which the database is restored. If supplied as a variable

logical_backup_device_name_var

), the backup device name can be specified either as a string

logical_backup_device_name_var

logical_backup_device_name

) or as a variable of

character string data type, except for the

data types.

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

SQL*AltDiction_CP1253*

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

_(. and 18 more arguments)_
