---
title: "How to: Create a Snapshot of a Project"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  A
  
  file provides you with a read-only representation of the database
  
  schema at the time it's created. It's essentially being treated as a database schema from which
  
  you can import the sc
tags:
  - "ssb-diagnose"
  - "how-to-create-a-snapshot-of-a-project"
pubDate: 2025-12-01
---

09/10/2025

A

file provides you with a read-only representation of the database

schema at the time it's created. It's essentially being treated as a database schema from which

you can import the schema objects back to a project. You can also compare it with the schema

of a database or a project, and update the database or project to reflect the schema defined in

the snapshot.

In the event of a user error on a source database project, you can revert the source project to

the state it was in when the snapshot was created. You can also establish snapshots at various

stages of your development for baseline purpose.

1. Right-click the

project in

, and select

.

2. SQL Server Data Tools (SSDT) attempts to build the project first. If there's no build error, a

folder is created in

. Inside this folder, SSDT creates a

file using the name format of

.

3. Right-click the

file and select

. Change the default file name to

.

4. Right-click the

function in

and select

to

remove it from the project.

5. Follow the previous steps to create a new snapshot called

.

1. Right-click the

project in

, select

, then

from the contextual menus.

2. In the

dialog box, select

to select

to be used as the source of the import.

The

section has been disabled, since the current project is the default

target. Select

to start the import.

```cmd
TradeDev
.dacpac
<Project Name>_YYYYMMDD_HH-MM-SS.dacpac
.dacpac
TradeDev1.dacpac
```