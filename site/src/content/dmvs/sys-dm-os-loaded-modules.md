---
name: "sys.dm_os_loaded_modules"
title: "sys.dm_os_loaded_modules"
category: "os"
description: "Returns a row for each module loaded into the server address space. Address of the module in the process. Version of the file. Appears in the following format: Version of the product. Appears in the following format: 1 = Module is a debug version of the loaded module. 1 = Module is a pre-release version of the loaded module."
tags: ["os","dmv"]
pubDate: "2026-05-29"
syntax: |
  sys.dm_os_function_symbolic_name
      sys.dm_os_memory_allocations
      sys.dm_os_sublatches
      sys.dm_os_worker_local_storage
---

## Description

Analytics Platform System (PDW) Returns a row for each module loaded into the server address space. Address of the module in the process. Version of the file. Appears in the following format: Version of the product. Appears in the following format: 1 = Module is a debug version of the loaded module. 1 = Module is a pre-release version of the loaded module. 1 = Module is a private build of the loaded module.

## Syntax

```sql
sys.dm_os_function_symbolic_name sys.dm_os_memory_allocations sys.dm_os_sublatches sys.dm_os_worker_local_storage
```
