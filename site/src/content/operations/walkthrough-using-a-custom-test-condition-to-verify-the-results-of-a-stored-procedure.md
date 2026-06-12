---
title: "Walkthrough: Using a Custom Test Condition to Verify the Results of a Stored Procedure"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
    In this feature extension walkthrough, you create a test condition, and you verify its
  
    functionality by creating a SQL Server unit test. The process includes creating a class library
  
    pro
tags: ["ssb-diagnose","walkthrough-using-a-custom-test-condition-to-verify-the-results-of-a-stored-procedure"]
pubDate: "2025-12-01"
---

In this feature extension walkthrough, you create a test condition, and you verify its

functionality by creating a SQL Server unit test. The process includes creating a class library

project for the test condition, and signing and installing it. If you already have a test condition

that you want to update, see

How to: Upgrade a Visual Studio 2010 Custom Test Condition

from a Previous Release to SQL Server Data Tools.

This walkthrough illustrates the following tasks:

How to create a test condition.

How to sign the assembly with a strong name.

How to add the necessary references to the project.

How to build a test condition.

How to install the new test condition.

How to test the new test condition.

You must have Visual Studio 2010 or Visual Studio 2012 with the latest version of SQL Server

Data Tools to complete this walkthrough. For more information, see

Install SQL Server Data

Tools (SSDT) for Visual Studio.

First, you create a class library.

1. On the

menu, select

and then select.

2. In the

dialog box, under

, select C#.

3. Under

, select.

4. In the

text box, type

and then select.

Next, sign the project.

1. On the

menu, select.

2. On the

tab, select the

check box.

3. In the

box, select.
