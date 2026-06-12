---
name: "sys.dm_tran_session_transactions"
title: "sys.dm_tran_session_transactions"
category: "io"
description: "The identifier for the node that this distribution is on. On SQL Server and SQL Managed Instance, requires In Microsoft Fabric, membership in the or more privileged role is needed to query On SQL Database service objectives, and for databases in Microsoft Entra admin account, or membership in the is required. On all other SQL Database service objectives, permission on the database, or membership i"
tags: ["io","dmv"]
pubDate: "2026-05-29"
syntax: "sys.dm_tran_session_transactions"
---

## Description

The identifier for the node that this distribution is on. On SQL Server and SQL Managed Instance, requires In Microsoft Fabric, membership in the or more privileged role is needed to query On SQL Database service objectives, and for databases in Microsoft Entra admin account, or membership in the is required. On all other SQL Database service objectives, permission on the database, or membership in the server role is required. Requires VIEW SERVER PERFORMANCE STATE permission on the server. Through bound sessions and distributed transactions, it's possible for a transaction to be running under more than one session. In such cases, multiple rows for the same , one for each session under which the transaction is running. Because of differences in how they are recorded, By executing multiple requests in autocommit mode using multiple active result sets (MARS),

## Syntax

`sys.dm_tran_session_transactions`

## Remarks

The identifier for the node that this distribution is on.

On SQL Server and SQL Managed Instance, requires

permission.

In Microsoft Fabric, membership in the

workspace role

or more privileged role is

needed to query

On SQL Database

service objectives, and for databases in

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

permission on the database, or membership in the

server role is required.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

Through bound sessions and distributed transactions, it's possible for a transaction to be

running under more than one session. In such cases,

multiple rows for the same

, one for each session under which the transaction is

running. Because of differences in how they are recorded,

By executing multiple requests in autocommit mode using multiple active result sets (MARS),

it's possible to have more than one active transaction on a single session. In such cases,

shows multiple rows for the same

, one for each

transaction running under that session.

To call from Azure Synapse Analytics or Analytics Platform System (PDW), use the name. This syntax is not supported by serverless SQL

pool in Azure Synapse Analytics.
