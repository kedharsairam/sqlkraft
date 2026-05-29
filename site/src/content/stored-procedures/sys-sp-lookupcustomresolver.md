---
name: 'sys.sp_lookupcustomresolver'
title: 'sp_lookupcustomresolver'
category: 'general'
description: 'Returns the information on a business logic handler or the class identifier (CLSID) value of a COM-based custom resolver component that is registered at the Distributor. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions Specifies the name of the custom business logic being unregistered. , with no default. If the business logic being rem'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_lookupcustomresolver
  [ @article_resolver = ]
  N
  'article_resolver'
  , [ @resolver_clsid = ]
  N
  'resolver_clsid'
  OUTPUT
  [ , [ @is_dotnet_assembly = ] is_dotnet_assembly
  OUTPUT
  ]
  [ , [ @dotnet_assembly_name = ]
  N
  'dotnet_assembly_name'
  OUTPUT
  ]
  [ , [ @dotnet_class_name = ]
  N
  'dotnet_class_name'
  OUTPUT
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Returns the information on a business logic handler or the class identifier (CLSID) value of a COM-based custom resolver component that is registered at the Distributor. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions Specifies the name of the custom business logic being unregistered. , with no default. If the business logic being removed is a COM component, then

## Syntax

```sql
sp_lookupcustomresolver
[ @article_resolver = ]
N
'article_resolver'
, [ @resolver_clsid = ]
N
'resolver_clsid'
OUTPUT
[ , [ @is_dotnet_assembly = ] is_dotnet_assembly
OUTPUT
]
[ , [ @dotnet_assembly_name = ]
N
'dotnet_assembly_name'
OUTPUT
]
[ , [ @dotnet_class_name = ]
N
'dotnet_class_name'
OUTPUT
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
