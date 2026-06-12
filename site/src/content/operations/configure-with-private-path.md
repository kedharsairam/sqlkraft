---
title: "Configure with private path"
topic: "azure-synapse"
description: |
  SQL Server enabled by Azure Arc

  07/03/2025

  This article describes how to configure communication for a SQL Server enabled by Azure Arc

  instance so that it connects to Azure without going over inter
tags:
  - "azure-synapse"
  - "configure-with-private-path"
pubDate: 2025-12-01
---

enabled by Azure Arc

07/03/2025

This article describes how to configure communication for a SQL Server enabled by Azure Arc

instance so that it connects to Azure without going over internet paths.

This design deploys forward proxy servers in Azure to allow SQL Server to communicate over a

site-to-site VPN or ExpressRouteConnection with private IP addresses. The proxies

communicate with Arc URLs over the Azure backbone network.

The following diagram represents this pattern.

）

Important

This implementation uses

- which is currently available in

preview.
