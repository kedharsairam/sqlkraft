---
title: "Custom Test Conditions  for SQL Server Unit Tests"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
    You can add custom test conditions for SQL Server unit tests. However, you must first install
  
    the test condition before you can use it, whether you created the extension or you're install
tags: ["ssb-diagnose","custom-test-conditions-for-sql-server-unit-tests"]
pubDate: "2025-12-01"
---

You can add custom test conditions for SQL Server unit tests. However, you must first install

the test condition before you can use it, whether you created the extension or you're installing

one that someone else created.

Before you install a test condition that you didn't create, you should understand the following

risks:

The installation program for the test condition might be malicious and gain access to

protected resources based on your installation permissions.

The test condition itself might be malicious and gain control of protected resources if the

user who uses the extension has sufficient permissions.

To minimize risk, you should install a custom test condition only if it's from a known source. If

you obtain a test condition from an untrusted source, you should inspect the source code for

that test condition and its installation program (if it has one) before you install and it.

To install a custom test condition, copy the signed assembly (

) to the

folder. If this folder doesn't

exist, create it. You need administrative privileges on your machine to copy to this directory.

You need to install Visual Studio 2010 and Visual Studio 2012 versions of the test condition if:

You install custom test conditions on a computer that might be used to build SQL Server

unit tests.

Those unit tests are used in Visual Studio 2010 and Visual Studio 2012.

For more information about custom test conditions for SQL Server unit tests, see:

How to: Create Test Conditions for the SQL Server Unit Test Designer

How to: Upgrade a Visual Studio 2010 Custom Test Condition from a Previous Release to

Data Tools

```cmd.dll
%ProgramFiles%\Microsoft Visual Studio
<Version>\Common7\IDE\Extensions\Microsoft\SQLDB\TestConditions
```
