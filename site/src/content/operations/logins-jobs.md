---
title: "Logins & jobs"
topic: "high-availability"
description: "You should routinely maintain the same set of user logins and SQL Server Agent jobs on every primary database of an Always On availability group (AG),"
tags: ["high-availability","logins-jobs"]
pubDate: "2025-12-01"
---

You should routinely maintain the same set of user logins and SQL Server Agent jobs on every

primary database of an Always On availability group (AG), and the corresponding secondary

databases. The logins and jobs must be reproduced on every instance of SQL Server that hosts

an availability replica for the AG.

Agent jobs

You need to manually copy relevant jobs from the server instance that hosts the original

primary replica to the server instances that host the original secondary replicas. For all

databases, you need to add logic at the beginning of each relevant job to make the job

execute only on the primary database, that is, only when the local replica is the primary

replica for the database.

The server instances that host the availability replicas of an AG might be configured

differently, with different drive letters for example. The jobs for each availability replica

must allow for any such differences.

Backup jobs can use the

sys.fn_hadr_backup_is_preferred_replica

function to identify

whether the local replica is the preferred one for backups, according to the AG backup

preferences. Backup jobs created using the

Use the Maintenance Plan Wizard

natively use

this function. For other backup jobs, we recommend that you use this function as a

condition in your backup jobs, so they execute only on the preferred replica. For more

information, see

Offload supported backups to secondary replicas of an availability group.

If you're using contained databases, you can configure contained users in the databases,

and for these users, you don't need to create logins on the server instances that host a

secondary replica. For a non-contained availability database, you need to create users for

the logins on the server instances that host the availability replicas. For more information,

see

CREATE USER.

If any of your applications use SQL Server Authentication or a local Windows login, see

Logins Of Applications That Use SQL Server Authentication or a Local Windows Login

,

later in this article.
