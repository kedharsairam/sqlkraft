---
title: "Cluster DTC"
topic: "high-availability"
description: "on Windows This topic describes the requirements and steps for clustering the Microsoft Distributed Transaction Coordinator (DTC) service for Always On availability groups."
tags: ["high-availability","cluster-dtc"]
pubDate: "2025-12-01"
---

on Windows

This topic describes the requirements and steps for clustering the Microsoft Distributed

Transaction Coordinator (DTC) service for Always On availability groups. For additional

information regarding distributed transactions and Always On availability groups, see

Cross-

Database Transactions and Distributed Transactions for Always On Availability Groups and

Database Mirroring (SQL Server).

Ensure all nodes, services and the

Availability Group have been configured

correctly.

Prerequisites, Restrictions, and Recommendations for Always

On Availability Groups (SQL Server)

Ensure Availability Group DTC

requirements have been met.

Cross-Database Transactions and Distributed Transactions for

Always On Availability Groups and Database Mirroring (SQL

Server)

A shared-storage drive.

Configuring the Shared-Storage

Drive. Consider using drive

letter.

A unique DTC Network Name resource. The name will be registered as a

cluster computer object in Active Directory.

Make sure that either of the following is true:

• The user who creates the DTC Network Name resource has the Create

Computer objects permission to the OU or the container where the DTC

Prestage Cluster Computer

Objects in Active Directory

Domain Services

ﾉ

Expand table

ﾉ

Expand table
