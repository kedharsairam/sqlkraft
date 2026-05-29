---
name: 'sys.fn_servershareddrives'
title: 'sys.fn_servershareddrives'
category: 'system'
description: 'Returns the names of shared drives used by the clustered server.'
tags: ["function"]
pubDate: 2026-05-29
---

The following example uses

to query on a clustered server instance:

Here's the result set.

DriveName

--------

m

n

sys.dm_io_cluster_valid_path_names (Transact-SQL)

sys.dm_io_cluster_shared_drives (Transact-SQL)

sys.fn_virtualservernodes (Transact-SQL)

See Also

```sql
fn_servershareddrives
```

```sql
SELECT * FROM fn_servershareddrives();
```
