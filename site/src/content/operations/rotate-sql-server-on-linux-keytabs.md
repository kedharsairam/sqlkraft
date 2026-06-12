---
title: "Rotate SQL Server on Linux keytabs"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  Based on your organization's security best practices, you might be required to rotate the

  password regularly for the Windows Active Directory account provided as

  i
tags:
  - "linux-operations"
  - "rotate-sql-server-on-linux-keytabs"
pubDate: 2025-12-01
---

SQL Server

on Linux

Based on your organization's security best practices, you might be required to rotate the

password regularly for the Windows Active Directory account provided as

in

, or any other account that owns the service principal

names (SPN) for the SQL Server service. The supported method for changing the password for

the account is documented in this article. The password change takes effect without the need to

restart the SQL Server service on Linux.

The

tool is used to update the keytab. The

command must be run from a domain-

joined machine. For more information about

and how to download the tool, see

Introduction to adutil - Active Directory utility.

It's critical to update the new password in the keytab with the next

number before updating

it in Active Directory. Using the next

number prevents the SQL Server service from the need

to be restarted after the password change. If you update the password in Active Directory first,

and then change the keytab, you must restart the SQL Server service to ensure that Active

Directory authentication works properly.

Let's consider an example. Active Directory authentication is already enabled for SQL Server on

Linux. In the

file, you set the

to. The account

is already created in Active Directory, and the keytab is also created at the

default location. Now you want to change the password

for the. Here are the steps that you need to follow:

1.

Install adutil

on the domain joined machine.

2. Obtain or renew the Kerberos TGT (ticket-granting ticket) using the

command. Use a

privileged account for the

command. The account needs to have permission to

connect to the domain and should be able to create accounts and SPNs in the domain. In

this case, we're using the account

that has permissions to

create accounts and SPNs in our domain called.

```cmd
network.privilegedadaccount mssql.conf mssql.conf network.privilegedadaccount sqluser
```
