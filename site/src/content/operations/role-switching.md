---
title: "Role Switching"
topic: "high-availability"
description: "Within the context of a database mirroring session, the principal and mirror roles are typically interchangeable in a process known as role switching"
tags: ["high-availability","role-switching"]
pubDate: 2025-12-01
---

Within the context of a database mirroring session, the principal and mirror roles are typically

interchangeable in a process known as

role switching. In role switching, the mirror server acts

as the

failover partner

for the principal server, taking over the principal role, recovering its copy

of the database and bringing it online as the new principal database. The former principal

server, when available, assumes the mirror role, and its database becomes the new mirror

database. Potentially, the roles can switch back and forth either in response to multiple failures

or for administrative purposes.

The following illustration shows mirroring partners,

and

, switching the

principal and mirror roles over a series of automatic or manual failovers.

７

Note

This topic assumes that you are familiar with the database mirroring operating modes. For

more information, see.

）

Important
