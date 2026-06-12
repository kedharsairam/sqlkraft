---
title: "Install SQL Server Integration Services"
topic: "linux-operations"
description: "- Linux Follow the steps in this article to install SQL Server Integration Services ( ) on Linux. For more information about the features that are supported in Integration"
tags: ["linux-operations","install-sql-server-integration-services"]
pubDate: "2025-12-01"
---

- Linux

Follow the steps in this article to install SQL Server Integration Services (

) on

Linux. For more information about the features that are supported in Integration Services for

Linux, see

Limitations and known issues for SSIS on Linux.

You can install SQL Server Integration Services (SSIS) on Red Hat Enterprise Linux (RHEL) and

Ubuntu. SUSE Linux Enterprise Server (SLES) isn't supported. Installing SSIS on containers is

also not supported.

To install the

package on RHEL, follow these steps:

1. Download the SQL Server Red Hat repository configuration file.

Bash

2. Run the following command to install SQL Server Integration Services.

Bash

3. After installation, run. For more info, see

Configure SQL Server Integration

Services on Linux with ssis-conf.

Bash

4. After the configuration is done, set the

environment variable.

Bash

Red Hat Enterprise Linux

```cmd
PATH sudo curl -o /etc/yum.repos.d/mssql-server.repo https://packages.microsoft.com/config/rhel/8/mssql-server-2022.repo sudo yum install -y mssql-server-is sudo /opt/ssis/bin/ssis-conf setup
```
