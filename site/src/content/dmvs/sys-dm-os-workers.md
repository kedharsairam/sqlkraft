---
name: "sys.dm_os_workers"
title: "sys.dm_os_workers"
category: "os"
description: "Returns a row for every worker in the system. For more information about workers, see the Thread and Task Architecture Guide 1 = Worker is running with preemptive scheduling. Any worker that is running external code is run 1 = Worker is running with lightweight pooling. For 1 = Worker is stuck trying to obtain a spin lock. If this bit is set, this might indicate a p"
tags: ["os","dmv"]
pubDate: "2026-05-29"
syntax: "Azure Active Directory admin"
---

## Description

Analytics Platform System (PDW) Returns a row for every worker in the system. For more information about workers, see the Thread and Task Architecture Guide 1 = Worker is running with preemptive scheduling. Any worker that is running external code is run 1 = Worker is running with lightweight pooling. For 1 = Worker is stuck trying to obtain a spin lock.

## Syntax

```sql
Azure Active Directory admin
```

## Examples

### Example 1

```sql
VIEW SERVER STATE
```

### Example 2

```sql
VIEW DATABASE STATE
```

### Example 3

```sql
Server Admin
```

### Example 4

```sql
Azure Active Directory admin
```
