---
title: "Sequence Properties"
topic: "service-broker"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Creates a sequence object and specifies its properties. A sequence is a user-defined schema

tags:
  - "service-broker"
  - "sequence-properties"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Creates a sequence object and specifies its properties. A sequence is a user-defined schema

bound object that generates a sequence of numeric values according to the specification with

which the sequence was created. The sequence of numeric values is generated in an ascending

or descending order at a defined interval and can be configured to restart (cycle) when

exhausted. Sequences, unlike identity columns, are not associated with specific tables.

Applications refer to a sequence object to retrieve its next value. The relationship between

sequences and tables is controlled by the application. User applications can reference a

sequence object and coordinate the values across multiple rows and tables.

Unlike identity columns values which are generated at the time of insert, an application can

obtain the next sequence number without inserting the row by calling the

NEXT VALUE FOR

function. Use

sp_sequence_get_range

to get multiple sequence numbers at once.

For information and scenarios that use both

and the

function, see

Sequence Numbers.

This page is accessed in two ways: either by right-clicking

in Object Explorer and

clicking

, or by right-clicking an existing sequence and clicking.

When you right-click an existing sequence and click

, the options are not editable. To

change the sequence options use the

ALTER SEQUENCE (Transact-SQL)

statement or drop and

recreate the sequence object.

Enter the sequence name here.

Specify the schema that will own this sequence.

A sequence can be defined as any integer type. This includes:

0 to 255

ﾉ

Expand table
