---
name: "sys.sp_droplinkedsrvlogin"
title: "sp_droplinkedsrvlogin"
category: "general"
description: "Removes an existing mapping between a login on the local server running SQL Server, and a login on the linked server. Transact-SQL syntax conventions The name of a linked server that the SQL Server login mapping applies to. , with no default. The SQL Server login on the local server that's a mapping to the linked server , with no default. A mapping for already exist."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_droplinkedsrvlogin
  [ @rmtsrvname = ]
  N
  'rmtsrvname'
  , [ @locallogin = ]
  N
  'locallogin'
  [ ; ]
---

## Description

Removes an existing mapping between a login on the local server running SQL Server, and a login on the linked server. Transact-SQL syntax conventions The name of a linked server that the SQL Server login mapping applies to. , with no default. The SQL Server login on the local server that's a mapping to the linked server , with no default. A mapping for already exist. If , the default mapping created by , which maps all logins on the local server to logins on the linked server, is deleted. Security stored procedures (Transact-SQL) sp_addlinkedserver (Transact-SQL) sp_droplinkedsrvlogin (Transact-SQL) System stored procedures (Transact-SQL) Related content

## Syntax

```sql
sp_droplinkedsrvlogin
[ @rmtsrvname = ]
N
'rmtsrvname'
, [ @locallogin = ]
N
'locallogin'
[ ; ]
```

## Remarks

Applies to:

Removes an existing mapping between a login on the local server running SQL Server, and a

login on the linked server.

Transact-SQL syntax conventions

The name of a linked server that the SQL Server login mapping applies to.

@rmtsrvname

, with no default.

The SQL Server login on the local server that's a mapping to the linked server

@rmtsrvname

@locallogin

, with no default. A mapping for

@locallogin

@rmtsrvname

already exist. If

, the default mapping created by

, which maps all

logins on the local server to logins on the linked server, is deleted.

(success) or

Security stored procedures (Transact-SQL)

sp_addlinkedserver (Transact-SQL)

sp_droplinkedsrvlogin (Transact-SQL)

System stored procedures (Transact-SQL)

Related content
