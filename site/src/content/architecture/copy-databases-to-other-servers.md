---
title: "Copy Databases to Other Servers"
topic: "collation"
description: |
  Article
  
  •
  
  07/22/2024
  
  Applies to:
  
  SQL Server
  
  Sometimes you might find it useful to copy a database from one computer to another. Reasons
  
  include testing, checking consistency, developing software
tags:
  - "collation"
  - "copy-databases-to-other-servers"
pubDate: 2025-12-01
---

Article

•

07/22/2024

Applies to:

SQL Server

Sometimes you might find it useful to copy a database from one computer to another. Reasons

include testing, checking consistency, developing software, running reports, creating a mirror

database, or possibly to make the database available to remote-branch operations.

There are several ways to copy a database:

Use the Copy Database Wizard

You can use the Copy Database Wizard to copy or move databases between servers or to

upgrade a SQL Server database to a later version. For more information, see

Use the Copy

Database Wizard

.

Restore a database backup

To copy an entire database, you can use the BACKUP and RESTORE Transact-SQL

statements. Typically, restoring a full backup of a database is used to copy the database

from one computer to another for various reasons. For information on using backup and

restore to copy a database, see

Copy Databases with Backup and Restore

.

Use the Copy Database Wizard

Restore database

７

Note

To set up a mirror database for database mirroring, you must restore the database

onto the mirror server by using

.

For more information, see

.

```sql
RESTORE DATABASE <database_name> WITH NORECOVERY
```