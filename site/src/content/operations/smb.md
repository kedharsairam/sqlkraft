---
title: "SMB"
topic: "linux-operations"
description: |
  Article

  •

  01/21/2025

  Applies to:

  SQL Server

  - Linux

  This article explains how to configure SMB storage for a failover cluster instance (FCI) on Linux.

  In the non-Windows world, SMB is also refe
tags:
  - "linux-operations"
  - "smb"
pubDate: 2025-12-01
---

Article

•

01/21/2025

Applies to:

SQL Server

- Linux

This article explains how to configure SMB storage for a failover cluster instance (FCI) on Linux.

In the non-Windows world, SMB is also referred to as a Common Internet File System (CIFS)

share and implemented via Samba. In the Windows world, accessing an SMB share is done this

way:

. For Linux-based SQL Server installations, the SMB share must be

mounted as a folder.

Here are some tips and notes for successfully using SMB:

The SMB share can be on Windows, Linux, or even from an appliance as long as it's using

SMB 3.0 or later versions. For more information on Samba and SMB 3.0, see

SMB 3.0

to

see if your Samba implementation is compliant with SMB 3.0.

The SMB share should be highly available.

Security must be set properly on the SMB share. Below is an example from

, where

is the name of the share.

ini

1. Choose one of the servers that will participate in the FCI configuration. It doesn't matter

which one.

2. Get information about the

user.

Bash

Important source and server information

```cmd
\\SERVERNAME\SHARENAME
/etc/samba/smb.conf
SQLData mssql
[SQLData]
path
=/var/smb/SQLData read only = no browseable
=
yes guest ok = no writeable
=
yes valid users = SQLSambaUser
```
