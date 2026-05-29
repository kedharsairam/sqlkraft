---
name: 'sys.dm_exec_describe_first_result_set_for_object'
title: 'sys.dm_exec_describe_first_result_set_for_object'
category: 'execution'
description: 'The following example evaluates a batch that contains two Transact-SQL statements. The result'
pubDate: 2026-05-29
---

SQL

The following example evaluates a batch that contains two Transact-SQL statements. The result

set describes the first result set returned.

SQL

sp_describe_first_result_set

sp_describe_undeclared_parameters

sys.dm_exec_describe_first_result_set_for_object

Last updated on 12/12/2025

## sys.dm_exec_describe_first_result_set_for_object

## int

## bit

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This dynamic management function takes an @object_id as a parameter and describes the first

result metadata for the module with that ID. The @object_id specified can be the ID of a

Transact-SQL stored procedure or a Transact-SQL trigger. If it is the ID of any other object (such

as a view, table, function, or CLR procedure), an error will be specified in the error columns of

the result.

has the same result set definition as

sys.dm_exec_describe_first_result_set (Transact-SQL)

and is similar to

sp_describe_first_result_set (Transact-SQL)

.

Transact-SQL syntax conventions

@object_id

The @object_id of a Transact-SQL stored procedure or a Transact-SQL trigger. @object_id is

type

.

@include_browse_information

@include_browse_information is type

. If set to 1, each query is analyzed as if it has a FOR

BROWSE option on the query. Returns additional key columns and source table information.

This common metadata is returned as a result set with one row for each column in the results

metadata. Each row describes the type and nullability of the column in the format described in

the following section. If the first statement does not exist for every control path, a result set

with zero rows is returned.

Specifies whether the column is an extra column

added for browsing information purposes that does

not actually appear in the result set.

Contains the ordinal position of the column in the

result set. Position of the first column will be specified

as 1.

Contains the name of the column if a name can be

determined. Otherwise is NULL.

Contains the value 1 if the column allows NULLs, 0 if

the column does not allow NULLs, and 1 if it cannot

be determined that the column allows NULLs.

Contains the system_type_id of the data type of the

column as specified in sys.types. For CLR types, even

though the system_type_name column will return

NULL, this column will return the value 240.

Contains the data type name. Includes arguments

(such as length, precision, scale) specified for the data

type of the column. If the data type is a user-defined

alias type, the underlying system type is specified

here. If it is a CLR user-defined type, NULL is returned

in this column.

Maximum length (in bytes) of the column.

-1 = Column data type is

,

,

, or

.

For

columns, the

value will be 16 or

the value set by

.

Precision of the column if numeric-based. Otherwise


## returns 0.
Scale of column if numeric-based. Otherwise returns

0.

Name of the collation of the column if character-

based. Otherwise returns NULL.

ﾉ

For CLR and alias types, contains the user_type_id of

the data type of the column as specified in sys.types.

Otherwise is NULL.

For CLR and alias types, contains the name of the

database in which the type is defined. Otherwise is

NULL.

For CLR and alias types, contains the name of the

schema in which the type is defined. Otherwise is

NULL.

For CLR and alias types, contains the name of the

type. Otherwise is NULL.

For CLR types, returns the name of the assembly and

class defining the type. Otherwise is NULL.

Contains the xml_collection_id of the data type of the

column as specified in sys.columns. This column will

return NULL if the type returned is not associated

with an XML schema collection.

Contains the database in which the XML schema

collection associated with this type is defined. This

column will return NULL if the type returned is not

associated with an XML schema collection.

Contains the schema in which the XML schema

collection associated with this type is defined. This

column will return NULL if the type returned is not

associated with an XML schema collection.

Contains the name of the XML schema collection

associated with this type. This column will return

NULL if the type returned is not associated with an

XML schema collection.


## Returns 1 if the returned data type is XML and that
type is guaranteed to be a complete XML document

(including a root node), as opposed to an XML

fragment). Otherwise returns 0.


## Returns 1 if the column is of a case-sensitive string
type and 0 if it is not.


## Returns 1 if the column is of a fixed-length CLR type
and 0 if it is not.

Name of the originating server returned by the

column in this result (if it originates from a remote

server). The name is given as it appears in sys.servers.


## Returns NULL if the column originates on the local
server, or if it cannot be determined which server it

originates on. Is only populated if browsing

information is requested.

Name of the originating database returned by the

column in this result. Returns NULL if the database

cannot be determined. Is only populated if browsing

information is requested.

Name of the originating schema returned by the

column in this result. Returns NULL if the schema

