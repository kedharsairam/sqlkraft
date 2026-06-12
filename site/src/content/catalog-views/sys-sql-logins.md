---
name: "sys.sql_logins"
title: "sys.sql_logins"
category: "security"
description: "Returns one row for every SQL Server authentication login. Password expiration is checked. Hash of SQL login password. In SQL Server 2022 (16.x) and earlier versions, the stored password information is calculated using SHA-512 of the salted password. Starting with SQL Server 2025 (17.x), an iterated hash algorithm, RFC2898 (PBKDF), is used."
tags: ["security","catalog-view"]
pubDate: "2026-05-29"
syntax: "sys.server_principals"
---

## Description

Analytics Platform System (PDW) Returns one row for every SQL Server authentication login. Password expiration is checked. Hash of SQL login password. In SQL Server 2022 (16.x) and earlier versions, the stored password information is calculated using SHA-512 of the salted password. Starting with SQL Server 2025 (17.x), an iterated hash algorithm, RFC2898 (PBKDF), is used.

## Syntax

`sys.server_principals`

## Permissions
