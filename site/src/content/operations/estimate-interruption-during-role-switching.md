---
title: "Estimate interruption during role switching"
topic: "high-availability"
description: ""
tags: ["high-availability","estimate-interruption-during-role-switching"]
pubDate: 2025-12-01
---

During a role switch, the amount of time that database mirroring will be out of service depends

on the type of role switching and the cause of the role switch.

For automatic failover, two factors contribute to the time service is interrupted: the time

required for the mirror server to recognize that the principal server instance has failed,

that is error detection, plus the time required to fail over the database, that is failover

time.

For a forced-service operation, though a failure has occurred, detecting and responding

to the failure depends on human responsiveness. However, estimating the potential

interruption of service is limited to estimating the time for the mirror server to switch

roles after the forced service command is issued.

For a manual failover, only the time required to fail over the database after the failover

command is issued.

The time for the system to notice an error depends on the type of error; for example, a network

error is noticed almost instantly, while noticing a server that is not responding takes 10

seconds (with the default timeout).

For information on errors that can cause a failure during a database mirroring session and

timeout detection in high-safety mode with automatic failover, see

Possible Failures During

Database Mirroring

).

７

Note

To reduce the time required to detect specific conditions such as some types of

errors, you can define alerts for those conditions.
