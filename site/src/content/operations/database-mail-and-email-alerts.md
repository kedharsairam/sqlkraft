---
title: "Database Mail and email alerts"
topic: "linux-operations"
description: "07/03/2025 - Linux This article shows how to set up Database Mail and use it with SQL Server Agent ( ) on Linux. SQL SQL Ｕ Caution"
tags: ["linux-operations","database-mail-and-email-alerts"]
pubDate: "2025-12-01"
---

- Linux

This article shows how to set up Database Mail and use it with SQL Server Agent (

) on Linux.

Ｕ

Caution

```cmd
USE master
;
GO
EXECUTE sp_configure
'show advanced options'
, 1;
GO
RECONFIGURE
WITH
OVERRIDE;
GO
EXECUTE sp_configure
'Database Mail XPs'
, 1;
GO
RECONFIGURE;
GO
EXECUTE msdb.dbo.sysmail_add_account_sp
@account_name =
'SQLAlerts'
,
@description =
'Account for Automated DBA Notifications'
,
@email_address =
'sqlagenttest@example.com'
,
@replyto_address =
'sqlagenttest@example.com'
,
@display_name =
'SQL Agent'
,
@mailserver_name =
'smtp.example.com'
,
@port = 587,
@enable_ssl = 1,
@username =
'sqlagenttest@example.com'
,
@
password
=
'<password>'
;
GO
```
