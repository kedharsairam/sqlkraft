---
title: "Force service to fail over"
topic: "high-availability"
description: ""
tags: ["high-availability","force-service-to-fail-over"]
pubDate: 2025-12-01
---

In high-performance mode and high-safety mode without automatic failover, if the principal

server fails while the mirror server is available, the database owner can make the database

available by forcing service to fail over (with possible data loss) to the mirror database. This

option is available only under all the following conditions:

The principal server is down.

WITNESS is set to OFF or is connected to the mirror server.

Forcing service suspends the session and starts a new recovery fork. The effect of forcing

service is similar to removing mirroring and recovering the former principal database. However,

forcing service facilitates resynchronizing the databases (with possible data loss) when

mirroring resumes.

1. Connect to the mirror server.

2. Issue the following statement:

ALTER DATABASE

<database_name>

SET PARTNER FORCE_SERVICE_ALLOW_DATA_LOSS

where

<database_name>

is the mirrored database.

The mirror server immediately transitions to principal server, and mirroring is suspended.

Ｕ

Caution

Forced service is strictly a disaster recovery method. Forcing service may involve some

data loss. Therefore, force service only if you are willing to risk losing some data in order

to restore service to the database immediately. If forcing service risks losing significant

data, we recommend that you stop mirroring and manually resynchronize the databases.

For more information about the risks of forcing service, see.
