---
name: "sys.sp_helpdistpublisher"
title: "sp_helpdistpublisher"
category: "general"
description: "Returns properties of the Publishers using a Distributor. This stored procedure is executed at the Distributor on any database. Specifies the Publisher for which properties are returned. Identified for informational purposes only. Not supported. Future compatibility is not Distribution database for the specified Publisher."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpdistpublisher
  [ [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @check_user = ] check_user ]
  [ ; ]
---

## Description

Returns properties of the Publishers using a Distributor. This stored procedure is executed at the Distributor on any database. Specifies the Publisher for which properties are returned. Identified for informational purposes only. Not supported. Future compatibility is not Distribution database for the specified Publisher.

## Syntax

```sql
sp_helpdistpublisher
[ [ @publisher = ]
N
'publisher'
]
[ , [ @check_user = ] check_user ]
[ ; ]
```
