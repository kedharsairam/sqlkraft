---
title: "Use the schema explorer and designer"
topic: "profiler"
description: |
  Quickstart: Use the schema explorer and

  In this quickstart, you learn how GitHub Copilot assists developers in designing, understanding,

  and evolving database schemas with context-aware suggestions.
tags:
  - "profiler"
  - "use-the-schema-explorer-and-designer"
pubDate: 2025-12-01
---

Quickstart: Use the schema explorer and

In this quickstart, you learn how GitHub Copilot assists developers in designing, understanding,

and evolving database schemas with context-aware suggestions. Whether you're building from

scratch or reverse-engineering existing tables, GitHub Copilot streamlines the process across

SQL and object-relational mapping (ORM) frameworks. It makes schema work faster, smarter,

and easier to maintain.

This section covers both creating new schemas from scratch and working with existing

databases. You can use GitHub Copilot to generate code-first schema definitions, update

objects, or reverse-engineer and explore existing databases.



Tip

Looking for the GitHub Copilot integration within the Schema Designer visual canvas? See

for the AI-powered visual

schema design experience.

```cmd
Write a SQL script to create a new schema named `blog` for a blog application. The
schema should include three tables: `Posts`, `Comments`, and `Users`. Each table
must have appropriate primary keys, and the necessary foreign key relationships and
constraints should be defined.
Add a new column named `LastModified` of type `datetime` to the `Posts` table in
the `blog` schema. Generate the updated SQL script reflecting this change,
including the full definition of the modified schema.
It isn't needed to create the schema, but it would be great if you could use the
script generated and run it to validate the accuracy of the generated code. The
following section continues using this new schema called `blog`.
```
