---
name: "To View Content inside a Page"
title: "To View Content inside a Page"
description: "this is useful to findout the modified extents"
category: backup-restore
tags: ["backup-restore"]
pubDate: 2025-03-15
---

```sql
--this is useful to findout the modified extents
--first turn on this trace flag dbcc tranceon (3604)

--then use the following command to view the content dbcc page ('databasename', file_id, page_number, viewing_type ) with tableresults
--ex: DBCC PAGE('databasename',1,???,3)   --Specify Data Page Number
GO
```
