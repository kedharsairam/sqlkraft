---
name: "sys.dm_os_child_instances"
title: "sys.dm_os_child_instances"
category: "os"
description: "Analytics Platform System (PDW) Returns a row for each user instance that has been created from the parent server instance."
tags: ["os", "dmv"]
pubDate: 2026-05-29
---

## Description

Analytics Platform System (PDW) Returns a row for each user instance that has been created from the parent server instance. can be used to determine the state of each User Instance (heart_beat) and to obtain the pipe name (instance_pipe_name) that can be used to create a connection to the User Instance using SQL Server Management Studio or SQLCmd. You can only connect to a User Instance after it has been started by an external
