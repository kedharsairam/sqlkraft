---
name: 'sys.fn_helpcollations'
title: 'sys.fn_helpcollations'
category: 'system'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric


## Returns a list of all supported collations.
Transact-SQL syntax conventions


## returns the following information.

## Description
Name

Standard collation name


## Description

## Description of the collation
SQL Server supports Windows collations. SQL Server also supports a limited number (<80) of

collations called SQL Server collations, that were developed before SQL Server supported

Windows collations. SQL Server collations are still supported for backward compatibility, but

shouldn't be used for new development work. For more information about Windows collations,

see

Windows Collation Name (Transact-SQL)

. For more information about collations, see

Collation and Unicode Support

.

The following example returns all collation names starting with the letter

and that are binary

sort collations.

ﾉ

Expand table

７

Note

SQL

Here's the result set.

COLLATE (Transact-SQL)

COLLATIONPROPERTY (Transact-SQL)

Collation and Unicode support

Last updated on 11/18/2025

Azure Synapse Analytics queries against fn_helpcollations() must be run in the master

database.

See Also

```sql
L
```

```sql
fn_helpcollations ()
```

```sql
SELECT
Name
, Description
FROM
fn_helpcollations()
WHERE
Name
like
'L%'
AND
Description
LIKE
'% binary sort'
;
Name                   Description
-------------------    ------------------------------------
Lao_100_BIN            Lao-100, binary sort
Latin1_General_BIN     Latin1-General, binary sort
Latin1_General_100_BIN Latin1-General-100, binary sort
Latvian_BIN            Latvian, binary sort
Latvian_100_BIN        Latvian-100, binary sort
Lithuanian_BIN         Lithuanian, binary sort
Lithuanian_100_BIN     Lithuanian-100, binary sort
(7 row(s) affected)
```
