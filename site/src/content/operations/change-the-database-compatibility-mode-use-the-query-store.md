---
title: "Change the database compatibility mode & use the Query Store"
topic: "upgrade"
description: "06/04/2025 - Windows only In SQL Server 2016 (13.x) and later, some changes are only enabled once the database compatibility level has been changed."
tags: ["upgrade","change-the-database-compatibility-mode-use-the-query-store"]
pubDate: 2025-12-01
---

- Windows only

In SQL Server 2016 (13.x) and later, some changes are only enabled once the

database

compatibility level

has been changed. This was done for several reasons:

Since upgrade is a one-way operation (it isn't possible to downgrade the file format),

there's value in separating the enablement of new features to a separate operation within

the database. It's possible to revert a setting to a prior database compatibility level. The

new model reduces the number of things that must happen during an outage window.

Changes to the query processor can have complex effects. Even though a "good" change

to the system might be great for most workloads, it could cause an unacceptable

regression on an important query for others. Separating this logic from the upgrade

process allows for features, such as the Query Store, to mitigate plan choice regressions

quickly or even avoid them completely in production servers.

The following behaviors are expected for SQL Server 2017 (14.x) when a database is attached

or restored, and after an in-place upgrade:

If the compatibility level of a user database was 100 or higher before the upgrade, it

remains the same after upgrade.

If the compatibility level of a user database was 90 before upgrade, in the upgraded

database, the compatibility level is set to 100, which is the lowest supported compatibility

level in SQL Server 2017 (14.x).

The compatibility levels of the

,

,

, and

databases are set to

the current compatibility level after upgrade.

The

system database retains the compatibility level it had before upgrade.

The upgrade process to enable new query processor functionality is related to the post-release

servicing model of the product. Some of those fixes are released under

Trace Flag 4199.

Customers needing fixes can opt in to those fixes without causing unexpected regressions for

other customers. The post-release servicing model for query processor hotfixes is documented

here. Beginning with SQL Server 2016 (13.x), moving to a new compatibility level implies that

Trace Flag 4199 is no longer needed, because those fixes are now enabled by default in the

latest compatibility level. Therefore, as part of the upgrade process, it's important to validate

that 4199 isn't enabled once the upgrade process completes.

```cmd
tempdb model msdb
Resource master
```
