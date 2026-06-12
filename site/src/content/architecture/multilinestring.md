---
title: "MultiLineString"
topic: "spatial-data"
description: "SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric A is a collectio"
tags: ["spatial-data","multilinestring"]
pubDate: "2025-12-01"
---

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

A

is a collection of zero or more

or

instances.

The following illustration shows examples of

instances.

As shown in the illustration:

Figure 1 is a simple

instance whose boundary is the four endpoints of its

two

elements.

Figure 2 is a simple

instance because only the endpoints of the

elements intersect. The boundary is the two nonoverlapping endpoints.

Figure 3 is a nonsimple

instance because the interior of one of its

elements is intersected. The boundary of this

instance is the

four endpoints.

Figure 4 is a nonsimple, nonclosed

instance.

Figure 5 is a simple, nonclosed. It is not closed because its

elements are not closed. It is simple because none of the interiors of any of the

instances intersect.
