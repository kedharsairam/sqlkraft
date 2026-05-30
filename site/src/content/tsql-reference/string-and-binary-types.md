---
name: "String and binary types"
title: "String and binary types"
category: "data-types"
description: "Azure SQL Managed Instance"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

#### Type

#### binary

#### varbinary

#### binary

#### char

#### varchar

#### nchar

#### nvarchar

#### ntext

#### text

#### image

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

SQL Server supports the following string and binary types.

## Description

binary and

varbinary

Binary data types of either fixed length or variable length. Converting data to the

and

data types is useful if

data is the easiest way to move around data.

char and

varchar

Character data types that are either fixed-size,

, or variable-size,

.

Starting with SQL Server 2019 (15.x), when a UTF-8 enabled collation is used, these data

types store the full range of Unicode character data and use the UTF-8 character

encoding.

nchar and

nvarchar

Unicode character data types that are either fixed-size,

, or variable-size,

.

Starting with SQL Server 2012 (11.x), when a Supplementary Character (SC) enabled

collation is used, these data types store the full range of Unicode character data and use

the UTF-16 character encoding.

ntext, text,

and image

Fixed and variable-length data types for storing large non-Unicode and Unicode

character and binary data. Unicode data uses the Unicode UCS-2 character set.

The

,

, and

data types will be removed in a future version of SQL Server.

Avoid using these data types in new development work, and plan to modify applications

that currently use them.

Data types (Transact-SQL)

Numeric types

String Functions

Last updated on 11/18/2025



Expand table

See also
