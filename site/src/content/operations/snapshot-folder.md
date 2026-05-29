---
title: "Snapshot folder"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  The snapshot folder is a directory that you have designated as a share; agents that read from
  
  and write to this folder must have enough permissions to access it.
  
  B
tags:
  - "linux-operations"
  - "snapshot-folder"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

The snapshot folder is a directory that you have designated as a share; agents that read from

and write to this folder must have enough permissions to access it.

Before the examples, let's walk through how SQL Server uses samba shares in replication.

Following is a basic example of how this works.

1. Samba shares are configured that files written to

by the replication agents

on publisher can be seen by the subscriber

2. SQL Server is configured to use share paths when setting up the publisher on the

distribution server such that all instances would look at the

3. SQL Server finds the local path from the

to know where to look for the files

4. SQL Server reads/writes to local paths backed by a samba share

Replication agents will need a shared directory between replication hosts to access snapshot

folders on other machines. For example, in transactional pull replication, the distribution agent

resides on the subscriber, which requires access to the distributor to get articles. In this section,

we'll go through an example of how to configure a samba share on two replication hosts.



```cmd
/local/path1
//share/path
//share/path
```