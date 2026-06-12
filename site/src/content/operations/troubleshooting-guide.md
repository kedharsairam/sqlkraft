---
title: "Troubleshooting guide"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This article describes how to troubleshoot SQL Server running on Linux or in a Linux container.

  When troubleshooting SQL Server on Linux, remember to review the sup
tags:
  - "linux-operations"
  - "troubleshooting-guide"
pubDate: 2025-12-01
---

SQL Server

on Linux

This article describes how to troubleshoot SQL Server running on Linux or in a Linux container.

When troubleshooting SQL Server on Linux, remember to review the supported features and

known limitations:

Release notes for SQL Server 2025 on Linux

Release notes for SQL Server 2022 on Linux

Release notes for SQL Server 2019 on Linux

Release notes for SQL Server 2017 on Linux

For answers to frequently asked questions, see the

on Linux FAQ.

If you have difficulty connecting to your Linux SQL Server instance, there are a few things to

check.

If you're unable to connect locally using

, try using the IP address 127.0.0.1

instead. It's possible that

isn't properly mapped to this address.

Verify that the server name or IP address is reachable from your client machine.

To find the IP address of your Ubuntu machine, you can run the

command as in

the following example:

For Red Hat, you can use the

command as in the following example:



Tip

```cmd
localhost localhost ifconfig ip addr sudo ifconfig eth0 | grep
'inet addr'
sudo ip addr show eth0 | grep
"inet"
```
