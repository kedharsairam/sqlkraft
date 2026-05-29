---
name: 'Result Sets'
title: 'Result Sets'
category: 'statements'
description: 'For descriptions of the RESTORE LABELONLY arguments, see'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

For descriptions of the RESTORE LABELONLY arguments, see

RESTORE Arguments (Transact-

SQL)

.

The result set from RESTORE LABELONLY consists of a single row with this information.


## Description
Name of the media.

Unique identification number of the media set.

Number of media families in the media set.

Sequence number of this family.

Unique identification number for the media family.

Sequence number of this media in the media family.

Whether the media description contains:

= Microsoft Tape Format media label

= Media description

Media description, in free-form text, or the Tape Format

media label.

Name of the backup software that wrote the label.

７

Note

URL is the format used to specify the location and the file name for Microsoft Azure Blob

Storage and is supported starting with SQL Server 2012 (11.x) SP1 CU2. Although

Microsoft Azure storage is a service, the implementation is similar to disk and tape to

allow for a consistent and seamless restore experience for all the three devices.

ﾉ

Expand table

#### Column name

#### Data type

#### SoftwareVendorId

#### int

#### MediaDate

#### datetime

#### Mirror_Count

#### int

#### IsCompressed

#### bit

```sql
}
```
