---
title: "Change tracking"
topic: "change-data-capture"
description: ""
tags: ["change-data-capture","change-tracking"]
pubDate: "2025-12-01"
---

This article describes the change tracking feature for SQL Server, which is a lightweight solution

that provides an efficient change tracking mechanism for applications.

To get started, review

Configure change tracking.

Previously, to enable applications to query for changes to data in a database and access

information that is related to the changes, application developers had to implement custom

change tracking mechanisms. These mechanisms typically involved a lot of work such as a

combination of triggers,

columns, new tables to store tracking information, and

custom cleanup processes. The change tracking feature of SQL Server simplifies this process,

making it easy to identify information related to changes without the need for a custom

solution.

Different types of applications have different requirements for how much information they

need about the changes. Applications can use change tracking to answer the following

questions about the changes that have been made to a user table:

What rows have changed for a user table?

Only the fact that a row has changed is required, not how many times the row has

changed or the values of any intermediate changes.

The latest data can be obtained directly from the table that is being tracked.

Has a row changed?

The fact that a row has changed and information about the change must be available

and recorded at the time that the change was made in the same transaction.

７

Note

If an application requires information about all the changes that were made and the

intermediate values of the changed data, using change data capture, instead of change

tracking, might be appropriate. For more information, see.
