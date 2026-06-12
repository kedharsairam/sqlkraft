---
title: "Troubleshoot AD Authentication"
topic: "linux-operations"
description: "- Linux This article helps you troubleshoot Active Directory Domain Services authentication issues with SQL Server on Linux and containers. It includ"
tags: ["linux-operations","troubleshoot-ad-authentication"]
pubDate: "2025-12-01"
---

- Linux

This article helps you troubleshoot Active Directory Domain Services authentication issues with

on Linux and containers. It includes prerequisite checks and tips for a successful

Active Directory configuration, and a list of common errors and troubleshooting steps.

Before you begin troubleshooting, you must validate the current user,

, Service

Principal Name (SPN), and realm settings.

1. Obtain or renew the Kerberos TGT (ticket-granting ticket) using

:

Bash

2. Run the following command, making sure that the user under which you're running this

command has access to the

:

Bash

For more information about the

command, view the help using

command.

1. DNS lookups on the domain name and NetBIOS name should return the same IP address,

which normally matches the IP address for the domain controller (DC). Run these

commands from the SQL Server host machine.

Bash

```cmd
mssql.conf kinit mssql.keytab validate-ad-config
/opt/mssql/bin/mssql-conf validate-ad-config --help
```
