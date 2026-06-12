---
title: "Deliver a snapshot through FTP"
topic: "migration"
description: "This topic describes how to deliver a snapshot through FTP in SQL Server by using SQL Server Management Studio or Transact-SQL. By default, snapshots"
tags: ["migration","deliver-a-snapshot-through-ftp"]
pubDate: "2025-12-01"
---

This topic describes how to deliver a snapshot through FTP in SQL Server by using SQL Server

Management Studio or Transact-SQL.

By default, snapshots are stored in folders defined as Universal Naming Convention (UNC)

shares. Replication also allows you to specify a File Transfer Protocol (FTP) share instead of a

UNC share. To use FTP, you must configure an FTP server and then configure a publication and

one or more subscriptions to use FTP. For information about how to configure an FTP server,

see the Internet Information Services (IIS) documentation. If you specify FTP information for a

publication, subscriptions to that publication use FTP by default. FTP is only used with Web

synchronization when the computer that is running IIS is separated from the Distributor by a

firewall. In this case, FTP can be used to transfer the snapshot from the Distributor and the

computer that is running IIS. (The snapshot is always transferred to the Subscriber by using

HTTPS.)

The Snapshot Agent must have write permissions for the directory you specify, and the

Distribution Agent or Merge Agent must have read permissions. If pull subscriptions are

used, you must specify a shared directory as a universal naming convention (UNC) path,

such as \\ftpserver\home\snapshots. For more information, see

Secure the Snapshot

Folder.

To transfer snapshot files using File Transfer Protocol (FTP), you must first configure an

FTP server. For more information, see the Microsoft Internet Information Services (IIS)

）

Important

We recommend that you use Microsoft Windows Authentication and a UNC share rather

than an FTP share because FTP passwords must be stored, and the password is sent from

the Subscriber or the computer that is running IIS when it uses Web synchronization to

the FTP server in plain text. Additionally, because a single account controls access to the

snapshot share, it is not possible to ensure that a Subscriber to a filtered merge

publication only has access to the snapshot files from their data partition.
