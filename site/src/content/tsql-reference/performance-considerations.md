---
name: "Performance considerations"
title: "Performance considerations"
category: "statements"
description: "Beginning with SQL Server 2017 (14.x),"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Beginning with SQL Server 2017 (14.x),

supports the CSV format, as does Azure

SQL Database.

Before SQL Server 2017 (14.x), comma-separated value (CSV) files aren't supported by SQL

Server bulk-import operations. However, in some cases, a CSV file can be used as the data file

for a bulk import of data into SQL Server. For information about the requirements for

importing data from a CSV data file, see

Prepare data for bulk export or import.

For information about when row-insert operations that are performed by bulk import into SQL

Server are logged in the transaction log, see

Prerequisites for minimal logging in bulk import.

Minimal logging isn't supported in Azure SQL Database.

When using a format file with

, you can specify up to 1,024 fields only. This is same

as the maximum number of columns allowed in a table. If you use a format file with

with a data file that contains more than 1,024 fields,

generates the 4822

error. The

bcp utility

doesn't have this limitation, so for data files that contain more than 1,024

fields, use

without a format file or use the

command.

If the number of pages to be flushed in a single batch exceeds an internal threshold, a full scan

of the buffer pool might occur to identify which pages to flush when the batch commits. This

full scan can hurt bulk-import performance. A likely case of exceeding the internal threshold

occurs when a large buffer pool is combined with a slow I/O subsystem. To avoid buffer

overflows on large machines, either don't use the

hint (which removes the bulk

optimizations) or use a smaller batch size (which preserves the bulk optimizations).

You should test various batch sizes with your data load to find out what works best for you.

Keep in mind that the batch size has partial rollback implications. If your process fails and

before you use

again, you might have to do additional manual work to remove a

part of the rows that were inserted successfully, before a failure occurred.

## osql

## Storage Blob Data Contributor

```sql
BULK INSERT
```

```sql
BULK INSERT
```

```sql
BULK
INSERT
```

```sql
BULK INSERT
```

```sql
BULK INSERT
```

`TABLOCK`

```sql
BULK INSERT
```
