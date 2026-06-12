---
title: "Environment variables"
topic: "linux-operations"
description: "on Linux You can use several different environment variables to configure SQL Server on Linux."
tags: ["linux-operations","environment-variables"]
pubDate: "2025-12-01"
---

on Linux

You can use several different environment variables to configure SQL Server on Linux. These

variables are used in two scenarios:

To configure initial setup with the

command.

To configure a new

Linux container image.

Description

Sets the

variable to any value to confirm your acceptance of the

End-User Licensing Agreement. Required setting for the SQL Server image.

Configures the

password.

The

environment variable is deprecated. Use

instead.

Sets the name of a database to create on container startup.

If

is set, sets the name of a non-

user to create on container startup.

The user is granted access rights on the

database. If this variable is

used,

must also be set. If

isn't set, this variable is

ignored.

Sets the password of the user whose name is in. If this variable is

used,

must also be set. If

isn't set, this variable is ignored.

Sets the

edition

or product key. Possible values are listed in the

following

editions

table. If you specify a product key, it must be in the



Tip

To configure SQL Server after these setup scenarios, see.

ﾉ

Expand table

```cmd
mssql-conf setup
ACCEPT_EULA
ACCEPT_EULA
MSSQL_SA_PASSWORD sa
```