cannot be determined. Is only populated if browsing

information is requested.

Name of the originating table returned by the

column in this result. Returns NULL if the table

cannot be determined. Is only populated if browsing

information is requested.

Name of the originating column returned by the

column in this result. Returns NULL if the column

cannot be determined. Is only populated if browsing

information is requested.


## Returns 1 if the column is an identity column and 0 if
not. Returns NULL if it cannot be determined that the

column is an identity column.


## Returns 1 if the column is part of a unique index
(including unique and primary constraint) and 0 if

not. Returns NULL if it cannot be determined that the

column is part of a unique index. Only populated if

browsing information is requested.


## Returns 1 if the column is updateable and 0 if not.

## Returns NULL if it cannot be determined that the
column is updateable.


## Returns 1 if the column is a computed column and 0
if not. Returns NULL if it cannot be determined that

the column is a computed column.


## Returns 1 if the column is a sparse column and 0 if
not. Returns NULL if it cannot be determined that the

column is a part of a sparse column set.

## sp_describe_first_result_set

Position of this column in ORDER BY list Returns

NULL if the column does not appear in the ORDER BY

list or if the ORDER BY list cannot be uniquely

determined.

Length of the ORDER BY list. Returns NULL if there is

no ORDER BY list or if the ORDER BY list cannot be

uniquely determined. Note that this value will be the

same for all rows returned by

sp_describe_first_result_set.

If the ordinal_in_order_by_list is not NULL, the

column reports the direction

of the ORDER BY clause for this column. Otherwise it

reports NULL.

Contains the error number returned by the function.

Contains NULL if no error occurred in the column.

Contains the severity returned by the function.

Contains NULL if no error occurred in the column.

Contains the state message returned by the function.

If no error occurred. the column will contain NULL.

Contains the message returned by the function. If no

error occurred, the column will contain NULL.

Contains an integer representing the error being

returned. Maps to error_type_desc. See the list under


## remarks.
Contains a short uppercase string representing the

error being returned. Maps to error_type. See the list

under remarks.

This function uses the same algorithm as

. For more information,

see

sp_describe_first_result_set (Transact-SQL)

.

The following table lists the error types and their descriptions

ﾉ

1

MISC

All errors that are not otherwise described.

2


## SYNTAX
A syntax error occurred in the batch.

3

CONFLICTING_RESULTS

The result could not be determined because of a conflict

between two possible first statements.

4

DYNAMIC_SQL

The result could not be determined because of dynamic SQL

that could potentially return the first result.

5

CLR_PROCEDURE

The result could not be determined because a CLR stored

procedure could potentially return the first result.

6

CLR_TRIGGER

The result could not be determined because a CLR trigger

could potentially return the first result.

7

EXTENDED_PROCEDURE

The result could not be determined because an extended

stored procedure could potentially return the first result.

8

UNDECLARED_PARAMETER

The result could not be determined because the data type

of one or more of the result set's columns potentially

depends on an undeclared parameter.

9

RECURSION

The result could not be determined because the batch

contains a recursive statement.

10

TEMPORARY_TABLE

The result could not be determined because the batch

contains a temporary table and is not supported by

.

11

UNSUPPORTED_STATEMENT

The result could not be determined because the batch

contains a statement that is not supported by

(e.g., FETCH, REVERT etc.).

12

OBJECT_ID_NOT_SUPPORTED

The @object_id passed to the function is not supported (i.e.

not a stored procedure)

13

OBJECT_ID_DOES_NOT_EXIST

The @object_id passed to the function was not found in the

system catalog.

Requires permission to execute the @tsql argument.

## sys.dm_exec_describe_first_result_set

## sys.dm_exec_describe_first_result_set_for_object

```sql
USE
@AdventureWorks2025;
GO
CREATE
PROC Production.TestProc
AS
SELECT
Name
, ProductID, Color
FROM
Production.Product;
SELECT
Name
, SafetyStockLevel, SellStartDate
FROM
Production.Product;
GO
SELECT
*
FROM
sys.dm_exec_describe_first_result_set(
'Production.TestProc'
,
NULL
, 0);
```

```sql
USE
AdventureWorks2025;
GO
SELECT
*
FROM
sys.dm_exec_describe_first_result_set(
N
'SELECT CustomerID, TerritoryID, AccountNumber FROM Sales.Customer WHERE
CustomerID = @CustomerID;SELECT * FROM Sales.SalesOrderHeader;'
,
N
'@CustomerID int'
,
0
)
AS
a;
```

```sql
sys.dm_exec_describe_first_result_set_for_object
( @object_id , @include_browse_information )
```
