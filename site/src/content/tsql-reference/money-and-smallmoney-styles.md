---
name: "money and smallmoney styles"
title: "Money and smallmoney styles"
category: "data-types"
description: ""
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

When converting character data to

, using a style that includes a time, a time

zone offset is appended to the result.

For a

or

expression

,

style

can have one of the values shown in the following table.

Other values are processed as 0.

(default)

A maximum of 6 digits. Use in scientific notation, when appropriate.

Always 8 digits. Always use in scientific notation.

Always 16 digits. Always use in scientific notation.

Always 17 digits. Use for lossless conversion. With this style, every distinct float or real value

is guaranteed to convert to a distinct character string.

Applies to:

SQL Server 2016 (13.x) and later versions, and Azure SQL Database.

Included for legacy reasons. Don't use these values for new development.

For a

or

expression

,

style

can have one of the values shown in the

following table. Other values are processed as 0.

(default)

No commas every three digits to the left of the decimal point, and two digits to the right of

the decimal point

Example: 4235.98.

Commas every three digits to the left of the decimal point, and two digits to the right of the

decimal point

Example: 3,510.92.

Expand table

Expand table
