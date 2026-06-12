---
title: "Configure the hash index bucket count"
topic: "index-architecture"
description: "The interplay of the hash index and the buckets is summarized in the following image."
tags: ["index-architecture","architecture"]
pubDate: "2026-05-29"
---

The interplay of the hash index and the buckets is summarized in the following image.

The hash index bucket count is specified at index create time, and can be changed using the

## syntax.

In most cases, the bucket count should be between 1 and 2 times the number of distinct values

in the index key. You might not always be able to predict how many values a particular index

key has. Performance is usually still good if the

value is within 10 times of the

actual number of key values, and overestimating is generally better than underestimating.

Too

few

buckets can have the following drawbacks:

More hash collisions of distinct key values.

Each distinct value is forced to share the same bucket with a different distinct value.

The average chain length per bucket grows.

The longer the bucket chain, the slower the speed of equality lookups in the index.

Too

many

buckets can have the following drawbacks:

Too high a bucket count can result in more empty buckets.

Empty buckets affect the performance of full index scans. If scans are performed regularly,

consider picking a bucket count close to the number of distinct index key values.

Empty buckets use memory, though each bucket uses only 8 bytes.

７

Note

Adding more buckets does nothing to reduce the chaining together of entries that share a

duplicate value. The rate of value duplication is used to decide whether a hash index or a

nonclustered index is the appropriate index type, not to calculate the bucket count.

```sql
ALTER TABLE.ALTER INDEX REBUILD
```

`BUCKET_COUNT`
