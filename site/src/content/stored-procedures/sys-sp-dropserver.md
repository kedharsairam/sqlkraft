---
name: "sys.sp_dropserver"
title: "sp_dropserver"
category: "general"
description: "Removes a server from the list of known remote and linked servers on the local instance of SQL The server to be removed. , with no default. Indicates that related remote and linked server logins for must also be removed if , with a default of An error is returned if you run on a server with associated remote and linked server login entries"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_dropserver
      [ @server = ]
      N
      'server'
      [ , [ @droplogins = ]
      'droplogins'
      ]
      [ ; ]
---

## Description

Removes a server from the list of known remote and linked servers on the local instance of SQL The server to be removed. , with no default. Indicates that related remote and linked server logins for must also be removed if , with a default of An error is returned if you run on a server with associated remote and linked server login entries, or is configured as a replication publisher.

## Syntax

```sql
sp_dropserver
[ @server = ]
N
'server'
[ , [ @droplogins = ]
'droplogins'
]
[ ; ]
```

## Remarks

Removes a server from the list of known remote and linked servers on the local instance of SQL

The server to be removed.

, with no default.

must exist.

Indicates that related remote and linked server logins for

must also be removed if

@droplogins

is specified.

@droplogins

, with a default of

(success) or

An error is returned if you run

on a server with associated remote and linked

server login entries, or is configured as a replication publisher. To remove all remote and linked

server logins for a server when you remove the server, use the

@droplogins

## Examples

### Example 1

`sp_dropserver`

### Example 2

`sp_dropserver`

### Example 3

```sql
ALTER ANY LINKED SERVER
```

### Example 4

`ACCOUNTS`

### Example 5

```sql
EXECUTE sp_dropserver
'ACCOUNTS'
,
'droplogins'
;
```
