---
title: "Log blocks"
topic: "locking"
description: "Additionally, SQL Server can log a"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Additionally, SQL Server can log a

MSSQLSERVER_9017

error when you restore a database that

has a large number of VLFs:

Output

For more information, see

MSSQLSERVER_9017

.

To keep the total number of VLFs at a reasonable amount, such as a maximum of several

thousand, you can reset the transaction log file to contain a smaller number of VLFs by

performing the following steps:

1. Shrink the transaction log files manually.

2. Grow the files to the required size manually in one step using the following T-SQL script:

After you set the new layout of the transaction log file with fewer VLFs, review and make

necessary changes to the autogrow settings of the transaction log. This setting validation

ensures that the log file avoids encountering the same problem in the future.

Before you perform any of these operations, make sure that you have a valid restorable backup

in case you encounter issues later.

To determine the optimal VLF distribution for the current transaction log size of all databases in

a given instance, and the required growth increments to achieve the required size, you can use

the following GitHub script to

fix VLFs

.

７

Note

This step is also possible in SQL Server Management Studio, using the database

properties page.

```sql
ALTER DATABASE <database name> MODIFY FILE (NAME='Logical file name of transaction
log', SIZE = <required size>);
```

```sql
Database %ls has more than %d virtual log files which is excessive. Too many virtual
log files can cause long startup and backup times. Consider shrinking the log and
using a different growth increment to reduce the number of virtual log files.
```
