---
title: "srv_alloc"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Allocates memory dynamically.

  size

  Specifies the number of bytes to allocate.

  A pointer to the newly allocated space. If

  size

  bytes cannot be allo
tags:
  - "clr-integration"
  - "srv-alloc"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Allocates memory dynamically.

size

Specifies the number of bytes to allocate.

A pointer to the newly allocated space. If

size

bytes cannot be allocated, a null pointer is

returned.

The

function is equivalent to the Microsoft Windows API

function.

Normal Windows API C run-time memory management functions can be used in an Extended

Stored Procedure API application.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

）

Important

```sql
void * srv_alloc ( DBINT
size
);
```
