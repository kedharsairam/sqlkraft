---
name: "Summary of support for WITH options"
title: "Summary of support for WITH options"
category: "queries"
description: "contains the backup from a single, successful backup operation. RESTORE, RESTORE"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

A

backup set

contains the backup from a single, successful backup operation. RESTORE, RESTORE

FILELISTONLY, RESTORE HEADERONLY, and RESTORE VERIFYONLY statements operate on a single backup

set within the media set on the specified backup device or devices. You should specify the backup you

need from within the media set. You can obtain the

backup_set_file_number

of a backup set by using the

RESTORE HEADERONLY

statement.

The option for specifying the backup set to restore is:

FILE

{

backup_set_file_number

|

backup_set_file_number

}

Where

backup_set_file_number

indicates the position of the backup in the media set. A

backup_set_file_number

of 1 (FILE = 1) indicates the first backup set on the backup medium and a

backup_set_file_number

of 2 (FILE = 2) indicates the second backup set, and so on.

The behavior of this option varies depending on the statement, as described in the following table:

Statement

Behavior of backup-set FILE option

RESTORE

The default backup set file number is 1. Only one backup-set FILE option is allowed in a RESTORE

statement. It is important to specify backup sets in order.

RESTORE

FILELISTONLY

The default backup set file number is 1.

RESTORE

HEADERONLY

By default, all backup sets in the media set are processed. The RESTORE HEADERONLY results set

## returns information about each backup set, including its

Position

in the media set. To return

information on a given backup set, use its position number as the

backup_set_file_number

value in

the FILE option.

Note: For tape media, RESTORE HEADER only processes backup sets on the loaded tape.

RESTORE

VERIFYONLY

The default

backup_set_file_number

is 1.

The following WITH options are supported by only the RESTORE statement: BLOCKSIZE, BUFFERCOUNT,

MAXTRANSFERSIZE, PARTIAL, KEEP_REPLICATION, { RECOVERY | NORECOVERY | STANDBY }, REPLACE,

RESTART, RESTRICTED_USER, and { STOPAT | STOPATMARK | STOPBEFOREMARK }

Expand table

７

Note

The FILE option for specifying a backup set is unrelated to the FILE option for specifying a database

file, FILE

{

logical_file_name_in_backup

|

logical_file_name_in_backup_var

}.

#### =
