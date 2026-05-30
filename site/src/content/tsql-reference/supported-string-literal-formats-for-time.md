---
name: "Supported String Literal Formats for time"
title: "Supported String Literal Formats for time"
category: "data-types"
description: "* Not supported in Informatica."
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

(11,2)

3

0-2

(12,3)

4

3-4

-

(13,4)

4

3-4

-

(14,5)

5

5-7

-

(15,6)

5

5-7

- -

(16,7)

5

5-7

- Not supported in Informatica.

* Not supported in Microsoft Fabric.

The following table shows the valid string literal formats for the data type.

SQL Server

## Description

hh:mm[:ss]

[:fractional seconds][AM]

[PM]

hh:mm[:ss]

[.fractional seconds][AM]

[PM]

hhAM[PM] hh AM[PM]

The hour value of 0 represents the hour after midnight (AM), regardless of whether AM is specified. PM cannot be specified when the hour equals 0.

Hour values from 01 through 11 represent the hours before noon if neither AM nor PM is specified. The values represent the hours before noon when AM is specified. The values represent hours after noon if PM is specified.

The hour value 12 represents the hour that starts at noon if neither AM nor PM is specified. If AM is specified, the value represents the hour that starts at midnight. If PM is specified, the value represents the hour that starts at noon. For example, 12:01 is 1 minute after noon, as is 12:01 PM; and 12:01 AM is one minute after midnight.

Specifying 12:01 AM is the same as specifying 00:01 or 00:01 AM.

Hour values from 13 through 23 represent hours after noon if AM or PM is not specified. The values also represent the hours after noon when PM is specified. AM cannot be specified when the hour value is from 13 through 23.

An hour value of 24 is not valid. To represent midnight, use 12:00 AM or 00:00.

ISO 8601

ODBC

time

date

datetime2

datetimeoffset
