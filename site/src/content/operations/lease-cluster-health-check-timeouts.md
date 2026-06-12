---
title: "Lease, cluster, & health check timeouts"
topic: "high-availability"
description: ""
tags: ["high-availability","lease-cluster-health-check-timeouts"]
pubDate: 2025-12-01
---

Differences in hardware, software, and cluster configurations as well as different application

requirements for uptime and performance require specific configuration for lease, cluster, and health

check timeout values. Certain applications and workloads require more aggressive monitoring to limit

downtime following hard failures. Others require more tolerance for transient network issues and waits

from high resource usage and are okay with slower failovers.

Multiple services on each node work to detect failures. The cluster service could detect quorum loss, the

resource DLL could detect an issue surfaced by Always On health detection, or manual failover might be

initiated directly on the primary instance. The cluster service, the resource host, and the SQL Server

instance synchronize with each other via RPC, shared memory, and T-SQL. In most scenarios, these

services successfully communicate, however this communication isn't perfectly reliable even between

services on the same machine. Furthermore, the availability group (AG) needs to be able to withstand

system wide events like network and disk failures, which might prevent communication or interrupt

functionality. With many failure cases and without fully dependable communication between services,

the AG depends on various failover detection mechanisms to detect and respond to failures

independently of each other so the cluster state is always consistent for all nodes.

Resource constraints such as high CPU, disk latency, or memory exhaustion can trigger an Always On

availability group lease timeout. When a lease timeout is reported in the cluster log, the most recent

performance monitor data for CPU utilization, memory utilization, and disk read and write latency are

reported in the Windows Failover Cluster Log along with the lease timeout.

Likewise, resource constraints can also trigger a health check timeout. Starting with SQL Server 2025

(17.x) Preview, the same performance monitor counters are now reported in the Windows Failover

Cluster Log when a health check timeout is detected, similar to the lease timeout diagnostic output.

The following is a sample of the improved Windows Failover Cluster Log output for a health check

timeout:

Output

2025 improved health check timeout

```cmd
[Verbose] 000035b8.00001a64::2024/04/18-23:56:35.536 ERR [RES] SQL Server Availability
Group: [hadrag] Failure detected, diagnostics heartbeat is lost
[Verbose] 000035b8.00001a64::2024/04/18-23:56:35.536 WARN [RES] SQL Server Availability
Group: [hadrag] AG health check failed, logging perf counter data collected so far
[Verbose] 000035b8.00001a64::2024/04/18-23:56:35.536 WARN [RES] SQL Server Availability
```
