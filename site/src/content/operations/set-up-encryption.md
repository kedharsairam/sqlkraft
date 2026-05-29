---
title: "Set up encryption"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  To enable automatic decryption of the database master key of a mirror database, you must

  provide the password used to encrypt the master key to the mi
tags:
  - "high-availability"
  - "set-up-encryption"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

To enable automatic decryption of the database master key of a mirror database, you must

provide the password used to encrypt the master key to the mirror server instance. SQL Server

2005 (9.x) and later versions include mechanisms to transfer the password. Use

to create a credential for the database master key before

you start database mirroring. You must repeat this process for every database that will be

mirrored. For more information, see

sp_control_dbmasterkey_password (Transact-SQL)

.

sp_control_dbmasterkey_password (Transact-SQL)

CREATE MASTER KEY (Transact-SQL)

ALTER MASTER KEY (Transact-SQL)

Encryption Hierarchy

Setting Up Database Mirroring (SQL Server)

Ｕ

Caution

Do not enable failover decryption of a database that must remain inaccessible to

and

other highly privileged server principals. You can configure a database so that its key

hierarchy cannot be decrypted by the service master key. This option is supported as a

defense-in-depth for databases that contain information that should not be accessible to

or other highly privileged server principals. Enabling failover decryption of such a

database removes this defense-in-depth, enabling

and other highly privileged server

principals to decrypt the database.
