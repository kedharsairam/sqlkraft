---
title: "Troubleshoot SQL project build"
topic: "ssms"
description: "The SQL project build output provides feedback on the database model construction and T- SQL validation."
tags: ["ssms","troubleshoot-sql-project-build"]
pubDate: 2025-12-01
---

The SQL project build output provides feedback on the database model construction and T-

SQL validation. The default command line output only shows errors and some status

information. In this article, we discuss how to enable more verbose logging to help

troubleshoot build issues and common errors that are encountered with SQL projects.

To further troubleshoot build issues for SQL projects, you can use command line switches to

generate more logs. More logging can help in not only identifying the cause of errors but also

degradation in build speed. The two primary options are:

: This option generates a binary log file (

) that can be viewed

using the

MSBuild Log Viewer. This viewer is helpful for diagnosing dependency issues

and optimizing the build process. The command to generate this log is:

Bash

: This option generates a text log file that contains the most verbose logging

from the build. The command to generate this log is:

Bash

To recap, the combined command to generate both logs is:

Bash

The full set of switches can be found at the

MSBuild Command-Line Reference.

```cmd
msbuild.binlog dotnet build -bl dotnet build -flp:v=diag dotnet build -bl -flp:v=diag
```
