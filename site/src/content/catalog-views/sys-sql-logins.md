---
name: "sys.sql_logins"
title: "sys.sql_logins"
category: "security"
description: "Analytics Platform System (PDW) Returns one row for every SQL Server authentication login. Password expiration is checked. Hash of SQL login password. In SQL Server 2022 (16.x) and earlier versions, the stored password information is calculated using SHA-512 of the salted password. Starting with SQL Server 2025 (17.x), an iterated hash algorithm, RFC2898 (PBKDF), is used."
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.server_principals"
---

## Description

Analytics Platform System (PDW) Returns one row for every SQL Server authentication login. Password expiration is checked. Hash of SQL login password. In SQL Server 2022 (16.x) and earlier versions, the stored password information is calculated using SHA-512 of the salted password. Starting with SQL Server 2025 (17.x), an iterated hash algorithm, RFC2898 (PBKDF), is used. The first byte of the hash indicates the

## Syntax

`sys.server_principals`

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Analytics Platform System (PDW) Returns one row for every SQL Server authentication login. Description N/A Inherits from . Password policy is checked. Password expiration is checked. Hash of SQL login password. In SQL Server 2022 (16.x) and earlier versions, the stored password information is calculated using SHA-512 of the salted password. Starting with SQL Server 2025 (17.x), an iterated hash algorithm, RFC2898 (PBKDF), is used. The first byte of the hash indicates the version: for version 2 (SQL Server 2022 (16.x) and earlier versions) and for version 3 (SQL Server 2025 (17.x) and later versions). For a list of columns that this view inherits, see sys.server_principals . The columns and isn't inherited from sys.server_principals. To view both SQL Server authentication logins and Windows authentication logins, see sys.server_principals . When contained database users are enabled, connections can be made without logins. To identify those accounts, see sys.database_principals . In SQL Server, any SQL Server authentication login can see their own login name, and the login. To see other logins, the principal requires , , or a permission on the login. ﾉ Expand table
