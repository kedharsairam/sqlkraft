---
name: "sys.resource_governor_workload_groups"
title: "sys.resource_governor_workload_groups"
category: "compatibility"
description: "Returns the stored workload group configuration. Each row represents a workload group. Each workload group uses one resource pool. Unique ID of the workload group. Not nullable."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "request_max_memory_grant_percent"
---

## Description

Returns the stored workload group configuration. Each row represents a workload group. Each workload group uses one resource pool. Unique ID of the workload group. Not nullable. Name of the workload group. Not nullable. Is the relative importance of a request in this workload group. Importance is one of the Importance is relative to other workload groups in the same resource pool. Maximum memory grant for a single request, as

## Syntax

`request_max_memory_grant_percent`
