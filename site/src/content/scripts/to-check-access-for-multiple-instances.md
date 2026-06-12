---
name: "To Check Access for Multiple Instances"
title: "To Check Access for Multiple Instances"
description: "diagnostic script for security-audit operations."
category: security-audit
tags: ["health-check", "security-audit"]
pubDate: 2025-03-15
---

```sql
# run this in powershell ise
# make sure to provide the file with all of the instances names in it

Function TestSQLInstance
{
Param([String] $InputFile)
Function Test-SQLConn ($Server)
{
$connectionString = "Data Source=[datasource];Integrated Security=true;Initial Catalog=[database];Connect Timeout=3;"
$sqlConn = new-object ("Data.SqlClient.SqlConnection") $connectionString trap
{
Write-output "$instance Cannot connect.";
continue
}
$sqlConn.Open()

if ($sqlConn.State -eq 'Open')
{
$sqlConn.Close();
"$instance Opened successfully."
}
}

ForEach ($instance in Get-Content $InputFile)
{
Test-SQLConn -server $instance
}
}

TestSQLInstance -InputFile 'Serverlist.txt' |Out-File C:\Ouptut.txt
```
