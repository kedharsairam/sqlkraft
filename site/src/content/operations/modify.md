---
title: "Modify"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  You can modify templates that are saved in a file on the local computer on which SQL Server

  Profiler is running. You can also modify t
tags:
  - "profiler"
  - "modify"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

You can modify templates that are saved in a file on the local computer on which SQL Server

Profiler is running. You can also modify templates derived from those files. When you modify

existing templates, you edit template properties such as event classes and data columns, in the

same order that the properties were set originally, on the

tab of the

dialog box. Event classes and data columns can be added or removed, and filters

can be changed. After the template is modified, a user-specific template is created and the

original system template is left intact. For more information, see

Save traces and trace

templates

.

You might need to derive a template from an existing trace file if you can't remember (or

haven't saved) the original template that was used to create the trace, or if you want to run the

same trace at a later date. When working with existing traces, you can view the properties, but

you can't modify the properties. To modify the properties, stop or pause the trace. For more

information, see

Derive a template from a trace file or trace table (SQL Server Profiler)

and

Derive a template from a running trace (SQL Server Profiler)

.

1. On the

menu, point to

, and then select

.

2. In the

dialog box, on the

tab, you can modify the

server type and template name, or choose to use a default template for the server type.

3. On the

tab, use the grid control to add or remove events and data

columns from the trace file as follows.

To add an event, expand the appropriate event category in the

column, and

then select the event name.

When you add an event, all relevant data columns are included by default. To

remove a data column for an event from a trace, clear the check box in the data

column for the event.

To add filters, select the data column name and specify the filter criteria in the

dialog box. You can also right-click the data column name, and select

to launch the

dialog box. Select

to add the filter.

4. Select

, or select

to save the trace template under another name.
