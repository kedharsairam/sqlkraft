---
title: "How to: Fix Errors"
topic: "ssb-diagnose"
description: |
  09/10/2025

  The Error List pane displays any deployment or build errors. Syntax and semantic errors caused

  by editing in either the Transact-SQL Editor or Table Designer also shows up in the list whe
tags:
  - "ssb-diagnose"
  - "how-to-fix-errors"
pubDate: 2025-12-01
---

09/10/2025

The Error List pane displays any deployment or build errors. Syntax and semantic errors caused

by editing in either the Transact-SQL Editor or Table Designer also shows up in the list when

you're editing database entities and its definitions. The Error List is dynamically updated as you

edit scripts across different tabs. You can then follow the errors identified for further

troubleshooting.

1. Right-click the

table (

) in

and select

.

2. In the Columns Grid of the designer, right-click the

column and select

to delete this column from the table.

3. In the

pane at the bottom of the screen, a warning, and an error similar to the

following pop-up immediately.

Output

4. You can right-click the

and use the contextual menus to sort results, filter which

entries you want to display, and which columns of information you want to appear for

each entry.

Double-click the first warning identified and follow it to the script file that generated the

warning. The problematic code section is highlighted. In the example, it's because the

column is being used by both a

and

statement in a table-value

function created previously.

5. In the Transact-SQL Editor, remove

from the function.

6. Fix the second error in a similar manner by removing the check constraint.

```cmd
Product
Product.sql
ShelfLife
ShelfLife
RETURN
```
