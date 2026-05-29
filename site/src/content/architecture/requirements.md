---
title: "Requirements"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  A type in a common language runtime (CLR) assembly can be registered as a user-defined

  aggregate function, as long as it implements the required aggre
tags:
  - "clr-integration"
  - "requirements"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

A type in a common language runtime (CLR) assembly can be registered as a user-defined

aggregate function, as long as it implements the required aggregation contract. This contract

consists of the

attribute and the aggregation contract methods. The

aggregation contract includes the mechanism to save the intermediate state of the

aggregation, and the mechanism to accumulate new values, which consist of four methods:

,

,

, and

. Once you meet these requirements, you can take full

advantage of user-defined aggregates in SQL Server. This article provides more information

about how to create and work with user-defined aggregates. For an example, see

Invoke CLR

user-defined aggregate functions

.

For more information, see

SqlUserDefinedAggregateAttribute

.

The class registered as a user-defined aggregate should support the following instance

methods. The query processor uses the following methods to compute the aggregation.

Init

Accumulate

Merge

Terminate

Syntax:

C#

The query processor uses this method to initialize the computation of the aggregation. This

method is invoked once for each group that the query processor is aggregating. The query

processor might choose to reuse the same instance of the aggregate class for computing

aggregates of multiple groups. The

method should perform any clean-up as necessary

from previous uses of this instance, and enable it to restart a new aggregate computation.

```sql
SqlUserDefinedAggregate
Init
Accumulate
Merge
Terminate
Init
public
void
Init
();
```
