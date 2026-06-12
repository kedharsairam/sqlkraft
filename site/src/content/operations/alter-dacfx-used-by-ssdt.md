---
title: "Alter DacFx Used by SSDT"
topic: "data-tools"
description: |
  09/10/2025
          
            Under specific circumstances you might need to use a different version of
          
            DacFx
          
            with the SQL
          
            Server Data Tools interface in Visual Studio. When possible, it's recommended to use a
          
            stan
tags: ["data-tools","alter-dacfx-used-by-ssdt"]
pubDate: 2025-12-01
---

Under specific circumstances you might need to use a different version of

DacFx

with the SQL

Server Data Tools interface in Visual Studio. When possible, it's recommended to use a

standalone version of DacFx if an alternative version from SQL Server Data Tools is required.

Follow the process below to alter the version of DacFx used by SQL Server Data Tools (SSDT).

Data Tools stores the DacFx files under

within the Visual Studio program files. For Visual

Studio 2022 Community, the full path is commonly.

Substitution should be done within the same major version of DacFx. For example, if Visual

Studio 17.9 (2022) utilizes DacFx version 162.2.33.1, only other 162.x versions should be used.

To view the current version, select

file in File Explorer from the

SSDT DacFx folder and use the context menu to open the file properties.

DacFx is published to

NuGet. Identify the desired version within the

Microsoft.SqlServer.DacFx NuGet feed and follow these steps to use it with SSDT:

1. Download the NuGet package for the DacFx version from the web interface.

2. Change the

nupkg

file to a

zip

file and extract the archive.

3. Close Visual Studio.

4. Copy the following files from

into the SSDT DacFx folder:

Microsoft.Data.Tools.Schema.Sql.dll

Microsoft.Data.Tools.Utilities.dll

Microsoft.SqlServer.Dac.dll

Microsoft.SqlServer.Dac.Extensions.dll

Microsoft.SqlServer.Dac.Extensions.xml

Microsoft.SqlServer.Dac.xml

Microsoft.SqlServer.TransactSql.ScriptDom.dll

Microsoft.SqlServer.Types.dll

```cmd
Common7\IDE\Extensions\Microsoft\SQLDB\DAC
C:\Program Files\Microsoft Visual
Studio\2022\Community\Common7\IDE\Extensions\Microsoft\SQLDB\DAC
Microsoft.SqlServer.Dac.dll lib/net462
```
