---
title: "Join an Active Directory domain"
topic: "linux-operations"
description: "on Linux This article provides general guidance on how to join a SQL Server Linux host machine to an Active Directory domain."
tags: ["linux-operations","join-an-active-directory-domain"]
pubDate: "2025-12-01"
---

on Linux

This article provides general guidance on how to join a SQL Server Linux host machine to an

Active Directory domain. There are two methods: use a built-in SSSD package, or use third-

party Active Directory providers. Examples of third-party domain join products are

PowerBroker

Identity Services (PBIS)

,

One Identity

, and

Centrify.

This guide includes steps to check your Active Directory configuration. However, it isn't

intended to provide instructions on how to join a machine to a domain when using third-party

utilities.

Before you configure Active Directory authentication, you need to set up an Active Directory

domain controller, Windows, on your network. Then join your SQL Server on Linux host to an

Active Directory domain.

The sample steps described in this article are for guidance only and refer to Ubuntu 16.04, Red

Hat Enterprise Linux (RHEL) 7.x, and SUSE Linux Enterprise Server (SLES) 12 operating systems.

Actual steps might slightly differ in your environment depending on how your overall

environment is configured and operating system version. For example, Ubuntu 18.04 uses

while Red Hat Enterprise Linux (RHEL) 8.x uses

among other tools to manage

and configure network. You should engage your system and domain administrators for your

environment for specific tooling, configuration, customization, and any required

troubleshooting.

７

Note

For information on configuring Active Directory with newer versions of Ubuntu, RHEL, or

SLES, see.

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.
