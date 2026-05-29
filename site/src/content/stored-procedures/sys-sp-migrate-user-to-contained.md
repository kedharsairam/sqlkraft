---
name: 'sys.sp_migrate_user_to_contained'
title: 'sp_migrate_user_to_contained'
category: 'general'
description: 'Converts a database user that is mapped to a SQL Server login, to a contained database user with password. In a contained database, use this procedure to remove dependencies on the instance of SQL Server where the database is installed. separates the user from the original SQL Server login, so that settings such as password and default language can be administered separately for the contained data'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_migrate_user_to_contained'
---

## Description

Converts a database user that is mapped to a SQL Server login, to a contained database user with password. In a contained database, use this procedure to remove dependencies on the instance of SQL Server where the database is installed. separates the user from the original SQL Server login, so that settings such as password and default language can be administered separately for the contained database.

## Syntax

```sql
sp_migrate_user_to_contained
```

## Arguments

Applies to:


Converts a database user that is mapped to a SQL Server login, to a contained database user


with password. In a contained database, use this procedure to remove dependencies on the


instance of SQL Server where the database is installed.


separates the user from the original SQL Server login, so that settings such as password and


default language can be administered separately for the contained database.


can be used before moving the contained database to a


different instance of the SQL Server Database Engine to eliminate dependencies on the current


SQL Server instance logins.


Be careful when using


, as you'll not be able to reverse the


effect. This procedure is only used in a contained database. For more information, see


Arguments for extended stored procedures must be entered in the specific order as


described in the


section. If the parameters are entered out of order, an error


message occurs.


Migrate to a Partially Contained Database


Contained Databases


Related content
