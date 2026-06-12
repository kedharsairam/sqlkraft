---
name: "Changing the SQL Server Service Account"
title: "Changing the SQL Server Service Account"
category: "statements"
description: "Specifies the name of the new Windows service account."
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

NEW_ACCOUNT

Specifies the name of the new Windows service account.

NEW_PASSWORD

Specifies the password of the new Windows service account.

The service master key is automatically generated the first time it is needed to encrypt a linked

server password, credential, or database master key. The service master key is encrypted using

the local machine key or the Windows Data Protection API. This API uses a key that is derived

from the Windows credentials of the SQL Server service account.

2012 (11.x) uses the AES encryption algorithm to protect the service master key

(SMK) and the database master key (DMK). AES is a newer encryption algorithm than 3DES

used in earlier versions. After upgrading an instance of the Database Engine to SQL Server

2012 (11.x) the SMK and DMK should be regenerated in order to upgrade the master keys to

AES. For more information about regenerating the DMK, see

ALTER MASTER KEY (Transact-

SQL).

To change the SQL Server service account, use SQL Server Configuration Manager. To manage

a change of the service account, SQL Server stores a redundant copy of the service master key

protected by the machine account that has the necessary permissions granted to the SQL

Server service group. If the computer is rebuilt, the same domain user that was previously used

by the service account can recover the service master key. This does not work with local

２

Warning

This option is obsolete. Do not use. Use SQL Server Configuration Manager instead.

２

Warning

This option is obsolete. Do not use. Use SQL Server Configuration Manager instead.

２

Warning

This option is obsolete. Do not use. Use SQL Server Configuration Manager instead.
