---
title: "Prerequisites, Restrictions, & Recommendations"
topic: "high-availability"
description: "Prerequisites, Restrictions, and This topic describes the prerequisites and recommendations for setting up database mirroring."
tags: ["high-availability","prerequisites-restrictions-recommendations-2"]
pubDate: 2025-12-01
---

Prerequisites, Restrictions, and

This topic describes the prerequisites and recommendations for setting up database mirroring.

For an introduction to database mirroring, see

Database Mirroring (SQL Server).

For a list of features supported by the editions of SQL Server on Windows, see:

Editions and supported features of SQL Server 2025 Preview

Editions and supported features of SQL Server 2022

Editions and supported features of SQL Server 2019

Editions and supported features of SQL Server 2017

Editions and supported features of SQL Server 2016

Note that database mirroring works with any supported database compatibility level. For

information about the supported compatibility levels, see

ALTER DATABASE Compatibility Level

(Transact-SQL).

For a mirroring session to be established, the partners and the witness, if any, must be

running on the same version of SQL Server.

The two partners, that is the principal server and mirror server, must be running the same

edition of SQL Server. The witness, if any, can run on any edition of SQL Server that

supports database mirroring.

７

Note

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Always On availability groups instead.

Database Mirroring in SQL Server is a distinct technology from.
