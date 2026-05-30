---
name: "Deprecation notice"
title: "Deprecation notice"
category: "statements"
description: "In some cases, a user can use a database without having a database user account (a database"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

In some cases, a user can use a database without having a database user account (a database

principal in the database). This condition can happen in the following situations:

A login has

privileges.

A Windows user doesn't have an individual database user account (a database principal in

the database), but accesses a database as a member of a Windows group that has a

database user account (a database principal for the Windows group).

A Microsoft Entra user doesn't have an individual database user account (a database

principal in the database), but accesses a database as a member of a Microsoft Entra

group that has a database user account (a database principal for the Microsoft Entra

group).

When a user without a database user account creates an object without specifying an existing

schema, a database principal and default schema are created in the database automatically for

that user. The created database principal and schema have the same name as the name that

user used when connecting to SQL Server (the SQL Server authentication login name or the

Windows user name).

This behavior is necessary to allow users that are based on Windows groups to create and own

objects. However, it can result in the unintentional creation of schemas and users. To avoid

implicitly creating users and schemas, whenever possible explicitly create database principals

and assign a default schema. Or explicitly state an existing schema when creating objects in a

database, using two or three-part object names.

The implicit creation of a Microsoft Entra user isn't possible on SQL Database. Since creating a

Microsoft Entra user from external provider must check the user's status in Microsoft Entra ID,

creating the user fails with error 2760:

And then error 2759:

Attempts to create or alter schemas result in the error 15151:

, also followed by error 2759. To

work around these errors, either create the Microsoft Entra user from an external provider, or

alter the Microsoft Entra group to assign a default schema. Then rerun the statement creating

the object.

In SQL analytics endpoint in Microsoft Fabric and Warehouse in Microsoft Fabric, schema

names can't contain

or

or end with a

.

```sql
CONTROL SERVER
```

```sql
The specified schema name "<user@domain>" either does not exist or you do not have permission to use it.
```

```sql
CREATE SCHEMA failed due to previous errors.
```

```sql
Cannot find the user '',
because it does not exist or you do not have permission.
```

```sql
/
```

```sql
\
```

```sql
.
```
