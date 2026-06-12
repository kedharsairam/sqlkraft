---
title: "DCM and BCM pages"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

An IAM page has a header that indicates the starting extent of the range of extents mapped by

that page. An IAM page also has a bitmap in which each bit represents one extent. The first bit

in the map represents the first extent in the range, the second bit represents the second extent,

and so on. If a bit is

, the extent it represents isn't allocated to the allocation unit owning the

IAM page. If the bit is

, the extent it represents is allocated to the allocation unit owning the

IAM page.

When the Database Engine has to insert a new row and no space is available in the current

page, it uses IAM and PFS pages to find a page to allocate the row. For heap or text/LOB

pages, it similarly uses IAM and PFS pages to find a page with sufficient space to hold the row.

The Database Engine uses IAM pages to find the extents allocated to the allocation unit. For

each extent, it searches the PFS pages to see if there's a page that can be used.

For BTree indexes, the insertion point of a new row is determined by the index key, but when a

new page is needed, the previously described process occurs.

The Database Engine allocates a new extent to an allocation unit when it can't quickly find a

page in an existing extent with sufficient space to hold the row being inserted.

The Database Engine uses two types of system pages to track extents modified since the last

full backup, and extents modified by bulk copy operations.

Differential Changed Map (DCM) pages speed up differential backups. Bulk Changed Map

(BCM) speed up bulk copy operations when a database is using the bulk-logged recovery

model. Like the GAM and SGAM pages, these structures are bitmaps in which each bit

represents a single extent.

### BCM pages

These pages track the extents that have changed since the last full database backup. If

the bit for an extent is

, the extent has been modified. If the bit is

, the extent hasn't

been modified.

Differential backups read the DCM pages to determine which extents have been

modified. This reduces the number of pages that a differential backup must read and

write. The length of time that a differential backup takes is proportional to the number of

extents modified since the last full database backup, and not the total size of the

database.

These pages track the extents that have been modified by bulk-logged operations since

the last transaction log backup. If the bit for an extent is

, the extent has been modified.

If the bit is

, the extent hasn't been modified.

Although BCM pages appear in all databases, they are only relevant when the database is

using the bulk-logged

recovery model. In this recovery model, when a transaction log

backup is performed, the backup process scans BCM pages for extents that have been

modified. It includes those extents in the log backup to enable recovery if the database is

restored from a database backup and a sequence of transaction log backups.

BCM pages aren't relevant in a database that is using the simple recovery model, because

no bulk-logged operations are fully logged. They also aren't relevant in a database that is

using the full recovery model, because that recovery model treats bulk-logged operations

as fully logged operations.

The DCM and BCM pages are stored at the same GAM intervals of approximately 4 GiB as the

GAM and SGAM pages. The DCM and BCM pages follow the GAM and SGAM pages in a

physical file as follows:

I/O fundamentals

sys.allocation_units (Transact-SQL)

Heaps (Tables without Clustered Indexes)

sys.dm_db_page_info (Transact-SQL)

Read data pages in the Database Engine
