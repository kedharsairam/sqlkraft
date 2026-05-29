---
title: "SqlPackage in development pipelines"
topic: "sqlpackage"
description: |
  SqlPackage in development pipelines
  
  06/27/2025
  
  SqlPackage
  
  is a command-line utility that automates several database development tasks and
  
  can be incorporated into CI/CD pipelines.
  
  If SqlPackage i
tags:
  - "sqlpackage"
  - "sqlpackage-in-development-pipelines"
pubDate: 2025-12-01
---

SqlPackage in development pipelines

06/27/2025

SqlPackage

is a command-line utility that automates several database development tasks and

can be incorporated into CI/CD pipelines.

If SqlPackage is installed as a global dotnet tool (recommended), you can invoke it in the

pipeline with simply

from any directory. If SqlPackage is installed as a standalone

executable, you must specify the full path to the executable in the pipeline. On Windows, the

standalone install of SqlPackage is available on the path

(DacFx.msi). In both Windows and Linux environments, if you download the

self-contained .zip SqlPackage for .NET, you can extract the executable to a location of your

choosing.

The virtual environments used for GitHub Actions hosted runners and Azure Pipelines virtual

machine images are managed in the

runner-images

GitHub repository. SqlPackage is

included in several environments including

and

but is no longer

included by default in

and

. Updates to the images in

runner-

images

are made within a few weeks of each SqlPackage release.

In a managed virtual environment, you would install SqlPackage at runtime in the pipeline. The

installation is performed as a separate step in either Azure Pipelines and GitHub Actions and

adds a short delay to each pipeline run while the installation occurs. To install SqlPackage at

runtime, add a step to the pipeline that uses the dotnet CLI to install SqlPackage as a global

tool. This step should be run before any SqlPackage actions in the pipeline.

Bash

７

Note

Utilizing a

for pipeline automation is

recommended over using the SqlPackage executables bundled with other applications,

including SQL Server Management Studio or Visual Studio. The standalone installation of

SqlPackage is updated more frequently and isn't tied to the release cadence of other

applications.

```cmd
sqlpackage
C:\Program Files\Microsoft SQL
Server\170\DAC\bin
windows-latest
ubuntu-22.04
ubuntu-24.04
```