---
name: "Backward Compatibility for Down-level Clients"
title: "Backward Compatibility for Down-level Clients"
category: "statements"
description: "Milliseconds can be preceded by either a colon (:) or a period (.)."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## Description

Milliseconds can be preceded by either a colon (:) or a period (.).

number means thousandths-of-a-second.

thousandths-of-a-second. For example, 12:30:20:1 indicates 20 and one-thousandth

seconds past 12:30; 12:30:20.1 indicates 20 and one-tenth seconds past 12:30.

Notes

hh:mm:ss

hh:mm[:ss].fractional

seconds]

the time zone offset.

additional minutes in the time zone offset.

Notes

{t 'hh:mm:ss[.fractional seconds]'}

ODBC API specific.

Using hour 24 to represent midnight and leap second over 59 as defined by ISO 8601 (5.3.2

and time types.

The default string literal format (used for down-level client) will align with the SQL standard

form, which is defined as hh:mm:ss[.nnnnnnn]. This format resembles the ISO 8601 definition

for TIME excluding fractional seconds.

,

,

and

data

types. The following table shows the type mapping between an up-level instance of SQL Server

and down-level clients.

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

### time(n)
