---
title: "Logins & Jobs after role switching"
topic: "high-availability"
description: ""
tags: ["high-availability","logins-jobs-after-role-switching"]
pubDate: "2025-12-01"
---

When deploying a high-availability or disaster-recovery solution for a SQL Server database, it is

important to reproduce relevant information that is stored for the database in the

or

databases. Typically, the relevant information includes the jobs of the primary/principal

database and the logins of users or processes that need to connect to the database. You

should duplicate this information on any instance of SQL Server that hosts a secondary/mirror

database. If possible after roles are switched, it is best to programmatically reproduce the

information on the new primary/principal database.

On every server instances that hosts a copy of the database, you should reproduce the logins

that have permission to access the principal database. When the primary/principal role

switches, only users whose logins exist on the new primary/principal server instance can access

the new primary/principal database. Users whose logins are not defined on the new

primary/principal server instance are orphaned and cannot access the database.

If a user is orphaned, create the login on the new primary/principal server instance and run

sp_change_users_login. For more information, see

Troubleshoot Orphaned Users (SQL Server).

If an application uses SQL Server Authentication or a local Windows login, mismatched SIDs

can prevent the application's login from resolving on a remote instance of SQL Server. The

mismatched SIDs cause the login to become an orphaned user on the remote server instance.

This issue can occur when an application connects to a mirrored or log shipping database after

a failover or to a replication subscriber database that was initialized from a backup.

To prevent this issue, we recommend that you take preventative measures when you set up

such an application to use a database that is hosted by a remote instance of SQL Server.

Prevention involves transferring the logins and the passwords from the local instance of SQL

Server to the remote instance of SQL Server. For more information about how to prevent this

issue, see KB article 918992 -

How to transfer logins and passwords between instances of SQL

Server

).
