---
name: "sys.spatial_indexes"
title: "sys.spatial_indexes"
category: "indexes"
description: "Represents the main index information of the spatial indexes."
tags: ["indexes","catalog-view"]
pubDate: "2026-05-29"
---

## Description

Represents the main index information of the spatial indexes. Type description of spatial index: GEOMETRY = geometric spatial index GEOGRAPHY = geographic spatial index GEOMETRY_GRID, GEOMETRY_AUTO_GRID, GEOGRAPHY_GRID, GEOGRAPHY_AUTO_GRID Note: For information about tessellation schemes, see The inherited columns has_filter and filter_definition appear after the columns that are specific to spatial indexes.

## Permissions

Article • 02/28/2023 Description <inherited columns> Inherits columns from sys.indexes. spatial_index_type Type of spatial index: 1 = Geometric spatial index 2 = Geographic spatial index spatial_index_type_desc Type description of spatial index: GEOMETRY = geometric spatial index GEOGRAPHY = geographic spatial index tessellation_scheme Name of tessellation scheme: GEOMETRY_GRID, GEOMETRY_AUTO_GRID, GEOGRAPHY_GRID, GEOGRAPHY_AUTO_GRID Note: For information about tessellation schemes, see Spatial Indexes Overview. <inherited columns> Inherits columns from sys.indexes. The inherited columns has_filter and filter_definition appear after the columns that are specific to spatial indexes. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. ﾉ Expand table See Also
