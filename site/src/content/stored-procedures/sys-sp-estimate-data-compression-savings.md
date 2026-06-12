---
name: "sys.sp_estimate_data_compression_savings"
title: "sp_estimate_data_compression_savings"
category: "general"
description: "Returns the current size of the requested object and estimates the object size for the requested compression state. Compression can be evaluated for whole tables or parts of tables. This includes heaps, clustered indexes, nonclustered indexes, columnstore indexes, indexed views, and table and index partitions."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sys.sp_estimate_data_compression_savings"
---

## Description

Returns the current size of the requested object and estimates the object size for the requested compression state. Compression can be evaluated for whole tables or parts of tables. This includes heaps, clustered indexes, nonclustered indexes, columnstore indexes, indexed views, and table and index partitions. The objects can be compressed by using row, page, columnstore, or columnstore archive compression. If the table, index, or partition is already

## Syntax

`sys.sp_estimate_data_compression_savings`
