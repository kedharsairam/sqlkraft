---
name: "B. Multiple updates"
title: "B. Multiple updates"
category: "statements"
description: "Here's the result set."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Here's the result set.

JSON

With

, you can update only one property. If you have to do multiple updates, you

can use multiple

calls.

Here's the result set.

JSON

## C. Rename a key

## D. Increment a value

The following example shows how to rename a property in JSON text with the

function. First you can take the value of an existing property and insert it as a new key:value

pair. Then you can delete the old key by setting the value of the old property to.

Here's the result set.

JSON

If you don't cast the new value to a numeric type,

treats it as text and surrounds it

with double quotes.

The following example shows how to increment the value of a property in JSON text with the

function. First you can take the value of the existing property and insert it as a

new key:value pair. Then you can delete the old key by setting the value of the old property to.

## E. Modify a JSON object

Here's the result set.

JSON

treats the

newValue

argument as plain text even if it contains properly formatted

JSON text. As a result, the JSON output of the function is surrounded with double quotes and

all special characters are escaped, as shown in the following example.

Here's the result set.

JSON

## F. Update a JSON column

To avoid automatic escaping, provide

newValue

by using the

function.

knows that the value returned by

is properly formatted JSON, so it doesn't escape

the value.

Here's the result set.

JSON

The following example updates the value of a property in a table column that contains JSON.

JSON Path Expressions

JSON data in SQL Server
