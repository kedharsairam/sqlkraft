---
name: "sys.sp_unbindefault"
title: "sp_unbindefault"
category: "general"
description: "Removes one or more user-defined defaults from the current database. : SQL Server ( SQL Server 2016 (13.x) through current version Conditionally drops the default only if it already exists. Is the name of the schema to which the default belongs. Is the name of an existing default. To see a list of defaults that exist, execute must comply w"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_unbindefault
      [ @objname = ]
      N
      'objname'
      [ , [ @futureonly = ]
      'futureonly'
      ]
      [ ; ]
---

## Description

Removes one or more user-defined defaults from the current database. : SQL Server ( SQL Server 2016 (13.x) through current version Conditionally drops the default only if it already exists. Is the name of the schema to which the default belongs. Is the name of an existing default. To see a list of defaults that exist, execute must comply with the rules for. Specifying the default schema name is optional. Before dropping a default, unbind the default by executing if the default is currently bound to a column or an alias data type. DROP DEFAULT will be removed in the next version of Microsoft SQL Server. Do not use DROP DEFAULT in new development work, and plan to modify applications that currently use them. Instead, use default definitions that you can create by using the DEFAULT CREATE DEFAULT (Transact-SQL)

## Syntax

```sql
sp_unbindefault
[ @objname = ]
N
'objname'
[ , [ @futureonly = ]
'futureonly'
]
[ ; ]
```

## Remarks

Removes one or more user-defined defaults from the current database.

: SQL Server ( SQL Server 2016 (13.x) through

current version

Conditionally drops the default only if it already exists.

schema_name

Is the name of the schema to which the default belongs.

default_name

Is the name of an existing default. To see a list of defaults that exist, execute

must comply with the rules for

identifiers. Specifying the default schema name is optional.

Before dropping a default, unbind the default by executing

if the default is

currently bound to a column or an alias data type.

DROP DEFAULT will be removed in the next version of Microsoft SQL Server. Do not use

DROP DEFAULT in new development work, and plan to modify applications that currently

use them. Instead, use default definitions that you can create by using the DEFAULT

CREATE DEFAULT (Transact-SQL)

sp_helptext (Transact-SQL)

sp_help (Transact-SQL)

sp_unbindefault (Transact-SQL)
