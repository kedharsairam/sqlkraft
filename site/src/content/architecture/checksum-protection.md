---
title: "Checksum protection"
topic: "io-fundamentals"
description: "and the command that triggered the read continues. If the retry attempts fail, the command"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

and the command that triggered the read continues. If the retry attempts fail, the command

fails with the

MSSQLSERVER_824

error.

The kind of page protection used is an attribute of the database containing the page.

Checksum protection is the default protection for databases created in SQL Server 2005 (9.x)

and later versions. The page protection mechanism is specified at database creation time, and

can be altered by using

. You can determine the current page protection

setting by querying the

column in the

sys.databases

catalog view or the

property of the

DATABASEPROPERTYEX

function.

Torn page protection, introduced in SQL Server 2000 (8.x), is primarily a way of detecting page

corruptions due to power failures. For example, an unexpected power failure might leave only

part of a page written to disk. When torn page protection is used, a specific 2-bit signature

pattern for each 512-byte sector in the 8-kilobyte (KB) database page and stored in the

database page header when the page is written to disk.

When the page is read from disk, the torn bits stored in the page header are compared to the

actual page sector information. The signature pattern alternates between binary

and

with every write, so it's always possible to tell when only a portion of the sectors made it to

disk: if a bit is in the wrong state when the page is later read, the page was written incorrectly

and a torn page is detected. Torn page detection uses minimal resources; however, it doesn't

detect all errors caused by disk hardware failures. For information on setting torn page

detection, see

ALTER DATABASE SET Options

.

Checksum protection, introduced in SQL Server 2005 (9.x), provides stronger data integrity

checking. A checksum is calculated for the data in each page that is written, and stored in the

page header. Whenever a page with a stored checksum is read from disk, the database engine

recalculates the checksum for the data in the page and raises error 824 if the new checksum is

different from the stored checksum. Checksum protection can catch more errors than torn

７

Note

If the page protection setting is changed, the new setting doesn't immediately affect the

entire database. Instead, pages adopt the current protection level of the database

whenever they are written next. This means that the database might be composed of

pages with different kinds of protection.

### PAGE_VERIFY

```sql
ALTER DATABASE SET
```

```sql
page_verify_option
```

```sql
IsTornPageDetectionEnabled
```

```sql
01
```

```sql
10
```
