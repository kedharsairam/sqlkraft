---
title: "How to: Create Test Conditions for the SQL Server Unit Test Designer"
topic: "ssb-diagnose"
description: |
  09/10/2025

  You can use the extensible

  TestCondition

  class to create new test conditions. For example, you

  might create a new test condition that verifies the number of columns or the values in a r
tags:
  - "ssb-diagnose"
  - "how-to-create-test-conditions-for-the-sql-server-unit-test-designer"
pubDate: 2025-12-01
---

09/10/2025

You can use the extensible

TestCondition

class to create new test conditions. For example, you

might create a new test condition that verifies the number of columns or the values in a result

set.

This procedure explains how to create a test condition to appear in the SQL Server Unit Test

Designer.

1. In Visual Studio, create a class library project.

2. On the

menu, select.

3. Select the

tab.

4. In the

list, select

and then

select.

5. Add the required assembly references. Right-click the project node and then select. Select

and navigate to the

folder. Choose Microsoft.Data.Tools.Schema.Sql.dll and select

,

then select.

6. On the

menu, select.

7. Right-click on the project in

and choose.

8. Add the following

statements after the import of

:

XML

```cmd
C:\Program Files (x86)\Microsoft SQL
Server\110\DAC\Bin
Import
Microsoft.CSharp.targets
<Import
Project
=
"$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v10.0\SSDT\Microso ft.Data.Tools.Schema.Sql.UnitTesting.targets"
Condition
=
"'$(VisualStudioVersion)' == ''"
/>
<Import
Project
=
"$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVer sion)\SSDT\Microsoft.Data.Tools.Schema.Sql.UnitTesting.targets"
Condition
=
"'$(VisualStudioVersion)' != ''"
/>
```
