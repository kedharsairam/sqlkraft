---
title: "Log Shipping"
topic: "high-availability"
description: "A given database can be mirrored or log shipped; it can also be simultaneously mirrored and log shipped."
tags: ["high-availability","log-shipping"]
pubDate: 2025-12-01
---

A given database can be mirrored or log shipped; it can also be simultaneously mirrored and

log shipped. To choose what approach to use, consider the following:

How many destination servers do you require?

If you require only a single destination database, database mirroring is the recommended

solution.

If you require more than one destination database, you need to use log shipping, either

alone or with database mirroring. Combining these approaches gives you the benefits of

database mirroring along with the support for multiple destinations provided by log

shipping.

If you need to delay restoring log on the destination database (typically, to protect

against logical errors), use log shipping, alone or with database mirroring.

This topic discusses considerations for combining log shipping and database mirroring.

The principal database in a mirroring session can also act as the primary database in a log

shipping configuration, or vice versa, as the log shipping backup share is intact. The database

mirroring session run in any operating mode, whether synchronous (with transaction safety set

to FULL) or asynchronous (with transaction safety set to OFF).

７

Note

For introductions to these technologies, see

and.

７

Note

To use database mirroring on a database, the full recovery model is always required.
