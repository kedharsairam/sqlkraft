---
name: "Differences between compatibility levels"
title: "Differences between compatibility levels"
category: "predicates"
description: "resulting in different converted values."
tags: ["tsql", "predicates"]
pubDate: 2026-05-29
---

resulting in different converted values. To restore previous conversion behavior, set the

database compatibility level to 120 or lower.

## Examples of breaking changes

by compatibility level are:

Changed column names in system objects. In SQL Server 2012 (11.x) the column

in

was renamed to. Regardless of the

compatibility level, the query

will

produce error 207 (Invalid column name).

Removed system objects. In SQL Server 2012 (11.x) the

was removed.

Regardless of the compatibility level, the statement

produces error 2812 (

).

For more information on breaking changes, see:

Breaking changes to Database Engine features in SQL Server 2019

Breaking changes to Database Engine features in SQL Server 2017

Breaking changes to Database Engine features in SQL Server 2016

For all installations of SQL Server, the default compatibility level is associated with the version

of the Database Engine, as seen in

this table. For new development work, always plan to certify

applications on the latest database compatibility level.

New Transact-SQL syntax isn't gated by database compatibility level, except when they can

break existing applications by creating a conflict with user Transact-SQL code. These exceptions

are documented in the next sections of this article that outline the differences between specific

compatibility levels.

Database compatibility level also provides backward compatibility with earlier versions of SQL

Server, because databases attached or restored from any earlier version of SQL Server retain

their existing compatibility level (if same or higher than the minimum allowed compatibility

level). This was discussed in the

Using compatibility level for backward compatibility

section of

this article.

Starting with database compatibility level 130, any new fixes and features affecting query plans

have been added only to the latest compatibility level available, also called the default

compatibility level. This has been done in order to minimize the risk during upgrades that arise

from performance degradation due to query plan changes, potentially introduced by new

query optimization behaviors.

### Query Optimizer fixes released for previous SQL Server versions under trace flag 4199

### become automatically enabled in the default compatibility level of a newer SQL Server

### version

#### Database Engine (DE)

#### version

#### Database

#### Compatibility

#### Level

#### TF

#### 4199

#### QO changes from all

#### previous Database

#### Compatibility Levels

#### QO changes

#### for (DE)

#### version post-

#### RTM

#### Disabled

#### Enabled

The fundamental plan-affecting changes added only to the default compatibility level of a new

version of the Database Engine are:

1.

(Starting with version SQL Server 2016 (13.x)), Azure SQL Database.

For example, when SQL Server 2016 (13.x) was released, all the Query Optimizer fixes

released for previous SQL Server versions (and respective compatibility levels 100 through

120. became automatically enabled for databases that use the SQL Server 2016 (13.x)

default compatibility level (130). Only post-RTM Query Optimizer fixes need to be

explicitly enabled.

To enable Query Optimizer fixes, you can use the following methods:

At the server level, with

trace flag 4199.

At the database level, with the

option in

ALTER DATABASE

SCOPED CONFIGURATION (Transact-SQL).

At the query level, with the

query hint

by modifying the query.

At the query level, with the

without

code changes, using the

Query Store hints

feature.

Later, when SQL Server 2017 (14.x) was released, all the Query Optimizer fixes released

after SQL Server 2016 (13.x) RTM became automatically enabled for databases using the

2017 (14.x) default compatibility level (140). This is a cumulative behavior that

includes all previous versions fixes as well. Again, only post-RTM Query Optimizer fixes

need to be explicitly enabled.

The following table summarizes this behavior:

13 (SQL Server 2016

(13.x))

100 to 120

130

Off

On

Off

On

Enabled

Enabled

Disabled

Enabled

Disabled

Enabled

Expand table

#### Database Engine (DE)

#### version

#### Database

#### Compatibility

#### Level

#### TF

#### 4199

#### QO changes from all

#### previous Database

#### Compatibility Levels

#### QO changes

#### for (DE)

#### version post-

#### RTM

#### Disabled

#### Enabled

#### Enabled

#### Disabled

#### Enabled

#### Enabled

#### Disabled

#### Enabled

#### Enabled

#### Disabled

#### Enabled

#### Enabled

### Changes to the

### cardinality estimator

### released on SQL Server, Azure SQL Database, and

### new Database Engine version

14 (SQL Server 2017

(14.x))

100 to 120

130

140

Off

On

Off

On

Off

On

Enabled

Enabled

Enabled

Disabled

Enabled

Disabled

Enabled

Disabled

Enabled

15 (SQL Server 2019

(15.x)) and (Azure SQL

Database)

100 to 120

130 to 140

150

Off

On

Off

On

Off

On

Enabled

Enabled

Enabled

Disabled

Enabled

Disabled

Enabled

Disabled

Enabled

16 (SQL Server 2022

(16.x)) and (Azure SQL

Database)

100 to 120

130 to 150

160

Off

On

Off

On

Off

On

Enabled

Enabled

Enabled

Disabled

Enabled

Disabled

Enabled

Disabled

Enabled

17 (SQL Server 2025

(17.x), Azure SQL

Database and SQL

database in Microsoft

Fabric)

100 to 120

130 to 160

170

Off

On

Off

On

Off

On

Enabled

Enabled

Enabled

Disabled

Enabled

Disabled

Enabled

Disabled

Enabled

Query Optimizer fixes that address wrong results or access violation errors aren't

protected by trace flag 4199. Those fixes aren't considered optional.

2.

are enabled only in the default compatibility level of a

, but not on previous compatibility levels.

For example, when SQL Server 2016 (13.x) was released, changes to the cardinality

estimation process were available only for databases using SQL Server 2016 (13.x) default

compatibility level (130). Previous compatibility levels retained the cardinality estimation

behavior that was available before SQL Server 2016 (13.x).

Later, when SQL Server 2017 (14.x) was released, newer changes to the cardinality

estimation process were available only for databases using SQL Server 2017 (14.x) default

#### Database Engine version

#### Database Compatibility Level

#### New version CE changes

#### Compatibility level setting of 160 or

#### lower

#### Compatibility level setting of 170

`single_pages_kb`

`sys.dm_os_sys_info`

`pages_kb`

```sql
SELECT single_pages_kb FROM sys.dm_os_sys_info
```

`sp_dboption`

```sql
EXEC sp_dboption
'AdventureWorks2022', 'autoshrink', 'FALSE';
```

```sql
Could not find stored procedure 'sp_dboption'
```

`QUERY_OPTIMIZER_HOTFIXES`

```sql
USE HINT 'ENABLE_QUERY_OPTIMIZER_HOTFIXES'
```

```sql
USE HINT 'ENABLE_QUERY_OPTIMIZER_HOTFIXES'
```
