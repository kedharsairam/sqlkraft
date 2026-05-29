---
title: "How to: Upgrade a Visual Studio 2010 Custom Test Condition from a Previous Release to SQL Server Data Tools"
topic: "data-tools"
description: |
  09/10/2025
  
  To use a test unit condition that you created in a version before SQL Server Data Tools, you
  
  must upgrade it.
  
  To update the project references:
  
  1. For Visual Basic only, in
  
  , select
  
  .
tags:
  - "data-tools"
  - "how-to-upgrade-a-visual-studio-2010-custom-test-condition-from-a-previous-release-to-sql-server-data-tools"
pubDate: 2025-12-01
---

09/10/2025

To use a test unit condition that you created in a version before SQL Server Data Tools, you

must upgrade it.

To update the project references:

1. For Visual Basic only, in

, select

.

2. In

, expand the

node.

3. Right-click the following assembly references and select

:

a. Microsoft.Data.Schema.UnitTesting

b. Microsoft.Data.Schema

4. On the

menu, or by right-clicking the project folder in

, select

.

5. Select the

tab.

6. In the

list, select

and select

.

7. Add the required assembly references. Right-click the project node and then select

. Select

and navigate to the

folder. Choose Microsoft.Data.Tools.Schema.Sql.dll and select

,

then select

.

8. On the

menu, select

.

9. Right-click on the

in

and choose

.

10. Add the following Import statement after the import of

:

XML

```cmd
C:\Program Files (x86)\Microsoft SQL
Server\110\DAC\Bin
Microsoft.CSharp.targets
```