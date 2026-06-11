---
name: "sys.database_mirroring_witnesses"
title: "Database Mirroring Witness - sys.database_mirroring_witnesses"
category: "compatibility"
description: "Contains a row for every witness role that a server plays in a database mirroring partnership. In a database mirroring session, automatic failover requires a witness server. Ideally, the witness resides on a separate computer from both the principal and mirror servers. The witness does not serve the database. Instead, it monitors the status of the principal and mirror servers."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Contains a row for every witness role that a server plays in a database mirroring partnership. In a database mirroring session, automatic failover requires a witness server. Ideally, the witness resides on a separate computer from both the principal and mirror servers. The witness does not serve the database. Instead, it monitors the status of the principal and mirror servers. If the principal server fails, the witness may initiate automatic failover to the mirror server.
