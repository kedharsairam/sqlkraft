---
name: "Backward Compatibility for Down-level Clients"
title: "Backward Compatibility for Down-level Clients"
category: "statements"
description: "Milliseconds can be preceded by either a colon (:) or a period (.)."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SQL Server

## Description

Milliseconds can be preceded by either a colon (:) or a period (.). If a colon is used, the

number means thousandths-of-a-second. If a period is used, a single digit means

tenths-of-a-second, two digits mean hundredths-of-a-second, and three digits mean

thousandths-of-a-second. For example, 12:30:20:1 indicates 20 and one-thousandth

seconds past 12:30; 12:30:20.1 indicates 20 and one-tenth seconds past 12:30.

Notes

hh:mm:ss

hh:mm[:ss].fractional

seconds]

hh is two digits, ranging from 0 to 23, that represent the number of hours in

the time zone offset.

mm is two digits, ranging from 0 to 59, that represent the number of

additional minutes in the time zone offset.

Notes

{t 'hh:mm:ss[.fractional seconds]'}

ODBC API specific.

Using hour 24 to represent midnight and leap second over 59 as defined by ISO 8601 (5.3.2

and 5.3) are not supported to be backward compatible and consistent with the existing date

and time types.

The default string literal format (used for down-level client) will align with the SQL standard

form, which is defined as hh:mm:ss[.nnnnnnn]. This format resembles the ISO 8601 definition

for TIME excluding fractional seconds.

Some down-level clients do not support the

,

,

and

data

types. The following table shows the type mapping between an up-level instance of SQL Server

and down-level clients.

Expand table

Expand table

Expand table

#### data type

#### Default string

#### literal format

#### passed to down-

#### level client

#### Down-level

#### ODBC

#### Down-level

#### OLEDB

#### Down-level

#### JDBC

#### Down-

#### level

### time(n)
