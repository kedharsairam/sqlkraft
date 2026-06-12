---
title: "Monitor"
topic: "high-availability"
description: "After you have configured log shipping, you can monitor information about the status of all the log shipping servers."
tags: ["high-availability","monitor-2"]
pubDate: "2025-12-01"
---

After you have configured log shipping, you can monitor information about the status of all

the log shipping servers. The history and status of log shipping operations are always saved

locally by the log shipping jobs. The history and status of the backup operation are stored at

the primary server, and the history and status of the copy and restore operations are stored at

the secondary server. If you have implemented a remote monitor server, this information is also

stored on the monitor server.

You can configure alerts that will fire if log shipping operations fail to occur as scheduled.

Errors are raised by an alert job that watches the status of the backup and restore operations.

You can define alerts that notify an operator when these errors are raised. If a monitor server is

configured, one alert job runs on the monitor server that raises errors for all operations in the

log shipping configuration. If a monitor server is not specified, an alert job runs on the primary

server instance, which monitors the backup operation. If a monitor server is not specified, an

alert job also runs on each secondary server instance to monitor the local copy and restore

operations.

The monitoring history tables contain metadata that is stored on the monitor server. A copy of

information specific to a given primary or secondary server is also stored locally.

You can query these tables to monitor the status of a log shipping session. For example, to

learn status of log shipping, check the status and history of the backup job, copy job, and

restore job. You can view specific log shipping history and error details by querying the

following monitoring tables.

）

Important

To monitor a log shipping configuration, you must add the monitor server when you

enable log shipping. If you add a monitor server later, you must remove the log shipping

configuration and then replace it with a new configuration that includes a monitor server.

For more information, see. Furthermore, after the

monitor server has been configured, it cannot be changed without removing log shipping

first.
