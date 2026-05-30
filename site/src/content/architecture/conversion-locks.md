---
title: "Conversion locks"
topic: "locking"
description: "Insert range, null resource lock; used to test ranges before inserting a new key"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

## Description

Insert range, null resource lock; used to test ranges before inserting a new key

into an index.

Exclusive range, exclusive resource lock; used when updating a key in a range.

Key-range lock modes have a compatibility matrix that shows which locks are compatible with

other locks obtained on overlapping keys and ranges.

Yes

Yes

No

Yes

Yes

Yes

No

Yes

No

No

Yes

No

Yes

No

No

No

No

No

No

Yes

No

Yes

Yes

No

Yes

Yes

No

No

Yes

No

No

Yes

No

No

No

Yes

Yes

Yes

No

No

Yes

No

No

No

No

No

No

No

No

Conversion locks are created when a key-range lock overlaps another lock.

７

Note

The internal

lock mode is compatible with all other lock modes.

ﾉ

Expand table

ﾉ

Expand table

```sql
RangeI
Null
RangeI-
N
```

```sql
RangeX
X
RangeX-
X
```

```sql
S
U
X
RangeS-S
RangeS-U
RangeI-N
RangeX-X
```

```sql
S
```

```sql
U
```

```sql
X
```

```sql
RangeS-S
```

```sql
RangeS-U
```

```sql
RangeI-N
```

```sql
RangeX-X
```

```sql
S
RangeI-N
RangeI-S
U
RangeI-N
RangeI-U
```

`Null`
