---
title: "FrameWindowVisible"
topic: "profiler"
description: |
  SqlToolsVSNativeHelpers -

  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Property that specifies whether a given window frame is visible. The helper method is used

  from managed
tags:
  - "profiler"
  - "framewindowvisible"
pubDate: 2025-12-01
---

SqlToolsVSNativeHelpers -

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Property that specifies whether a given window frame is visible. The helper method is used

from managed code.

frame

IVsWindowFrame\* pointer to a Visual Studio WindowFrame.

A Boolean value that specifies whether the window frame specified by

frame

is visible.

SqlToolsVSNativeHelpers

```cmd
BOOL WINAPI IsFrameWindowVisible(IVsWindowFrame* frame)
{
if (NULL == frame)
{
return FALSE;
}
return S_OK == frame->IsVisible();
}
```
