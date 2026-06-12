---
title: "How to: Compare & Synchronize the Data of Two Databases"
topic: "ssb-diagnose"
description: |
  09/10/2025
          
            You can compare the data that is contained in two databases. The databases that you compare
          
            are known as the
          
            source
          
            and the
          
            target
          
            .
          
            As the data is compared, a
          
            Data Manipulation Lan
tags: ["ssb-diagnose","how-to-compare-synchronize-the-data-of-two-databases"]
pubDate: 2025-12-01
---

You can compare the data that is contained in two databases. The databases that you compare

are known as the

source

and the

target.

As the data is compared, a

Data Manipulation Language

(DML) script is generated, which you

can use to synchronize the differing databases by updating some or all of the data on the

target database. When the data comparison finishes, its results appear in the Data Compare

window of Visual Studio.

After the comparison finishes, you can take other steps:

You can view the differences between the two databases. For more information, see

Viewing Data Differences.

You can update all or part of the target to match the source. For more information, see

Synchronizing Database Data.

For more information, see

Compare and synchronize data in one or more tables with data in a

reference database.

1. From the main menu, go to

>

>.

７

Note

Database projects

and

or

packages can't be the source or target in a data

comparison.

７

Note

You can also compare the

schema

of two databases or of two versions of the same

database. For more information, see.

```cmd.dacpac.bacpac
```
