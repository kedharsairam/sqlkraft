---
name: "Specifying a User or Login Name"
title: "Specifying a User or Login Name"
category: "operators"
description: ""
tags: ["tsql","operators"]
pubDate: "2026-05-29"
---

CALLER

When used inside a module, specifies the statements inside the module are executed in the

context of the caller of the module. When used outside a module, the statement has no action.

The change in execution context remains in effect until one of the following occurs:

Another EXECUTE AS statement is run.

A REVERT statement is run.

The session is dropped.

The stored procedure or trigger where the command was executed exits.

You can create an execution context stack by calling the EXECUTE AS statement multiple times

across multiple principals. When called, the REVERT statement switches the context to the login

or user in the next level up in the context stack. For a demonstration of this behavior, see

Example A.

The user or login name specified in EXECUTE AS <context_specification> must exist as a

principal in

or

, respectively, or the EXECUTE AS

statement fails. Additionally, IMPERSONATE permissions must be granted on the principal.

Unless the caller is the database owner, or is a member of the

fixed server role, the

７

Note

The cookie

parameter for is currently documented as

which is

the correct maximum length. However the current implementation returns.

Applications should reserve

so that the application continues to operate

correctly if the cookie return size increases in a future release.

７

Note

This option is not available in Azure Synapse Analytics.

## CompanyDomain\SQLUsers

## Sales

## CompanyDomain\SqlUser1

## Sales

## CompanyDomain\SqlUser1

## WITHOUT LOGIN

## EXECUTE AS
