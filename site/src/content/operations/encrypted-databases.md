---
title: "Encrypted databases"
topic: "high-availability"
description: |
  Article
  
  •
  
  01/19/2024
  
  Applies to:
  
  SQL Server
  
  This article contains information about the using currently encrypted or recently decrypted
  
  databases with Always On availability groups in SQL Server
tags:
  - "high-availability"
  - "encrypted-databases"
pubDate: 2025-12-01
---

Article

•

01/19/2024

Applies to:

SQL Server

This article contains information about the using currently encrypted or recently decrypted

databases with Always On availability groups in SQL Server.

If a database is encrypted or even contains a database encryption key (DEK), you can't use the

New Availability Group Wizard or Add Database to Availability Group Wizard to add the

database to an availability group. Even if an encrypted database has been decrypted, its log

backups might contain encrypted data. In this case, full initial data synchronization could fail on

the database. This is because the restore log operation might require the certificate that was

used by the database encryption keys (DEKs), and that certificate might be unavailable.

To make a decrypted database eligible to add to an availability group using the wizard:

1. Create a full database backup of the primary database.

2. Create a log backup of the primary database.

3. Restore the database backup on the server instance that hosts the secondary replica.

4. Restore the log backup on the secondary database.

Prepare a secondary database for an Always On availability group

Use the Availability Group Wizard (SQL Server Management Studio)

Add a database to an Always On availability group with the 'Availability Group Wizard'

What is an Always On availability group?

Transparent data encryption (TDE)