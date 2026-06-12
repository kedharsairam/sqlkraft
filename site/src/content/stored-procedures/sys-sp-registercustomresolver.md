---
name: "sys.sp_registercustomresolver"
title: "sp_registercustomresolver"
category: "general"
description: "Registers a business logic handler or a COM-based custom resolver that can be invoked during the merge replication synchronization process. This stored procedure is executed at the Specifies the friendly name for the custom business logic being registered. Specifies the CLSID value of the COM object that being registered. This parameter must be set to a valid CLSI"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_registercustomresolver
              [ @article_resolver = ]
              N
              'article_resolver'
              [ , [ @resolver_clsid = ]
              N
              'resolver_clsid'
              ]
              [ , [ @is_dotnet_assembly = ]
              N
              'is_dotnet_assembly'
              ]
              [ , [ @dotnet_assembly_name = ]
              N
              'dotnet_assembly_name'
              ]
              [ , [ @dotnet_class_name = ]
              N
              'dotnet_class_name'
              ]
              [ ; ]
---

## Description

Registers a business logic handler or a COM-based custom resolver that can be invoked during the merge replication synchronization process. This stored procedure is executed at the Specifies the friendly name for the custom business logic being registered. Specifies the CLSID value of the COM object that being registered.

## Syntax

```sql
sp_registercustomresolver
[ @article_resolver = ]
N
'article_resolver'
[ , [ @resolver_clsid = ]
N
'resolver_clsid'
]
[ , [ @is_dotnet_assembly = ]
N
'is_dotnet_assembly'
]
[ , [ @dotnet_assembly_name = ]
N
'dotnet_assembly_name'
]
[ , [ @dotnet_class_name = ]
N
'dotnet_class_name'
]
[ ; ]
```
