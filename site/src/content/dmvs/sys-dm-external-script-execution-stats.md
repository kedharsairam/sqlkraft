---
name: "sys.dm_external_script_execution_stats"
title: "sys.dm_external_script_execution_stats"
category: "execution"
description: "2016 (13.x) and later Returns one row for each type of external script request. The external script requests are grouped by the supported external script language. One row is generated for each registered external script function. Arbitrary external script functions aren't recorded unless sent by a Name of the registered external script language."
tags: ["execution","dmv"]
pubDate: "2026-05-29"
syntax: |
  SELECT
      counter_name, counter_value
      FROM
      sys.dm_external_script_execution_stats
      WHERE
      language
      =
      'R'
      ;
---

## Description

2016 (13.x) and later Returns one row for each type of external script request. The external script requests are grouped by the supported external script language. One row is generated for each registered external script function. Arbitrary external script functions aren't recorded unless sent by a Name of the registered external script language. Each external script must specify the language in the script request to start the associated launcher.

## Syntax

```sql
SELECT counter_name, counter_value
FROM sys.dm_external_script_execution_stats
WHERE language
=
'R'
;
```

## Permissions

Article • 06/19/2023 SQL Server 2016 (13.x) and later Azure SQL Managed Instance Returns one row for each type of external script request. The external script requests are grouped by the supported external script language. One row is generated for each registered external script function. Arbitrary external script functions aren't recorded unless sent by a parent process, such as. Name of the registered external script language. Each external script must specify the language in the script request to start the associated launcher. Name of a registered external script function. Isn't nullable. Total number of instances that the registered external script function has been called on the server. This value is cumulative, beginning with the time that the feature was installed on the instance, and can't be reset. For SQL Server 2019 (15.x) and previous versions, requires VIEW SERVER STATE permission on server. For SQL Server 2022 (16.x) and later versions, requires VIEW SERVER PERFORMANCE STATE permission on the server. Users who run external scripts must have the additional permission EXECUTE ANY EXTERNAL SCRIPT. However, this DMV can be used by administrators without this permission. ７ This dynamic management view (DMV) is available only if you have installed and enabled the feature that supports external script execution. For more information, see , and. ﾉ
