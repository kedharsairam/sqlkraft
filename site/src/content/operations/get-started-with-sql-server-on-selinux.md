---
title: "Get started with SQL Server on SELinux"
topic: "linux-operations"
description: |
  This article helps you get started with SQL Server as a
  
  confined service
  
  on a Security-Enhanced
  
  Linux (SELinux) distribution based on Red Hat Enterprise Linux (RHEL).
  
  Security-Enhanced Linux (SELi
tags:
  - "linux-operations"
  - "get-started-with-sql-server-on-selinux"
pubDate: 2025-12-01
---

This article helps you get started with SQL Server as a

confined service

on a Security-Enhanced

Linux (SELinux) distribution based on Red Hat Enterprise Linux (RHEL).

Security-Enhanced Linux (SELinux) is a security architecture for Linux systems. It helps define

access controls for applications, processes, and files on a system. SELinux uses a set of rules, or

security policies

, to define what can or can't be accessed. SELinux provides administrators more

control over who can access the system. For more information, see

What is SELinux (Security-

Enhanced Linux)

.

For details about how to enable SELinux for Red Hat systems, see

SELinux Architecture

. You can

also get started with an

SELinux-enabled operating system

for free.

SQL Server 2022 on Linux

is officially certified with RHEL 9 (as of July 2024), and is now generally

available on the

Red Hat Ecosystem Catalog

.

A

confined service

with SELinux means that it's restricted by security rules, explicitly defined in the

SELinux policy. For SQL Server, the SELinux custom policies are defined in the

package.

1. Enable SELinux and set it to

mode. Check the SELinux status by running the

command.

Here's the expected output.

SQL Server and SELinux

```cmd
mssql-server-
selinux
enforcing
sestatus
sestatus
```