---
title: "Disk I/O"
topic: "io-fundamentals"
description: "I/O fundamentals"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

I/O fundamentals

on Azure Virtual

Machines

The primary purpose of a SQL Server database is to store and retrieve data, so intensive disk

input/output (I/O) is a core characteristic of the Database Engine. Because disk I/O operations

can consume many resources and take a relatively long time to finish, SQL Server focuses on

making I/O highly efficient.

Storage subsystems for SQL Server are available in multiple form factors, including mechanical

drives and solid-state storage. This article provides details on how to use drive caching principles

to improve Database Engine I/O.

requires that systems support

guaranteed delivery to stable media

as outlined under

the

I/O Reliability Program Requirements.

This requirement includes, but isn't limited to, the following conditions:

Windows Hardware Compatibility Program

Write ordering

Caching stability

No data rewrites

Systems that meet these requirements support SQL Server database storage. Systems don't have

to be listed on SQL Server storage solutions programs, but they must guarantee that the

requirements are met.

The buffer manager only performs reads and writes to the database. Other file and database

operations, such as open, close, extend, and shrink, are handled by the database manager and file

manager components.

Disk I/O operations by the buffer manager have the following characteristics:

I/O is typically performed asynchronously, which allows the calling thread to continue

processing while the I/O operation takes place in the background. Under some

circumstances, such as misaligned log I/O, synchronous I/Os can occur.
