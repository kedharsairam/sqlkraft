---
name: "sys.dm_external_script_requests"
title: "sys.dm_external_script_requests"
category: "execution"
description: "SQL Server 2016 (13.x) and later Returns a row for each active worker account that is running an external script."
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: |
  EXECUTE ANY EXTERNAL
  SCRIPT
---

## Description

SQL Server 2016 (13.x) and later Returns a row for each active worker account that is running an external script. ID of the process that sent the external script request. This corresponds to the process ID as received the SQL instance. Keyword that represents a supported script language. Number indicating the number of parallel processes that were created. This value might be different from the number of

## Syntax

```sql
EXECUTE ANY EXTERNAL
SCRIPT
```

## Permissions

Article • 02/28/2023 SQL Server 2016 (13.x) and later Azure SQL Managed Instance Returns a row for each active worker account that is running an external script. external_script_request_id ID of the process that sent the external script request. This corresponds to the process ID as received the SQL instance. language Keyword that represents a supported script language. degree_of_parallelism Number indicating the number of parallel processes that were created. This value might be different from the number of parallel processes that were requested. external_user_name The Windows worker account under which the script was executed. Requires permission on server. Requires VIEW SERVER PERFORMANCE STATE permission on the server. ７ This dynamic management view (DMV) is available only if you have installed and enabled the feature that supports external script execution. For more information, see , , and . ﾉ ７ Users who run external scripts must have the additional permission , however, this DMV can be used by administrators without this permission.
