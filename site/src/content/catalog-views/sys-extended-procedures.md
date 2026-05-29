---
name: 'sys.extended_procedures'
title: 'sys.extended_procedures'
category: 'objects'
description: 'Contains a row for each object that is an extended stored procedure, with'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

04/12/2024

Applies to:

SQL Server

Contains a row for each object that is an extended stored procedure, with

=

. Because extended stored procedures are installed into the

database, they're only visible from that database context. Selecting from the

view in any other database context returns an empty result set.


## Description
Columns inherited from

For a list of columns that this view inherits, see

sys.objects

.

Name, including path, of the DLL for this extended

stored procedure.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

System catalog views (Transact-SQL)

ﾉ

Expand table

Related content

```sql
sys.all_objects.type
```

```sql
X
```

```sql
master
```

```sql
sys.extended_procedures
```

```sql
sys.objects
```

```sql
dll_name
```
