---
name: 'sys.configurations'
title: 'sys.configurations'
category: 'configuration'
description: 'The following query can be used to determine if any configured values haven''t been installed:'
tags: ["catalog-view", "configuration"]
pubDate: 2026-05-29
---

The following query can be used to determine if any configured values haven't been installed:

SQL

If the value equals the change for the configuration option you made but the

isn't

the same, either the RECONFIGURE command wasn't run or has failed, or the server engine

must be restarted.

There are configuration options where the value and value_in_use might not be the same and

this is expected behavior. For example:

"max server memory (MB)" - The default configured value of 0 shows up as

=

2147483647

"min server memory (MB)" - The default configured value of 0 might show up as

= 8 (32bit) or 16 (64bit). In some cases, the

is 0. In this situation, the "true"

is 8 (32bit) or 16 (64bit).

The

column can be used to determine if the configuration option requires a restart.

is_dynamic=1 means that when the RECONFIGURE(T-SQL) command is executed, the new

value takes effect "immediately" (in some cases the server engine might not evaluate the new

value immediately but does so in the normal course of its execution). is_dynamic=0 means the

changed configuration value doesn't take effect until the server is restarted even though the

RECONFIGURE(T-SQL) command was executed.

For a configuration option that isn't dynamic there's no way to tell if the RECONFIGURE(T-SQL)

command has been run to perform the first step of installing the configuration change. Before

you restart SQL Server to install a configuration change, run the RECONFIGURE(T-SQL)

command to ensure all configuration changes take effect after a SQL Server restart.

Requires membership in the

role.

７

Note

The config_value in the result set of sp_configure is equivalent to the

column. The

is equivalent to the

column.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

Server-wide Configuration Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Last updated on 03/03/2026


## Permissions for SQL Server 2022 and later
Related content

```sql
select
*
from
sys.configurations
where
value
!= value_in_use
```
