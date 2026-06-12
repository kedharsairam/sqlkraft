---
title: "Split page"
topic: "query-processing"
description: "Point lookups are similar to B-trees, except that because pages are linked in only one direction,"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

Point lookups are similar to B-trees, except that because pages are linked in only one direction,

the Database Engine follows right page pointers, where each nonleaf page has the highest

value of its child, rather than lowest value as in a B-tree.

If a leaf-level page has to change, the Database Engine doesn't modify the page itself. Rather,

the Database Engine creates a delta record that describes the change, and appends it to the

previous page. Then it also updates the page map table address for that previous page, to the

address of the delta record that now becomes the physical address for this page.

There are three different operations that can be required for managing the structure of a Bw-

tree: consolidation, split, and merge.

A long chain of delta records can eventually degrade search performance as it could require

long chain traversal when searching through an index. If a new delta record is added to a chain

that already has 16 elements, the changes in the delta records are consolidated into the

referenced index page, and the page is then rebuilt, including the changes indicated by the

new delta record that triggered the consolidation. The newly rebuilt page has the same page

ID but a new memory address.

An index page in Bw-tree grows on as-needed basis starting from storing a single row to

storing a maximum of 8 KB. Once the index page grows to 8 KB, a new insert of a single row

## Step 1:

## Step 2:
