---
name: "Key benefits of float16 support"
title: "Key benefits of float16 support"
category: "statements"
description: "SQL Server 2025 (17.x)"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2025 (17.x)

Beginning with SQL Server 2025 (17.x), you can specify the underlying base type for the

data type. By default,

uses

as its base type.

(half-precision) is an

alternate type for scenarios where reduced precision is acceptable. It offers a more compact

alternative by reducing storage and improving performance.

A half-precision floating point vector is an array or collection of numbers, where each number

is represented using a 16-bit half-precision (

) floating-point format. This representation

consumes half the memory of a standard 32-bit single-precision float. Use these vector types

to save memory and bandwidth, especially in deep learning and vector databases, by trading

off some precision for efficiency.

While

offers significant storage and performance advantages, it provides reduced

numerical precision compared to

. This tradeoff makes it well-suited for approximate

similarity scenarios, such as semantic search, but less appropriate for workloads that require

high-precision arithmetic or exact numerical fidelity.

SQL Server supports vectors with up to

(

) when using

. This feature doubles the limitation 1,998 dimensions for

. This capability

enables more expressive embeddings and compatibility with larger models, for example

.

Storing vectors in a 16-bit format significantly decreases the amount of storage required

compared to full-precision vectors. This makes it feasible to store and query high-

dimensional vectors at scale. This optimization also improves data density, which can

enhance query performance in vector search scenarios.

Choose the most appropriate base type:

for compact Storage

for general use and higher precision tasks

### vector

### varchar(max)

### vector

### half-precision

`float32`

`float16`

`float16`

`float16`

`float32`

```sql
1998 × 2
```

`float16`

`float32`

```sql
text-embedding-large
```

`float16`

`float32`
