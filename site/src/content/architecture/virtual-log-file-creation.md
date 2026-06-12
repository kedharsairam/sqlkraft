---
title: "Virtual log file creation"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

The SQL Server Database Engine divides each physical log file internally into several virtual log

files (VLFs). Virtual log files have no fixed size, and there's no fixed number of virtual log files

for a physical log file. The Database Engine chooses the size of the virtual log files dynamically

while it's creating or extending log files. The Database Engine tries to maintain a few virtual

files. The size of the virtual files after a log file has been extended is the sum of the size of the

existing log and the size of the new file increment. The size or number of virtual log files can't

be configured or set by administrators.

Virtual log file (VLF) creation follows this method:

In SQL Server 2014 (12.x) and later versions, if the next growth is less than 1/8 of the

current log physical size, then create 1 VLF that covers the growth size.

If the next growth is more than 1/8 of the current log size, use the pre-2014 method,

namely:

If growth is less than 64 MB, create 4 VLFs that cover the growth size (for example, for

1-MB growth, create 4 VLFs of size 256 KB).

In Azure SQL Database, and starting with SQL Server 2022 (16.x) (all editions), the

logic is slightly different. If the growth is less than or equal to 64 MB, the Database

Engine creates only one VLF to cover the growth size.

If growth is from 64 MB up to 1 GB, create 8 VLFs that cover the growth size (for

example, for 512-MB growth, create 8 VLFs of size 64 MB).

If growth is larger than 1 GB, create 16 VLFs that cover the growth size for example, for

8-GB growth, create 16 VLFs of size 512 MB).

If the log files grow to a large size in many small increments, they end up with many virtual log

files.

Conversely, if the log files are set

to a large size with few or just one increment, they contain few very large virtual log files. For

more information on properly estimating the

and

setting of a

transaction log, see the

Recommendations

section of

Manage the size of the transaction log

file.

We recommend that you create your log files close to the final size required, using the

increments needed to achieve optimal VLF distribution, and have a relatively large

growth_increment

value.

See the following tips to determine the optimal VLF distribution for the current transaction log

size:

### Fixing-VLFs script
