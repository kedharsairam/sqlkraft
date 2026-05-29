---
title: "Witness"
topic: "high-availability"
description: |
  Article
  
  •
  
  12/14/2022
  
  Applies to:
  
  SQL Server
  
  To support automatic failover, a database mirroring session must be configured in high-safety
  
  mode and also possess a third server instance, known as 
tags:
  - "high-availability"
  - "witness"
pubDate: 2025-12-01
---

Article

•

12/14/2022

Applies to:

SQL Server

To support automatic failover, a database mirroring session must be configured in high-safety

mode and also possess a third server instance, known as the

witness

. The witness is an optional

instance of SQL Server that enables the mirror server in a high-safety mode session to

recognize whether to initiate an automatic failover. Unlike the two partners, the witness does

not serve the database. Supporting automatic failover is the only role of the witness.

The following illustration shows a high-safety mode session with a witness.

Using a Witness in Multiple Sessions

７

Note

In high-performance mode, the witness can adversely affect availability. If a witness is

configured for a database mirroring session, the principal server must be connected at

least to one of the other server instances, the mirror server or the witness, or both of

them. Otherwise, the database becomes unavailable and forcing service (with possible

data loss) is impossible. Therefore, for high-performance mode, we strongly recommend

that you always keep the witness set to OFF. For information about the impact of a witness

on high-performance mode, see

.