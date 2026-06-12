---
title: "No cache workflow"
topic: "query-processing"
description: ""
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

This article explains how SQL Server uses a security cache to validate permissions a principal

has to access securables.

The Database Engine organizes a hierarchical collection of entities, known as securables, which

can be secured with permissions. The most prominent securables are servers and databases,

but permissions can also be set at a finer level. SQL Server controls the actions of principals on

securables by ensuring they have the appropriate permissions.

The following diagram shows that a user, Alice, has a login at the server level, and a three

different users mapped to the same login at each different database.

To optimize the authentication process, SQL Server uses a security cache.

When the security cache is invalid, SQL Server follows a no cache workflow to validate

## permissions. This section describes the no cache workflow.



To demonstrate, consider the following query:

When the security cache is invalid, the service completes the steps described in the following

workflow before it resolves the query.

Run Query

Establish connection

Repeat same

processes for all roles

the user belong to

Validate Login

Create

SecContextToken and

LoginToken

Connect to database

Create UserToken

Check for membership

of special fixed

database roles

Get user permission

on all columns

Get user permission

on all tables

Get user permission

on all schemas

Get user permission

on database

Have necessary grants

No denies

Real query

execution begins

For SQL Server the tasks without a security cache include:

1. Connect to the instance.

2. Perform login validation.

3. Create the security context token and login token. Details of these tokens are explained in

the next section.

4. Connect to the database.

5. Create a database user token inside the database.

6. Check the membership of database roles. For example, db_datareader, db_datawriter, or

db_owner.

```sql
SELECT t1.Column1,
t2.Column1
FROM
Schema1.Table1
AS t1
INNER
JOIN
Schema2.Table2
AS t2
ON t1.Column1 = t2.Column2;
```
