---
name: "sys.sp_unregistercustomresolver"
title: "sp_unregistercustomresolver"
category: "general"
description: "Unregisters a previously registered business logic module. Business logic can be in the form of either a COM component or a Microsoft .NET Framework assembly. This stored procedure is executed on the Distributor where the custom business logic was registered. Transact-SQL syntax conventions Specifies the name of the custom business logic being unregistered. @article_resolver , with no default. If "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_unregistercustomresolver"
---

## Description

Unregisters a previously registered business logic module. Business logic can be in the form of either a COM component or a Microsoft .NET Framework assembly. This stored procedure is executed on the Distributor where the custom business logic was registered. Transact-SQL syntax conventions Specifies the name of the custom business logic being unregistered. @article_resolver , with no default. If the business logic being removed is a COM component, this parameter is the friendly name of the component. If the business logic is a .NET Framework assembly, this parameter is the name of the assembly. is used in merge replication. sp_enumcustomresolvers at any server in the replication topology to return the list of registered custom business logic modules or COM resolvers available to the topology.

## Syntax

`sp_unregistercustomresolver`

## Permissions

Only members of the fixed server role or fixed database role can execute . sp_lookupcustomresolver (Transact-SQL) sp_registercustomresolver (Transact-SQL) System stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Unregisters a previously registered business logic module. Business logic can be in the form of

either a COM component or a Microsoft .NET Framework assembly. This stored procedure is

executed on the Distributor where the custom business logic was registered.

Transact-SQL syntax conventions

Specifies the name of the custom business logic being unregistered.

@article_resolver

, with no default. If the business logic being removed is a COM component, this

parameter is the friendly name of the component. If the business logic is a .NET Framework

assembly, this parameter is the name of the assembly.

(success) or

is used in merge replication.

sp_enumcustomresolvers

at any server in the replication topology to return the list of

registered custom business logic modules or COM resolvers available to the topology.
