---
name: "sys.sp_control_dbmasterkey_password"
title: "sp_control_dbmasterkey_password"
category: "general"
description: "Adds or drops a credential containing the password needed to open a database master key Transact-SQL syntax conventions Specifies the name of the database associated with this credential. Can't be a system database. Specifies the password of the DMK. Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an error"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_control_dbmasterkey_password @db_name =
  'db_name'
  , @password =
  'password'
  , @action = {
  N
  'add'
  |
  N
  'drop'
  }
---

## Description

Adds or drops a credential containing the password needed to open a database master key Transact-SQL syntax conventions Specifies the name of the database associated with this credential. Can't be a system database. Specifies the password of the DMK. Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an error

## Syntax

```sql
sp_control_dbmasterkey_password @db_name =
'db_name'
, @password =
'password'
, @action = {
N
'add'
|
N
'drop'
}
```

## Permissions

ﾃ Summarize this article for me Applies to: SQL Server Azure SQL Managed Instance Returns a row for each database master key password added by using the stored procedure. The passwords that are used to protect the master keys are stored in the credential store. The credential name follows this format: ##DBMKEY*<database_family_guid>*<random_password_guid>##. The password is stored as the credential secret. For each password added by using , there's a row in . Each row in this view shows a and the of a database the master key of which is protected by the password associated with that credential. A join with on the returns useful fields, such as the and credential name. Description ID of the credential to which the password belongs. This ID is unique within the server instance. Unique ID of the original database at creation. This GUID remains the same after the database is restored or attached, even if the database name is changed. If automatic decryption by the service master key fails, SQL Server uses the to identify credentials that might contain the password used to protect the database master key. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . SQL Server 2022 (16.x) and later versions require VIEW SERVER SECURITY STATE permission on the server. ﾉ Expand table
