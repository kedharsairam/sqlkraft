---
name: "Additional remarks about creating indexes"
title: "Additional remarks about creating indexes"
category: "statements"
description: "Under certain conditions, spatial indexes support a number of set-oriented geometry methods."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

Under certain conditions, spatial indexes support a number of set-oriented geometry methods.

For more information, see

Spatial Indexes Overview.

By default, if a spatial index is created on a partitioned table, the index is partitioned according

to the partition scheme of the table. This assures that index data and the related row are stored

in the same partition.

In this case, to alter the partition scheme of the base table, you would have to drop the spatial

index before you can repartition the base table. To avoid this restriction, when you are creating

a spatial index, you can specify the "ON filegroup" option. For more information, see "Spatial

Indexes and Filegroups," later in this topic.

By default, spatial indexes are partitioned to the same filegroups as the table on which the

index is specified. This can be overridden by using the filegroup specification:

[ ON {

filegroup_name

| "default" } ]

If you specify a filegroup for a spatial index, the index is placed on that filegroup, regardless of

the partitioning scheme of the table.

The following catalog views are specific to spatial indexes:

sys.spatial_indexes

Represents the main index information of the spatial indexes.

sys.spatial_index_tessellations

Represents the information about the tessellation scheme and parameters of each of the

spatial indexes.

For more information about creating indexes, see the "Remarks" section in

CREATE INDEX

(Transact-SQL).
