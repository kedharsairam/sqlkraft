---
title: "Set Subscription expiration period"
topic: "migration"
description: "This topic describes how to set the expiration period for subscriptions in SQL Server by using SQL Server Management Studi"
tags: ["migration","set-subscription-expiration-period"]
pubDate: 2025-12-01
---

This topic describes how to set the expiration period for subscriptions in SQL Server by using

Management Studio or Transact-SQL. The expiration period for subscriptions

determines the period of time before a subscription expires and is removed. For more

information, see

Subscription Expiration and Deactivation.

Recommendations

Management Studio

Transact-SQL

The subscription expiration period is also referred to as the

publication retention period.

Cleanup of merge replication metadata is dependent on this setting:

Replication cannot clean up metadata in the publication and subscription databases

until the retention period is reached. Use caution in specifying a high value for the

retention period, because it can negatively impact replication performance. It is

recommended that you use a lower setting if you can reliably predict that all

Subscribers will synchronize regularly within that time period.

The retention period for merge publications has a 24-hour grace period to

accommodate Subscribers in different time zones. If, for example, you set a retention

period of one day, the actual retention period is 48 hours.

It is possible to specify that subscriptions never expire, but it is strongly recommended

that you do not use this value, because metadata cannot be cleaned up.
