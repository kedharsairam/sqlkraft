---
title: "Conversion locks"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

## Description

into an index.

Exclusive range, exclusive resource lock; used when updating a key in a range.

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

ﾉ

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
