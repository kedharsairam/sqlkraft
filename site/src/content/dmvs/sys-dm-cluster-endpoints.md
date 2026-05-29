---
name: "sys.dm_cluster_endpoints"
title: "sys.dm_cluster_endpoints"
category: "execution"
description: "Name of the service exposed externally in a SQL big data cluster. Unique identifier for the endpoint. Key for this view. Is not nullable. Description of the service. Is not nullable. Endpoint url or connection attribute. Is not nullable. Description of the endpoint protocol Requires VIEW SERVER SECURITY STATE permission on the server. What are SQL Server Big Data Clusters"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
---

## Description

Name of the service exposed externally in a SQL big data cluster. Unique identifier for the endpoint. Key for this view. Is not nullable. Description of the service. Is not nullable. Endpoint url or connection attribute. Is not nullable. Description of the endpoint protocol Requires VIEW SERVER SECURITY STATE permission on the server. What are SQL Server Big Data Clusters

## Code Blocks

```sql
sysname
```

```sql
nvarchar(4000)
```

```sql
VIEW SERVER STATE
```
