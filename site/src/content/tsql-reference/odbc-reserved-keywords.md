---
name: "ODBC Reserved Keywords"
title: "ODBC Reserved Keywords"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

EXEC

PRECISION

WITH

EXECUTE

PRIMARY

WITHIN GROUP

EXISTS

PRINT

WRITETEXT

EXIT

PROC

The following table lists reserved keywords that are exclusive to.

Additionally, the ISO standard defines a list of reserved keywords. Avoid using ISO reserved keywords for object names and identifiers. The ODBC reserved keyword list, shown in the following table, is the same as the ISO reserved keyword list.

Transact-SQL reserved keywords can be used as identifiers or names of databases or database objects, such as tables, columns, views, and so on. Use either quoted identifiers or delimited identifiers. Using reserved keywords as the names of variables and stored procedure parameters is not restricted.

７

Note

The ISO standards reserved keywords list sometimes can be more restrictive than SQL

Server and at other times less restrictive. For example, the ISO reserved keywords list contains. SQL Server does not have to distinguish this as a reserved keyword.

ABSOLUTE

EXEC

OVERLAPS

ACTION

EXECUTE

PAD

ADA

EXISTS

PARTIAL

ADD

EXTERNAL

PASCAL

ALL

EXTRACT

POSITION

ALLOCATE

FALSE

PRECISION

ALTER

FETCH

The following words are reserved for use in ODBC function calls. These words do not constrain the minimum SQL grammar; however, to ensure compatibility with drivers that support the core SQL grammar, applications should avoid using these keywords.

This is the current list of ODBC reserved keywords.

PREPARE

AND

FIRST

PRESERVE

ANY

FLOAT

PRIMARY

ARE

FOR

PRIOR

AS

FOREIGN

PRIVILEGES

ASC

FORTRAN

PROCEDURE

ASSERTION

FOUND

PUBLIC

AT

FROM

READ

AUTHORIZATION

FULL

REAL

AVG

GET

REFERENCES

BEGIN

GLOBAL

RELATIVE

BETWEEN

GO

RESTRICT

BIT

GOTO

REVOKE

BIT_LENGTH

GRANT

RIGHT

BOTH

GROUP

ROLLBACK

BY

HAVING

ROWS

CASCADE

HOUR

SCHEMA

CASCADED

IDENTITY

SCROLL

CASE

IMMEDIATE

SECOND

CAST

IN

SECTION

CATALOG

INCLUDE

SELECT

CHAR

INDEX

SESSION

CHAR_LENGTH

INDICATOR

SESSION_USER

CHARACTER

INITIALLY

SET

CHARACTER_LENGTH

INNER

SIZE

CHECK

INPUT

SMALLINT

CLOSE

INSENSITIVE

SOME

COALESCE

INSERT

SPACE

COLLATE

INT

COLLATION

INTEGER

COLUMN

INTERSECT

SQLCA

COMMIT

INTERVAL

CONNECT

INTO

CONNECTION

IS

CONSTRAINT

ISOLATION

SUBSTRING

CONSTRAINTS

JOIN

SUM

CONTINUE

KEY

SYSTEM_USER

CONVERT

LANGUAGE

TABLE

SQLCODE

SQLERROR

SQLSTATE

SQLWARNING

CORRESPONDING

LAST

TEMPORARY

COUNT

LEADING

THEN

CREATE

LEFT

TIME

CROSS

LEVEL

TIMESTAMP

CURRENT

LIKE

TIMEZONE_HOUR

CURRENT_DATE

LOCAL

TIMEZONE_MINUTE

CURRENT_TIME

LOWER

TO

CURRENT_TIMESTAMP

MATCH

TRAILING

CURRENT_USER

MAX

TRANSACTION

CURSOR

MIN

TRANSLATE

DATE

MINUTE

TRANSLATION

DAY

MODULE

TRIM

DEALLOCATE

MONTH

TRUE

DEC

NAMES

UNION

DECIMAL

NATIONAL

UNIQUE

DECLARE

NATURAL

UNKNOWN

DEFAULT

NCHAR

UPDATE

DEFERRABLE

NEXT

UPPER

DEFERRED

NO

USAGE

DELETE

NONE

USER

DESC

NOT

USING

DESCRIBE

NULL

VALUE

DESCRIPTOR

NULLIF

VALUES

DIAGNOSTICS

NUMERIC

VARCHAR

DISCONNECT

OCTET_LENGTH

VARYING

DISTINCT

OF

VIEW

DOMAIN

ON

WHEN

DOUBLE

ONLY

WHENEVER

DROP

OPEN

WHERE

ELSE

OPTION

WITH

END

OR

WORK

END-EXEC

ORDER

WRITE

ESCAPE

OUTER

YEAR

EXCEPT

OUTPUT

ZONE

EXCEPTION
