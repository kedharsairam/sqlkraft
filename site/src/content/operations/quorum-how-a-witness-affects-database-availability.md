---
title: "Quorum: How a Witness Affects Database Availability"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Whenever a witness is set for a database mirroring session,

  quorum

  is required. Quorum is a

  relationship that exists when two or more server instanc
tags:
  - "high-availability"
  - "quorum-how-a-witness-affects-database-availability"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

Whenever a witness is set for a database mirroring session,

quorum

is required. Quorum is a

relationship that exists when two or more server instances in a database mirroring session are

connected to each other. Typically, quorum involves three interconnected server instances.

When a witness is set, quorum is required to make the database available. Designed for high-

safety mode with automatic failover, quorum makes sure that a database is owned by only one

partner at a time.

If a particular server instance becomes disconnected from a mirroring session, that instance

loses quorum. If no server instances are connected, the session loses quorum and the database

becomes unavailable. Three types of quorum are possible:

A

full quorum

includes both partners and the witness.

A

witness-to-partner quorum

consists of the witness and either partner.

A

partner-to-partner quorum

consists of the two partners.

The following figure shows these types of quorum.
