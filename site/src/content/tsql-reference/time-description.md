---
name: 'time Description'
title: 'time Description'
category: 'data-types'
description: 'Azure SQL Managed Instance'
tags: ["tsql", "data-types"]
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

Defines a time of a day. The time is without time zone awareness and is based on a 24-hour

clock.


## Syntax
[ (

fractional second scale

) ]

Usage

DECLARE @MyTime

CREATE TABLE Table1 ( Column1

)

fractional seconds scale

Specifies the number of digits for the fractional part of the seconds.

This can be an integer from 0 to 7. For Informatica, this can be an integer from 0

to 3.

The default fractional scale is 7 (100ns).

In Microsoft Fabric, this can be an integer from 0 to 6, with no default. Precision

must be specified in Microsoft Fabric.

Default string literal

format

(used for down-level

client)

hh:mm:ss[.nnnnnnn] for Informatica)

For more information, see the

Backward Compatibility for Down-level Clients

section.

Range

00:00:00.0000000 through 23:59:59.9999999 (00:00:00.000 through 23:59:59.999

for Informatica)

Element ranges

hh is two digits, ranging from 0 to 23, that represent the hour.

７

Note

Informatica information is provided for PDW customers using the Informatica Connector.

ﾉ

Expand table

#### Property

#### Value

#### date

#### datetime2

#### datetimeoffset

#### Specified scale

#### Result (precision, scale)

#### Column length (bytes)

#### Fractional

#### seconds

#### precision

#### time

#### time(0)

#### time(1)

mm is two digits, ranging from 0 to 59, that represent the minute.

ss is two digits, ranging from 0 to 59, that represent the second.

n* is zero to seven digits, ranging from 0 to 9999999, that represent the

fractional seconds. For Informatica, n* is zero to three digits, ranging from 0 to

999.

Character length

8 positions minimum (hh:mm:ss) to 16 maximum (hh:mm:ss.nnnnnnn). For

Informatica, the maximum is 12 (hh:mm:ss.nnn).

Precision, scale

(user specifies scale

only)

See the table below.

Storage size

5 bytes, fixed, is the default with the default of 100ns fractional second

precision. In Informatica, the default is 4 bytes, fixed, with the default of 1ms

fractional second precision.

Accuracy

100 nanoseconds (1 millisecond in Informatica)

Default value

00:00:00

This value is used for the appended time part for implicit conversion from

to

or

.

User-defined fractional

second precision

Yes

Time zone offset aware

and preservation

No

Daylight saving aware

No

(16,7) [(12,3) in Informatica]

5 (4 in Informatica)

7 (3 in Informatica)

(8,0)

3

0-2

(10,1)

3

0-2

ﾉ

Expand table

#### Specified scale

#### Result (precision, scale)

#### Column length (bytes)

#### Fractional

#### seconds

#### precision

#### time(2)

#### time(3)

#### time(4)

#### time(5)

#### time(6)

#### time(7)

### time
