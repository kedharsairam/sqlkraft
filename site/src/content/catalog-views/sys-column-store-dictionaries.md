---
name: 'sys.column_store_dictionaries'
title: 'sys.column_store_dictionaries'
category: 'compatibility'
description: 'SQL Server 2012 (11.x) and later Contains a row for each dictionary used in xVelocity memory optimized columnstore indexes. Dictionaries are used to encode some, but not all data types, therefore not all columns in a columnstore index have dictionaries. A dictionary can exist as a primary dictionary (for all segments) and possibly for other secondary dictionaries used for a subset of the column''s '
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

SQL Server 2012 (11.x) and later Contains a row for each dictionary used in xVelocity memory optimized columnstore indexes. Dictionaries are used to encode some, but not all data types, therefore not all columns in a columnstore index have dictionaries. A dictionary can exist as a primary dictionary (for all segments) and possibly for other secondary dictionaries used for a subset of the column's ID of the heap or B-tree index (HoBT) for the table that has this columnstore
