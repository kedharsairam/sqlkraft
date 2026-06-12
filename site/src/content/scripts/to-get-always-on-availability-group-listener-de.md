---
name: "To Get Always on Availability Group Listener De"
title: "To Get Always on Availability Group Listener De"
description: "diagnostic script for high-availability operations."
category: "high-availability"
tags: ["availability-group","high-availability"]
pubDate: "2025-03-15"
---

```sql
select @@servername, GL.dns_name as AG_ListenerName,GL.port as PortNo,
GL.ip_configuration_string_from_cluster as AG_IP_Addresses from sys.availability_group_listeners GL
```
