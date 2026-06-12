---
title: "Trade-offs when using hash partitioning"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

While hash partitioning can eliminate contention on inserts, there are several trade-offs to

consider when deciding whether or not to use this technique:

Select queries in most cases need to be modified to include the hash partition in the

predicate and lead to a query plan that provides no partition elimination when these

queries are issued. The following screenshot shows a bad plan with no partition

elimination after hash partitioning has been implemented.
