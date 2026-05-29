---
title: "Specify a server network address"
topic: "high-availability"
description: |
  Article
  
  •
  
  02/01/2024
  
  Applies to:
  
  SQL Server
  
  Setting up a database mirroring session requires a server network address for each of the
  
  server instances. The server network address of a server ins
tags:
  - "high-availability"
  - "specify-a-server-network-address"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

Setting up a database mirroring session requires a server network address for each of the

server instances. The server network address of a server instance must unambiguously identify

the instance by providing a system address and the number of the port on which the instance

is listening.

Before you can specify a port in a server network address, the database mirroring endpoint

must exist on the server instance. For more information, see

Create a Database Mirroring

Endpoint for Windows Authentication (Transact-SQL)

.

The syntax for a server network address is of the form:

TCP

<system-address>

<port>

where

<system-address>

is a string that unambiguously identifies the destination computer

system. Typically, the server address is a system name (if the systems are in the same

domain), a fully qualified domain name, or an IP address:

If the systems are the same domain, you can use the name of the computer system; for

example,

.

To use an IP address, it must be unique in your environment. We recommend that you

use an IP address only if it is static. The IP address can be IP Version 4 (IPv4) or IP

Version 6 (IPv6). An IPv6 address must be enclosed within square brackets, for

example:

<IPv6_address>

.

To learn the IP address of a system, at the Windows command prompt, enter the

command.

The fully qualified domain name is guaranteed to work. This is a locally defined

address string that different forms in different places. Often, but not always, a fully

qualified domain name is a compound name that includes the computer name and a

series of period-separated domain segments of the form:

```cmd
SYSTEM46
```