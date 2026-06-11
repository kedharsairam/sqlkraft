---
name: "To Get an Email Notification"
title: "To Get an Email Notification"
description: ""
category: automation
tags: ["automation"]
pubDate: 2025-03-15
---

```sql
--add this stored procedure as a new step in a job and setup exec msdb.dbo.sp_send_dbmail
@profile_name = 'profilename'
@recipients = 'youremail'
@subject = 'notification for job success or failure'
@body = 'job succeded or failed'
```
