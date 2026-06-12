---
title: "Troubleshoot Database Mirroring Configuration"
topic: "high-availability"
description: "This topic provides information to help you troubleshoot problems in setting up a database mirroring session."
tags: ["high-availability","troubleshoot-database-mirroring-configuration"]
pubDate: "2025-12-01"
---

This topic provides information to help you troubleshoot problems in setting up a database

mirroring session.

Error Message 1418

This SQL Server message indicates that the server network address cannot be

reached or does not exist, and it suggests that you verify the network address

name and reissue the command.

Accounts

Discusses requirements for correctly configuring the accounts under which

is running.

Endpoints

Discusses requirements for correctly configuring the database mirroring

endpoint of each server instance.

SystemAddress

Summarizes the alternatives for specifying the system name of a server

instance in a database mirroring configuration.

Network access

Documents the requirement that each the server instance be able to access

the ports of the other server instance or instances over TCP.

Mirror database

preparation

Summarizes the requirements for preparing the mirror database to enable

mirroring to start.

Failed create-file

operation

Describes how to respond to a failed create-file operation.

Starting mirroring by

Using Transact-SQL

Describes the required order for ALTER DATABASE

database_name

SET

PARTNER

partner_server

statements.

Cross-Database

Transactions

An automatic failover could lead to automatic and possibly incorrect resolution

of in-doubt transactions. For this reason database mirroring does not support

cross-database transactions.

７

Note

Ensure that you are meeting all the

prerequisites for database mirroring.

ﾉ

Expand table
