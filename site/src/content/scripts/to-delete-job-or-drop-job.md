---
name: 'To Delete Job or Drop Job'
title: 'To Delete Job or Drop Job'
description: 'SQL Server diagnostic script for automation operations.'
category: automation
tags: ["agent-job", "automation"]
pubDate: 2025-03-15
---

```sql
USE msdb ;  
GO  

EXEC sp_delete_job  
    @job_name = N'jobname' ;  
GO
```
