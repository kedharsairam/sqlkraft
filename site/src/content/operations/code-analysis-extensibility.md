---
title: "Code analysis extensibility"
topic: "ssms"
description: "The provided code analysis rules report on Transact-SQL design, naming, and performance warnings in your database code."
tags: ["ssms","code-analysis-extensibility"]
pubDate: 2025-12-01
---

The

provided code analysis rules

report on Transact-SQL design, naming, and performance

warnings in your database code. If the built-in code analysis rules don't include coverage for a

specific T-SQL issue or antipattern that you want to automatically detect, you can create

custom database code analysis rules.

For example, you might want to create a custom rule that avoids using the WAITFOR DELAY

statement, as demonstrated in

Author custom code analysis rules. To create custom database

code analysis rules, you use the classes in the

CodeAnalysis

namespace.

This overview covers the basic architecture among the various components of database code

analysis rules.

The following diagram illustrates how database code analysis rules components are processed:

When you use the database code analysis rules feature, all the rules are loaded and used

according to how you configured them in your project. For more information, see

How to:

Enable and Disable Specific Rules for Static Analysis of Database Code. The Extension Manager

also loads any custom rule assemblies that you created and registered.

A custom code analysis rule class inherits from

SqlCodeAnalysisRule. The custom rule class can

access useful objects via its rule execution context. These objects include:


