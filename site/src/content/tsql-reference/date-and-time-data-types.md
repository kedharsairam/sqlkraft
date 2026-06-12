---
name: "Date and time data types"
title: "Date and time data types"
category: "data-types"
description: "Lists and describes the date and time data types available in T-SQL, including their ranges, accuracy, and storage sizes."
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

rowversion

timestamp

rowversion

ﾃ

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse

Analytics

SQL database in Microsoft Fabric

The sections in this article cover all Transact-SQL date and time data types and functions, including usage and

## examples.

The following table lists the Transact-SQL date and time data types.

Data type

Format

Range

Accuracy

Storage

size

(bytes)

User-defined

fractional second precision

Time

zone offset

time

HH:mm:ss[.nnnnnnn]

00:00:00.0000000 through

23:59:59.9999999

100 nanoseconds

3 to 5

Yes

No

date

yyyy-MM-dd

0001-01-01 through

9999-12-31

1 day

3

No

No

smalldatetime

yyyy-MM-dd HH:mm:ss

1900-01-01 through

2079-06-06

1 minute

4

No

No

datetime

yyyy-MM-dd

HH:mm:ss[.nnn]

1753-01-01 through

9999-12-31

0.00333 second

8

No

No

datetime2

yyyy-MM-dd

HH:mm:ss[.nnnnnnn]

0001-01-01

00:00:00.0000000 through 9999-12-31

23:59:59.9999999

100 nanoseconds

6 to 8

Yes

No

datetimeoffset

yyyy-MM-dd

HH:mm:ss[.nnnnnnn]

[+|-]HH:mm

0001-01-01

00:00:00.0000000 through 9999-12-31

23:59:59.9999999 (in

UTC)

100 nanoseconds

8 to 10

Yes

Yes

７

Note

The Transact-SQL data type isn't a date or time data type.

is a deprecated synonym for.
