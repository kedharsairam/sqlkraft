---
title: "Cache considerations and SQLIOSim"
topic: "io-fundamentals"
description: "Listen closely to your hardware manufacturer's guidance."
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Listen closely to your hardware manufacturer's guidance.

To use a drive with SQL Server, disable drive caching. By default, the drive cache is enabled. In

Windows Server, use the

>

>

tab to disable write caching at the

OS level.

Don't rely on OS-level settings alone. Some drives ignore Windows settings and require

manufacturer-provided utilities or firmware settings to disable write caching. Confirm through

vendor tools that write caching is actually disabled.

To confirm transactional durability guarantees, validate your I/O subsystem by using

SQLIOSim

before moving to production. This utility simulates heavy asynchronous read and write activity to

a simulated data device and log device. For more information, see

Use the SQLIOSim utility to

simulate SQL Server activity on a disk subsystem. For broader storage benchmarking, you can

also use the

storage testing tool.

Many PC manufacturers order the drives with the write cache disabled. However, testing shows

that this condition might not always be the case, so you should always test it completely. If you

have any questions about the caching status of your storage device, contact the manufacturer

and obtain the appropriate utility to disable write-caching operations. On older storage media,

you might also need jumper settings.

requires systems to support

guaranteed delivery to stable media

, as outlined under the

I/O Reliability Program Requirements.

７

Note

Even with write caching disabled, drive firmware might introduce internal optimizations that

delay flush commands. Always confirm the effective cache state before deployment by using

testing tools such as

SQLIOSim.

７

Note

Ensure that any alternate caching mechanism can properly handle multiple types of failure.
