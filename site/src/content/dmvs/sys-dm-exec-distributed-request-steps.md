---
name: "sys.dm_exec_distributed_request_steps"
title: "sys.dm_exec_distributed_request_steps"
category: "execution"
description: "2016 (13.x) and later versions Holds information about all steps that compose a given PolyBase request or query. It lists one row per query step. sys.dm_exec_requests (Transact-SQL) 0 to (n-1) for a request with n steps. 'MoveOperation','OnOperation','RandomIDOperation','RemoteOperation','ReturnOperation','ShuffleMoveOperation', 'HadoopShuffleOperation', 'HadoopBroadCastOperation', 'Had"
tags: ["execution","dmv"]
pubDate: 2026-05-29
---

## Description

2016 (13.x) and later versions Holds information about all steps that compose a given PolyBase request or query. It lists one row per query step. sys.dm_exec_requests (Transact-SQL) 0 to (n-1) for a request with n steps. 'MoveOperation','OnOperation','RandomIDOperation','RemoteOperation','ReturnOperation','ShuffleMoveOperation', 'HadoopShuffleOperation', 'HadoopBroadCastOperation', 'HadoopRoundRobinOperation'
