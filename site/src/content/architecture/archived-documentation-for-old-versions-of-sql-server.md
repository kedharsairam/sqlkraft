---
title: "Archived documentation for old versions of SQL Server"
topic: "io-fundamentals"
description: "SQL Server 2016 (13.x) and later versions"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

09/09/2025

Applies to:

SQL Server 2016 (13.x) and later versions

This article describes breaking changes in the SQL Server 2016 (13.x) Database Engine and

earlier versions of SQL Server. These changes might break applications, scripts, or

functionalities that are based on earlier versions of SQL Server. You might encounter these

issues when you upgrade.

The

column of

has expanded from an

to a

data type.

The

column of

has expanded from an

to a

data type.

Under database compatibility level 130, implicit conversions from

to

data types show improved accuracy by accounting for the fractional milliseconds,

resulting in different converted values. Use explicit casting to

data type

whenever a mixed comparison scenario between

and

datatypes

exists. For more information, see this

SQL Server and Azure SQL Database improvements

in handling some data types and uncommon operations

.

Under database compatibility level 130, operations that perform implicit conversions

between certain numeric and

data types show improved accuracy and can result

in different converted values. This includes usage of functions that require calculations

such as

and

. For more information, see this

SQL Server and Azure SQL

Database improvements in handling some data types and uncommon operations

.

For information about breaking changes in SQL Server 2014 (12.x), and in some earlier versions,

see

Breaking Changes to Database Engine Features in SQL Server 2014

.

We accumulate and retain documentation for very old versions of Microsoft SQL Server, in sets

of archived webpages. The archived webpages aren't processed by search engines, such as

bing.com

and

google.com

. Yet you can see these archives at our Docs

previous-versions/sql/

address:

SQL Server previous versions documentation

These archives include the documentation for at least the following older versions:

SQL Server 2014 (12.x)

SQL Server 2012 (11.x)

SQL Server 2008 R2 (10.50.x)

SQL Server 2008 (10.0.x)

SQL Server 2005 (9.x)

SQL Server 2014 documentation

is still available on our main Docs address.

SQL Server 2022 documentation

is available on our main Docs address. Then, you can use the

versioning dropdown list near the top of the page, to select another version of interest.

For more information about the documentation for previous versions of SQL Server, see

Previous versions of SQL Server documentation

.

Deprecated Database Engine features in SQL Server 2016 (13.x)

Discontinued Database Engine functionality in SQL Server

ALTER DATABASE (Transact-SQL) compatibility level

SQL Server and Azure SQL Database improvements in handling some data types and

uncommon operations

Related content

```sql
sample_ms
```

```sql
sys.dm_io_virtual_file_stats
```

```sql
timestamp
```

```sql
sys.fn_virtualfilestats
```

```sql
DATEDIFF
```

```sql
ROUND
```
