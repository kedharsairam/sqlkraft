---
name: "To Generate Script to Change the Job Owner to S"
title: "To Generate Script to Change the Job Owner to S"
description: "diagnostic script for automation operations."
category: automation
tags: ["agent-job", "automation"]
pubDate: 2025-03-15
---

```sql
SELECT NAME,SUSER_SNAME(OWNER_SID) AS JOB_OWNER FROM MSDB.DBO.SYSJOBS

SELECT 'EXEC MSDB.DBO.SP_UPDATE_JOB @JOB_ID=N'''+ CONVERT(VARCHAR(MAX) ,JOB_ID) + CHAR(39)+ ', @OWNER_LOGIN_NAME=N''SA''' FROM MSDB.DBO.SYSJOBS
```
