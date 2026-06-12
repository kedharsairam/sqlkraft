---
title: "Disk space example"
topic: "filestream"
description: "Whenever an index is created, rebuilt, or dropped, disk space for both the old (source) and n"
tags: ["filestream","disk-space-example"]
pubDate: "2025-12-01"
---

Whenever an index is created, rebuilt, or dropped, disk space for both the old (source) and new

(target) structures is required in their appropriate files and filegroups. The old structure isn't

deallocated until the index creation transaction commits. Additional temporary disk space for

sorting operations might also be needed. For more information, see

Disk space requirements

for index DDL operations.

In this example, disk space requirements to create a clustered index are determined.

Assume the following conditions are true before creating the clustered index:

The existing table (heap) contains 1 million rows. Each row is 200 bytes long.

Nonclustered index A contains 1 million rows. Each row is 50 bytes long.

Nonclustered index B contains 1 million rows. Each row is 80 bytes long.

The index create memory option is set to 2 MB.

A fill factor value of 80 is used for all existing and new indexes. This means the pages are

80 percent full.

In the following steps, both temporary disk space to be used during the index operation and

permanent disk space to store the new indexes are calculated. The calculations shown are

approximate; results are rounded up and consider only the size of index leaf level. The tilde (~)

is used to indicate approximate calculations.

1. Determine the size of the source structures.

: 1 million \* 200 bytes ~ 200 MB

: 1 million \* 50 bytes / 80% ~ 63 MB

: 1 million \* 80 bytes / 80% ~ 100 MB

Total size of existing structures: 363 MB

７

Note

As a result of creating a clustered index, the two nonclustered indexes must be rebuilt to

replace the row indicator with the new clustered index key.
