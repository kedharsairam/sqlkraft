---
title: "Configure accounts"
topic: "high-availability"
description: ""
tags: ["high-availability","configure-accounts"]
pubDate: "2025-12-01"
---

For two server instances to connect to each other's

database mirroring endpoint

point, the

login account of each instance requires access to the other instance. Also, each login account

requires connect permission to the Database Mirroring endpoint of the other instance.

The impact of this requirement depends on whether the server instances run as the same

domain user account:

If the server instances run as the same domain user account, the correct user logins exist

automatically in both

databases. This simplifies the security configuration for

Database Mirroring and Always On Availability Groups.

If the server instances run as different user accounts, user logins on the server instance

that hosts the principal server or primary replica must be manually reproduced on the

server instance that hosts the mirror server or on every server instance that hosts a

secondary replica. For more information, see

Create a Login for a Different Account

and

Grant Connect Permission

, later in this topic.

If two server instances run as different accounts, the system administrator must use the CREATE

LOGIN Transact-SQL statement to create a login for the startup service account of the remote

instance for each server instance. For more information, see

CREATE LOGIN (Transact-SQL).

）

Important

To create a more secure environment, consider using separate domain accounts for

each server instance.

）

Important

If you run SQL Server under a non-domain account, you must use certificates. For more

information, see.
