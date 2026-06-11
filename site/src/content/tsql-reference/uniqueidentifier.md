---
name: "uniqueidentifier"
title: "Uniqueidentifier"
category: "data-types"
description: "A 16-byte GUID (globally unique identifier) data type."
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---
## Syntax

`uniqueidentifier`

## Arguments

### @variable

A variable declared as uniqueidentifier can store a 16-byte GUID value.

## Remarks

The uniqueidentifier data type stores 16-byte binary values that are globally unique. Use NEWID() or NEWSEQUENTIALID() to generate values. Column values can be compared using =, <, >, <=, >= operators but not arithmetic operations.

## Examples

```sql
-- Create a table with a uniqueidentifier column
CREATE TABLE Example.GuidTable (
    ID uniqueidentifier DEFAULT NEWID(),
    Name nvarchar(50)
);

-- Insert with explicit GUID
INSERT INTO Example.GuidTable (ID, Name)
VALUES ('6F9619FF-8B86-D011-B42D-00C04FC964FF', 'Sample');
```
