---
name: "sys.sp_help_peerconflictdetection"
title: "sp_help_peerconflictdetection"
category: "general"
description: "Returns information about the conflict detection settings for a publication that is involved in a peer-to-peer transactional replication topology. Transact-SQL syntax conventions The name of the publication for which to return information. Specifies the amount of time, in seconds, after which the procedure times out while waiting for response from every node in the topology. read-only Subscriber i"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_help_peerconflictdetection"
---

## Description

Returns information about the conflict detection settings for a publication that is involved in a peer-to-peer transactional replication topology. Transact-SQL syntax conventions The name of the publication for which to return information. Specifies the amount of time, in seconds, after which the procedure times out while waiting for response from every node in the topology. read-only Subscriber in the topology, specifying a time-out value isn't valid. Read-only

## Syntax

`sp_help_peerconflictdetection`
