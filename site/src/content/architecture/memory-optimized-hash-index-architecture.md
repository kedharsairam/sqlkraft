---
title: "Memory-optimized hash index architecture"
topic: "index-architecture"
description: "### Configure the hash index bucket"
tags: ["index-architecture","architecture"]
pubDate: 2026-05-29
---

## Configure the hash index bucket

## count

A hash index consists of an array of pointers, and each element of the array is called a hash

bucket.

Each bucket is 8 bytes, which are used to store the memory address of a link list of key

entries.

Each entry is a value for an index key, plus the address of its corresponding row in the

underlying memory-optimized table.

Each entry points to the next entry in a link list of entries, all chained to the current

bucket.

The number of buckets must be specified at index creation time:

The lower the ratio of buckets to table rows or to distinct values, the longer the average

bucket link list is.

Short link lists perform faster than long link lists.

The maximum number of buckets in hash indexes is 1,073,741,824.

The hash function is applied to the index key columns and the result of the function

determines what bucket that key falls into. Each bucket has a pointer to rows whose hashed

key values are mapped to that bucket.

The hashing function used for hash indexes has the following characteristics:

The Database Engine has one hash function that is used for all hash indexes.

The hash function is deterministic. The same input key value is always mapped to the

same bucket in the hash index.

Multiple index keys might be mapped to the same hash bucket.

The hash function is balanced, meaning that the distribution of index key values over

hash buckets typically follows a Poisson or bell curve distribution, not a flat linear

distribution.

Poisson distribution isn't an even distribution. Index key values aren't evenly distributed in

the hash buckets.

If two index keys are mapped to the same hash bucket, there's a

hash collision. A large

number of hash collisions can have a performance effect on read operations. A realistic

goal is for 30 percent of the buckets to contain two different key values.



Tip

To determine the right

for your data, see.

`BUCKET_COUNT`
