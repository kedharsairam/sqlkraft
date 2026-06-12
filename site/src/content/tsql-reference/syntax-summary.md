---
name: "Syntax Summary"
title: "Syntax Summary"
category: "statements"
description: "CREATE USER can't be used to create a guest user because the guest user already exists inside"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

CREATE USER can't be used to create a guest user because the guest user already exists inside

every database. You can enable the guest user by granting it CONNECT permission, as shown:

Information about database users is visible in the

sys.database_principals

catalog view.

Use the syntax extension

to create server-level Microsoft Entra logins

in Azure SQL Database and Azure SQL Managed Instance. Microsoft Entra logins allow

database-level Microsoft Entra principals to be mapped to server-level Microsoft Entra logins.

To create a Microsoft Entra user from a Microsoft Entra login use the following syntax:

When creating the user in the Azure SQL database, the

login_name

must correspond to an

existing Microsoft Entra login, or else using the

clause will only

create a Microsoft Entra user without a login in the

database. For example, this

command will create a contained user:

The following list shows possible syntax for users based on logins. The default schema options

aren't listed.

### Users that authenticate at the database

### master

### Users based on Windows principals without logins in the

#### master

### system database

### Users that cannot authenticate

The following list shows possible syntax for users that can only be used in a contained

database. The users created won't be related to any logins in the

database. The default

schema and language options aren't listed.

The following list shows possible syntax for users that have access to the Database Engine

through a Windows group but don't have a login in the

system database. This syntax

can be used in all types of databases. The default schema and language options aren't listed.

This syntax is similar to users based on logins in

, but this category of user doesn't have

a login in. The user must have access to the Database Engine through a Windows

group login.

This syntax is similar to contained database users based on Windows principals, but this

category of user doesn't get new access to the Database Engine.

The following list shows possible syntax for users that can't log in to SQL Server.

）

Important

This syntax grants users access to the database and also grants new access to the

Database Engine.

```sql
FROM EXTERNAL PROVIDER
```

`master`

```sql
CREATE USER [Domain1\WindowsUserBarry]
CREATE USER [Domain1\WindowsUserBarry] FOR LOGIN Domain1\WindowsUserBarry
CREATE USER [Domain1\WindowsUserBarry] FROM LOGIN Domain1\WindowsUserBarry
CREATE USER [Domain1\WindowsGroupManagers]
CREATE USER [Domain1\WindowsGroupManagers] FOR LOGIN [Domain1\WindowsGroupManagers]
CREATE USER [Domain1\WindowsGroupManagers] FROM LOGIN [Domain1\WindowsGroupManagers]
CREATE USER SQLAUTHLOGIN
GRANT
CONNECT
TO guest;
GO
CREATE
USER
[Microsoft_Entra_principal]
FROM
LOGIN [Microsoft Entra login];
CREATE
USER
[bob@contoso.com]
FROM
EXTERNAL
PROVIDER;
```

```sql
CREATE USER SQLAUTHLOGIN FOR LOGIN SQLAUTHLOGIN
CREATE USER SQLAUTHLOGIN FROM LOGIN SQLAUTHLOGIN
```

```sql
CREATE USER [Domain1\WindowsUserBarry]
CREATE USER [Domain1\WindowsGroupManagers]
CREATE USER Barry WITH PASSWORD = 'sdjklalie8rew8337!$d'
```

`master`

`master`

`master`

```sql
CREATE USER [Domain1\WindowsUserBarry]
CREATE USER [Domain1\WindowsUserBarry] FOR LOGIN Domain1\WindowsUserBarry
CREATE USER [Domain1\WindowsUserBarry] FROM LOGIN Domain1\WindowsUserBarry
CREATE USER [Domain1\WindowsGroupManagers]
CREATE USER [Domain1\WindowsGroupManagers] FOR LOGIN [Domain1\WindowsGroupManagers]
CREATE USER [Domain1\WindowsGroupManagers] FROM LOGIN [Domain1\WindowsGroupManagers]
```

```sql
CREATE USER RIGHTSHOLDER WITHOUT LOGIN
```
