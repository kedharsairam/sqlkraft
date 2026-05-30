---
title: "How to: Install & Manage Feature Extensions"
topic: "ssb-diagnose"
description: |
  09/10/2025

  You can add rules for analyzing database code, conditions for database unit tests and

  build/deployment contributors to increase the functionality that Visual Studio editions

  including SQ
tags:
  - "ssb-diagnose"
  - "how-to-install-manage-feature-extensions"
pubDate: 2025-12-01
---

09/10/2025

You can add rules for analyzing database code, conditions for database unit tests and

build/deployment contributors to increase the functionality that Visual Studio editions

including SQL Server Data Tools offer. However, you must first install a feature extension before

you can use it, whether you created the extension or you installed one that someone else

created.

Where to install your extension depends on the extension type, and from where you intend to

use it. In the latest editions of Visual Studio, the install location of some components has

moved from the SQL Server install directory to inside the Visual Studio directory. This setup

makes it easier to have different versions of the software running side by side, but it means

that you might need to install your extension in multiple locations if you wish to use it in

different version of SQL Server Data Tools and from the command line.

Custom Test Condition for

SQL Server Unit Tests

Build Contributors

Deployment Contributors

Static Code Analysis Rules

The

varies depending on which version of Visual Studio you're

using and where you chose to install it. For Visual Studio 2012, it's usually

. For Visual Studio 2013, it's usually

.

Extensions can be run as part of our command-line services:

ﾉ

Expand table

ﾉ

Expand table

```cmd
<Visual Studio Install
Dir>\Common7\IDE\Extensions\Microsoft\SQLDB\TestConditions
<Visual Studio Install
Dir>\Common7\IDE\Extensions\Microsoft\SQLDB\DAC\120\Extensions
<Visual Studio Install Dir>
C:\Program Files (x86)\Microsoft Visual Studio 11.0
C:\Program Files (x86)\Microsoft Visual Studio 12.0
```
