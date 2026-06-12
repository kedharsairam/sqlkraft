---
title: "Use Agent mode tools"
topic: "profiler"
description: |
  Quickstart: Use GitHub Copilot Agent
          
            Agent Mode allows GitHub Copilot to use the tools available in the MSSQL extension for Visual
          
            Studio Code. When the extension is installed and active, Copilot ca
tags: ["profiler","use-agent-mode-tools"]
pubDate: 2025-12-01
---

Quickstart: Use GitHub Copilot Agent

Agent Mode allows GitHub Copilot to use the tools available in the MSSQL extension for Visual

Studio Code. When the extension is installed and active, Copilot can list SQL Server

connections, connect to a server and database, and retrieve database metadata.

All actions use the same connection context and credentials as the MSSQL extension. Agent

Mode doesn't introduce additional authentication or permission changes.

For details about how Agent Mode selects and executes tools, see the

Visual Studio Code

documentation on Agent Mode.

Agent Mode lets GitHub Copilot perform SQL-related actions using the MSSQL extension, and

user confirmation is required before execution.

You can invoke these actions by using chat variables such as

, or by issuing

equivalent natural-language requests, for example:

Copilot prompt



Tip

You don't need to reference the MSSQL extension (

) explicitly when using Agent

Mode. If the extension is active, its tools are available automatically. For more information,

see.

```cmd
#mssql_connect
@mssql
Connect to my Library database using my LocalDev profile
```
