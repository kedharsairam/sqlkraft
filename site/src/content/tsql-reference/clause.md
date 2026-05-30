---
name: "Clause"
title: "Clause"
category: "statements"
description: "In the definition of a check constraint."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

In the definition of a check constraint.

In the definition of a rule or default object. (It can be used in a default constraint.)

As a default in a user-defined table type.

In a statement using

,

, or when the

option is set.

In the

clause of a statement.

In a

statement. (Except when the

function is used in a default

constraint in the target table and default is used in the

statement of the

statement.)

When using the

function in a default constraint, the following rules apply:

A single sequence object may be referenced from default constraints in multiple tables.

The table and the sequence object must reside in the same database.

The user adding the default constraint must have REFERENCES permission on the

sequence object.

A sequence object that is referenced from a default constraint cannot be dropped before

the default constraint is dropped.

The same sequence number is returned for all columns in a row if multiple default

constraints use the same sequence object, or if the same sequence object is used both in

the statement supplying the values, and in a default constraint being executed.

References to the

function in a default constraint cannot specify the

clause.

A sequence object that is referenced in a default constraint can be altered.

In the case of an

or

statement where the data being

inserted comes from a query using an

clause, the values being returned by the

function will be generated in the order specified by the

clause.

### NEXT VALUE FOR

### OVER

### NEXT VALUE FOR

### OVER

### OVER

### ORDER BY

### NEXT VALUE FOR

### OVER

### NEXT VALUE FOR

### OVER

### NEXT VALUE FOR

### OVER

### OVER

### NEXT VALUE FOR

### PARTITION BY

### NEXT VALUE FOR

### SELECT

### OVER

### ORDER BY

### SELECT

### OVER

### NEXT VALUE FOR

### SELECT

### OVER

### NEXT

### VALUE FOR

### UPDATE

### MERGE

### UPDATE

```sql
INSERT ... SELECT
```

```sql
INSERT ... EXEC
```
