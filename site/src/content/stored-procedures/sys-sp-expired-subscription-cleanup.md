---
name: 'sys.sp_expired_subscription_cleanup'
title: 'sp_expired_subscription_cleanup'
category: 'general'
description: 'Checks the status of all the subscriptions of every publication and drops subscriptions that are expired. This stored procedure is executed at the Publisher on any database, or at the Distributor on the distribution database for a non-SQL Server Publisher. Transact-SQL syntax conventions The name of a non-SQL Server publisher. , with a default of shouldn''t specify this parameter for a SQL Server P'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_expired_subscription_cleanup'
---

## Description

Checks the status of all the subscriptions of every publication and drops subscriptions that are expired. This stored procedure is executed at the Publisher on any database, or at the Distributor on the distribution database for a non-SQL Server Publisher. Transact-SQL syntax conventions The name of a non-SQL Server publisher. , with a default of shouldn't specify this parameter for a SQL Server Publisher. is used in all types of replication. The Expired Subscription Clean Up job runs remove expired subscriptions from publication databases every 24 hours. If any of the subscriptions are out-of-date, that is, aren't synchronized with the Publisher within the retention period, the publication is declared expired, and the traces of the subscription are

## Syntax

```sql
sp_expired_subscription_cleanup
```

## Permissions

cleaned up at the Publisher. For more information, see Subscription Expiration and Deactivation . Only members of the fixed server role or fixed database role can execute . sp_mergesubscription_cleanup (Transact-SQL) sp_subscription_cleanup (Transact-SQL) System stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Checks the status of all the subscriptions of every publication and drops subscriptions that are

expired. This stored procedure is executed at the Publisher on any database, or at the

Distributor on the distribution database for a non-SQL Server Publisher.

Transact-SQL syntax conventions

The name of a non-SQL Server publisher.

, with a default of

shouldn't specify this parameter for a SQL Server Publisher.

(success) or

is used in all types of replication.

The Expired Subscription Clean Up job runs

to detect and

remove expired subscriptions from publication databases every 24 hours. If any of the

subscriptions are out-of-date, that is, aren't synchronized with the Publisher within the

retention period, the publication is declared expired, and the traces of the subscription are
