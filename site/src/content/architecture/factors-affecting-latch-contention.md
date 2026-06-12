---
title: "Factors affecting latch contention"
topic: "io-fundamentals"
description: "later in this article."
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

later in this article. This performance improvement is directed at systems with high numbers of

cores and a high level of concurrency.

Latch contention that hinders performance in OLTP environments is typically caused by high

concurrency related to one or more of the following factors:

Latch contention can occur on any multi-core system. In SQLCAT experience

excessive latch contention, which impacts application performance beyond

acceptable levels, has most commonly been observed on systems with 16+ CPU

cores and might increase as more cores are made available.

Depth of B-tree, clustered and non-clustered index design, size and density of

rows per page, and access patterns (read/write/delete activity) are factors that can

contribute to excessive page latch contention.

Excessive page latch contention typically occurs in conjunction with a high level

of concurrent requests from the application tier. There are certain programming

practices that can also introduce a high number of requests for a specific page.

ﾉ

Expand table
