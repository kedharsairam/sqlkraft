---
title: "Partitioned attribute"
topic: "io-fundamentals"
description: "When an operator such as an Index Seek is executed on a partitioned table or index, the"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

When an operator such as an Index Seek is executed on a partitioned table or index, the

attribute appears in the compile-time and run-time plan, and is set to

(1).

The attribute doesn't display when it is set to

(0).

The

attribute can appear in the following physical and logical operators:

Table Scan

Index Scan

Index Seek

Insert

```sql
Partitioned
```

```sql
True
```

```sql
False
```

```sql
Partitioned
```
