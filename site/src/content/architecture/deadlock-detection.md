---
title: "Deadlock detection"
topic: "locking"
description: "However, when separate transactions hold partition locks in a table and want a lock"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

However, when separate transactions hold partition locks in a table and want a lock

somewhere on the other transactions partition, this causes a deadlock. This type of deadlock

can be avoided by setting

to

. However, this setting reduces

concurrency by forcing large updates to a partition to wait for a table lock.

All of the resources listed in the

Resources that can deadlock

section participate in the

Database Engine deadlock detection scheme. Deadlock detection is performed by a lock

monitor thread that periodically initiates a search through all of the tasks in an instance of the

Database Engine. The following points describe the search process:

The default interval is 5 seconds.

If the lock monitor thread finds deadlocks, the deadlock detection interval drops from 5

seconds to as low as 100 milliseconds depending on the frequency of deadlocks.

If the lock monitor thread stops finding deadlocks, the Database Engine increases the

intervals between searches to 5 seconds.

If a deadlock is detected, it's assumed that the new threads that must wait for a lock are

entering the deadlock cycle. The first few lock waits after a deadlock is detected

immediately trigger a deadlock search, rather than wait for the next deadlock detection

interval. For example, if the current interval is 5 seconds, and a deadlock was just

detected, the next lock wait kicks off the deadlock detector immediately. If this lock wait

is part of a deadlock, it's detected right away, rather than during the next deadlock

search.

The Database Engine typically performs periodic deadlock detection only. Because the number

of deadlocks encountered in the system is usually small, periodic deadlock detection helps

reduce the overhead of deadlock detection in the system.

When the lock monitor initiates deadlock search for a particular thread, it identifies the

resource on which the thread is waiting. The lock monitor then finds the owners for that

particular resource and recursively continues the deadlock search for those threads until it finds

a cycle. A cycle identified in this manner forms a deadlock.

After a deadlock is detected, the Database Engine ends a deadlock by choosing one of the

threads as a deadlock victim. The Database Engine terminates the current batch being

executed for the thread, rolls back the transaction of the deadlock victim, and returns error

1205 to the application. Rolling back the transaction for the deadlock victim releases all locks

held by the transaction. This allows the transactions of the other threads to become unblocked

`LOCK_ESCALATION`

`TABLE`
