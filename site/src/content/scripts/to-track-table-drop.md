---
name: "To Track Table Drop"
title: "To Track Table Drop"
description: "1) Read fn_dblog (try to get data from the log file) OR fn_dump_dblog (try to get data from the log backup)."
category: "database"
tags: ["database","table"]
pubDate: "2025-03-15"
---

```sql
--1) Read fn_dblog (try to get data from the log file) OR fn_dump_dblog (try to get data from the log backup).
--2) Server Side Traces
--3) Schema Changes History
--Database -> Reports -> Schema Changes History
--4) If alerts are configured then we get the information (WMI Alerts).
--5) Auditing

--6) Change Data Capture (CDC), can be enabled at DB Level or Table level also.
--7) Triggers (DDL)
```
