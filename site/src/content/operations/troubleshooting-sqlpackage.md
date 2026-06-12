---
title: "Troubleshooting SqlPackage"
topic: "sqlpackage"
description: |
  SqlPackage

  In some scenarios, SqlPackage operations take longer than expected or fail to complete. This

  article describes some frequently suggested tactics to troubleshoot or improve performance of

tags:
  - "sqlpackage"
  - "troubleshooting-sqlpackage"
pubDate: 2025-12-01
---

SqlPackage

In some scenarios, SqlPackage operations take longer than expected or fail to complete. This

article describes some frequently suggested tactics to troubleshoot or improve performance of

these operations. While reading the specific documentation page for each action to

understand the available parameters and properties is recommended, this article serves as a

starting point in investigating SqlPackage operations.

As general guideline, better performance can be obtained via the.NET version

of SqlPackage

instead of the.NET Framework version installed via the DacFramework.msi.

If you're unable to install the SqlPackage

dotnet tool

, which enables executing SqlPackage

commands from the command prompt in any directory:

1.

Download

the zip for SqlPackage on.NET 8 for your operating system (Windows, macOS,

or Linux).

2. Unzip archive as directed on the download page.

3. Open a command prompt and change directory (

) to the SqlPackage folder.

It's important to use the latest available version of SqlPackage as performance improvements

and bug fixes are released regularly.

If you attempted to use the Import/Export Service to import or export your database, you can

use SqlPackage to perform the same operation with more control on optional parameters and

properties. The blog post

Optimizing BACPAC Imports - SqlPackage Done Right!

walks

through the steps to use SqlPackage instead of the Import/Export Service for a

import.

For Import, an example command is:

Bash

For Export, an example command is:

```cmd
cd.bacpac./SqlPackage /Action:Import /sf:<
source
-bacpac-file-path> /tsn:<full-target-server-
name> /tdn:<a new or empty database> /tu:<target-server-username> /tp:<target-
server-password> /df:<
log
-file>
```
