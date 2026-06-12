---
name: "General Remarks"
title: "General Remarks"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

For descriptions of the RESTORE VERIFYONLY arguments, see

RESTORE Arguments (Transact-

SQL).

The media set or the backup set must contain minimal correct information to enable it to be

interpreted as Microsoft Tape Format. If not, RESTORE VERIFYONLY stops and indicates that the

format of the backup is invalid.

Checks performed by RESTORE VERIFYONLY include:

That the backup set is complete and all volumes are readable.

Some header fields of database pages, such as the page ID (as if it were about to write

the data).

７

Note

URL is the format used to specify the location and the file name for Microsoft Azure Blob

Storage and is supported starting with SQL Server 2012 (11.x) SP1 CU2. Although

Microsoft Azure storage is a service, the implementation is similar to disk and tape to

allow for a consistent and seamless restore experience for all the three devices.

## File-Snapshot

## Backups for Database Files in Azure

```sql
| {
STOP
_
ON
_
ERROR
|
CONTINUE
_
AFTER
_
ERROR
}
--Monitoring Options
|
STATS
[ = percentage ]
--Tape Options
| {
REWIND
|
NOREWIND
}
| {
UNLOAD
|
NOUNLOAD
}
} [ ,.n ]
]
[;]
<backup_device>
::=
{
{ logical_backup_device_name |
@logical_backup_device_name_var }
| {
DISK
|
TAPE
|
URL
} = {
'physical_backup_device_name'
|
@physical_backup_device_name_var }
}
```
