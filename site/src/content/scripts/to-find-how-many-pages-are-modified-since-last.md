---
name: "To Find How many Pages are Modified since last"
title: "To Find How many Pages are Modified since last"
description: "diagnostic script for backup-restore operations."
category: "backup-restore"
tags: ["backup-restore"]
pubDate: 2025-03-15
---

```sql
select file_id, total_page_count, modified_extent_page_count,
(modified_extent_page_count * 100) / total_page_count [%change]
from sys.dm_db_file_space_usage
```
