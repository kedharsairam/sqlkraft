---
name: "Date and time styles"
title: "Date and time styles"
category: "data-types"
description: ""
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

An integer expression that specifies how the function will translate expression. For a style value of NULL, NULL is returned.

data_type determines the range.

## Returns

expression

, translated to data_type.

For a date or time data type expression

, style can have one of the values shown in the following table. Other values are processed as 0. Beginning with SQL Server 2012 (11.x), the only styles supported, when converting from date and time types to

, are 0 or 1. All other conversion styles return error 9809.

- or

Default for and

(or

)

U.S.

1 =

101 =

ANSI

2 =

102 =

British/French

3 =

103 =

German

4 =

104 =

Italian

5 =

105 =

-

6 =

106 =

７

Note

supports the date format, in Arabic style, with the Kuwaiti algorithm.

1

3

1,

2

1

Without

century (yy)

With century

(yyyy)

Standard

Input/output

7

107

8

24

108

9

109

10

110

11

111

12

112

13

113

14

114

20

120

21

25

121

time

date

datetime2

datetimeoffset

22

23

126

127

130

131

-

7 =

107 = or

-

- or

Default + milliseconds

(or

)

USA

10 = mm-dd-yy

110 =

JAPAN

11 = yy/mm/dd

111 =

ISO

12 = yymmdd

112 =

- or

Europe default + milliseconds

(24-hour)

-

(24-hour)

- or

ODBC canonical

(24- hour)

- or

or

ODBC canonical (with milliseconds) default for

,

,

, and

(24-hour)

-

U.S.

(or

)

-

ISO8601

-

ISO8601

(no spaces)

-

ISO8601 with time zone Z

(no spaces)

-

Hijri

-

Hijri

1

3

1

1,

2

1,

2

2

2

4

6

8, 9

6

1,

2

5

7

2

5

0

100

9

109

13

113

20

120

23

21

25

121

datetime

datetime

smalldatetime

datetime

smalldatetime

datetime

smalldatetime

datetime

datetime

smalldatetime

datetime

smalldatetime

char

varchar

These style values return nondeterministic results. Includes all (

) (without century) styles and a subset of (

) (with century) styles.

The default values (or

, or

, or

, or

,

, and or or

) always return the century (

).

Input when you convert to

; output when you convert to character data.

Designed for XML use. For conversion from or to character data, see the previous table for the output format.

Hijri is a calendar system with several variations. SQL Server uses the Kuwaiti algorithm.

For a milliseconds (

) value of 0, the millisecond decimal fraction value won't display. For example, the value displays as.

In this style, represents a multi-token Hijri Unicode representation of the full month name. This value doesn't render correctly on a default US installation of SSMS.

Only supported when casting from character data to or. When casting character data representing only date or only time components to the or data types, the unspecified time component is set to
, and the unspecified date component is set to.

Use the optional time zone indicator to make it easier to map XML values that have time zone information to SQL Server values that have no time zone.

indicates time zone at UTC-0. The offset, in the or direction, indicates other time zones. For example:.

When converting to character data, the styles that include seconds or milliseconds show zeros in these positions. When converting from or values, use an appropriate or data type length to truncate unwanted date parts.

1

2

）

Important

By default, SQL Server interprets two-digit years based on a cutoff year of 2049. That means that SQL Server interprets the two-digit year 49 as 2049 and the two-digit year 50 as 1950. Many client applications, including those based on Automation objects, use a cutoff year of 2030. SQL Server provides the two digit year cutoff configuration option to change the cutoff year used by SQL Server. This allows for the consistent treatment of dates. We recommend specifying four-digit years.

3

4

5

6

7

8

9

datetimeoffset

float

real

Value

Output

0

1

2

3

126, 128,

129

money

smallmoney

Value

Output

0

1

`CONVERT`

```sql
mon dd yyyy hh:miAM
```

`PM`

```sql
mm/dd/yy
```

```sql
mm/dd/yyyy
```

`yy.mm.dd`

`yyyy.mm.dd`

```sql
dd/mm/yy
```

```sql
dd/mm/yyyy
```

`dd.mm.yy`

`dd.mm.yyyy`

```sql
dd-mm-yy
```

```sql
dd-mm-yyyy
```

```sql
dd mon yy
```

```sql
dd mon yyyy
```

```sql
Mon dd, yy
```

```sql
Mon dd, yyyy
```

```sql
hh:mi:ss
```

```sql
mon dd yyyy hh:mi:ss:mmmAM
```

`PM`

```sql
mm-dd-yyyy
```

```sql
yyyy/mm/dd
```

`yyyymmdd`

```sql
dd mon yyyy hh:mi:ss:mmm
```

```sql
hh:mi:ss:mmm
```

```sql
yyyy-mm-dd hh:mi:ss
```

```sql
yyyy-mm-dd hh:mi:ss.mmm
```

```sql
mm/dd/yy hh:mi:ss AM
```

`PM`

```sql
yyyy-mm-dd
```

```sql
yyyy-mm-ddThh:mi:ss.mmm
```

```sql
yyyy-MM-
ddThh:mm:ss.fffZ
```

```sql
dd mon yyyy hh:mi:ss:mmmAM
```

```sql
dd/mm/yyyy hh:mi:ss:mmmAM
```

`yy`

`yyyy`

`yyyy`

`mmm`

```sql
2022-11-07T18:26:20.000
```

```sql
2022-11-07T18:26:20
```

`mon`

```sql
00:00:00.000
```

```sql
1900-01-01
```

```sql
Z
```

```sql
Z
```

```sql
HH:MM
```

```sql
+
```

```sql
-
```

```sql
2022-12-12T23:45:12-08:00
```
