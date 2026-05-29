---
name: 'sys.system_objects'
title: 'sys.system_objects'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

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

Contains one row for all schema-scoped system objects that are included with Microsoft SQL

Server. All system objects are contained in the schemas named sys or INFORMATION_SCHEMA.


## Description
name

Object name.

object_id

Object identification number. Is unique within a database.

principal_id

ID of the individual owner if different from the schema owner. By

default, schema-contained objects are owned by the schema

owner. However, another owner can be specified by using the

ALTER AUTHORIZATION statement to change ownership.

Is NULL if there is no other individual owner.

Is NULL if the object type is one of the following:

C = CHECK constraint

D = DEFAULT (constraint or stand-alone)

F = FOREIGN KEY constraint

PK = PRIMARY KEY constraint

R = Rule (old-style, stand-alone)

TA = Assembly (CLR) trigger

TR = SQL trigger

UQ = UNIQUE constraint

schema_id

ID of the schema that the object is contained in.

For all schema-scoped system objects that included with SQL

Server, this value will always be in (schema_id('sys'),

schema_id('INFORMATION_SCHEMA'))

ﾉ

Expand table


## Description
parent_object_id

ID of the object to which this object belongs.

0 = Not a child object.

type

Object type:

AF = Aggregate function (CLR)

C = CHECK constraint

D = DEFAULT (constraint or stand-alone)

F = FOREIGN KEY constraint

FN = SQL scalar function

FS = Assembly (CLR) scalar-function

FT = Assembly (CLR) table-valued function

IF = SQL inline table-valued function

IT = Internal table

P = SQL Stored Procedure

PC = Assembly (CLR) stored-procedure

PG = Plan guide

PK = PRIMARY KEY constraint

R = Rule (old-style, stand-alone)

RF = Replication-filter-procedure

S = System base table

SN = Synonym

SQ = Service queue

TA = Assembly (CLR) DML trigger

TF = SQL table-valued-function

TR = SQL DML trigger


## Description
TT = Table type

U = Table (user-defined)

UQ = UNIQUE constraint

V = View

X = Extended stored procedure

type_desc


## Description of the object type. AGGREGATE_FUNCTION
CHECK_CONSTRAINT

DEFAULT_CONSTRAINT

FOREIGN_KEY_CONSTRAINT

SQL_SCALAR_FUNCTION

CLR_SCALAR_FUNCTION

CLR_TABLE_VALUED_FUNCTION

SQL_INLINE_TABLE_VALUED_FUNCTION

INTERNAL_TABLE

SQL_STORED_PROCEDURE

CLR_STORED_PROCEDURE

PLAN_GUIDE

PRIMARY_KEY_CONSTRAINT

RULE

REPLICATION_FILTER_PROCEDURE

SYSTEM_TABLE

SYNONYM

SERVICE_QUEUE

CLR_TRIGGER
