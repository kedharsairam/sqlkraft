---
name: "To Create Linked Server"
title: "To Create Linked Server"
description: "to connect another sql server"
category: "security-audit"
tags: ["security-audit"]
pubDate: "2025-03-15"
---

```sql
--to connect another sql server
EXEC master.dbo.sp_addlinkedserver @server = N'servername', @srvproduct=N'SQL Server'
EXEC master.dbo.sp_addlinkedsrvlogin @rmtsrvname = N'servername', @rmtuser = N'loginname', @rmtpassword = N'[password]'
```
