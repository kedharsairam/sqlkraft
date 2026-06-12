---
title: "Implicit transactions and avoiding concurrency and resource problems"
topic: "io-fundamentals"
description: "Don't open a transaction while browsing through data, if at all possible. Transactions"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Don't open a transaction while browsing through data, if at all possible. Transactions

shouldn't be started until all preliminary data analysis has been completed.

Keep the transaction as short as possible. After you know the modifications that have to be

made, start a transaction, execute the modification statements, and then immediately

commit or roll back. Don't open the transaction before it's required.

To reduce blocking, consider using a row versioning-based isolation level for read-only

queries.

Make intelligent use of lower transaction isolation levels. Many applications can be coded to

use the

transaction isolation level. Few transactions require the

transaction isolation level.

Make intelligent use of optimistic concurrency options. In a system with a low probability of

concurrent updates, the overhead of dealing with an occasional "somebody else changed

your data after you read it" error can be much lower than the overhead of always locking

rows as they're read.

Access the least amount of data possible while in a transaction. This lessens the number of

locked rows, thereby reducing contention between transactions.

Avoid pessimistic locking hints such as

whenever possible. Hints like

or

isolation level can cause processes to wait even on shared locks and reduce

concurrency.

Avoid using implicit transactions when possible. Implicit transactions can introduce

unpredictable behavior due to their nature. See

Implicit Transactions and concurrency

problems.

To prevent concurrency and resource problems, manage implicit transactions carefully. When

using implicit transactions, the next Transact-SQL statement after

or

automatically starts a new transaction. This can cause a new transaction to be opened while the

application browses through data, or even when it requires input from the user. After completing

the last transaction required to protect data modifications, turn off implicit transactions until a

transaction is once again required to protect data modifications. This process lets the Database

Engine use autocommit mode while the application is browsing data and getting input from the

user.

```sql
READ COMMITTED
```

`SERIALIZABLE`

`HOLDLOCK`

`HOLDLOCK`

`SERIALIZABLE`

`COMMIT`

`ROLLBACK`
