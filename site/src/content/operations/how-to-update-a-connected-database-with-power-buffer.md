---
title: "How to: Update a Connected Database with Power Buffer"
topic: "ssb-diagnose"
description: |
  09/10/2025

  SQL Server Data Tools (SSDT) Power Buffer technology makes it easy for you to apply changes

  to your connected database by storing all your edits in the current session. Any errors caused

tags:
  - "ssb-diagnose"
  - "how-to-update-a-connected-database-with-power-buffer"
pubDate: 2025-12-01
---

09/10/2025

Data Tools (SSDT) Power Buffer technology makes it easy for you to apply changes

to your connected database by storing all your edits in the current session. Any errors caused

by editing in Power Buffer window (in either the Transact-SQL Editor or Table Designer)

immediately show up in the

pane, which enables you to follow the errors identified

for further troubleshooting. You can verify your pending changes until you're ready to apply

them to your database. During the update process, SSDT automatically creates an

script

based on your edits, and alerts you of any potential issues. You can then apply all the changes

that accumulated across all open Power Buffer windows to the same database, or save the

script to be deployed later.

SSDT is also aware of any changes made to your database schema outside Visual Studio. For

example, if you add a new table to an existing database in SQL Server Management Studio,

such change immediately shows up in the SQL Server Object Explorer in Visual Studio without

manually refreshing it. The drift detection feature ensures that you're always viewing the latest

schema definition of a database in SQL Server Object Explorer. Any database objects opened in

Table Designer or Transact-SQL Editor for editing aren't refreshed to show changes outside

Visual Studio.

The following procedures utilize entities created in previous procedures in the

Manage tables,

relationships, and fix errors

section.

1. Select the green

button on the toolbar ("Update Database" tooltip is displayed if

you hover over the button). The toolbar is above the Columns Grid of the Table Designer.

2. The

dialog box appears. A deployment script based on your

changes is generated in the background. The dialog box then shows a summary of the

actions SSDT is going to take (for example, creating or dropping database entities),

together with potential issues it identifies (this isn't applicable to our procedure, but

comes in handy when your database definition contains errors that prevent an update

action until resolved).

3. If you don't want to update the database at this moment, select the

button to exit

the

dialog box.

```cmd
ALTER
ALTER
```
