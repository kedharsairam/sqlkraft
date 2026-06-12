---
title: "Modify a filter"
topic: "profiler"
description: "06/05/2025 You add filters to trace templates, which contain the trace definitions, to limit the number of events gathered by a trace. Limiting t"
tags: ["profiler","modify-a-filter"]
pubDate: "2025-12-01"
---

You add filters to trace templates, which contain the trace definitions, to limit the number of

events gathered by a trace. Limiting the number of events gathered can reduce the

performance effects of tracing. If you set filters for a trace template, and find that the trace isn't

gathering the kind of information that you need, you can edit the filter.

1. In SQL Server Profiler, open the template for the trace filter that you want to modify. On

the

menu, select

, and then choose.

2. In the

tab of the

dialog, select a template from the

list.

3. Select the

tab.

The

tab contains a grid control. The grid control is a table that contains

each of the traceable event classes. The table contains one row for each event class. The

event classes might differ slightly, depending on the type and version of server to which

you connect. The event classes are identified in the

column of the grid and are

grouped by event category. The remaining columns list the data columns that can be

returned for each event class.

4. Select.

5. In the

dialog box, select the value next to the comparison operator that you

want to edit, and type the new value or delete a value. You can also add extra filters.

6. Select

and save the template.

Profiler
