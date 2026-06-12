---
name: "Upgrade databases"
title: "Upgrade databases"
category: "statements"
description: "and a path that only visits the root is represented by a single slash."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

and a path that only visits the root is represented by a single slash. For levels underneath the

root, each label is encoded as a sequence of integers separated by dots.

Comparison between children is performed by comparing the integer sequences separated by

dots in dictionary order. Each level is followed by a slash. Therefore a slash separates parents

from their children. For example, the following are valid

paths of lengths 1, 2, 2, 3,

and 3 levels respectively:

Nodes can be inserted in any location. Nodes inserted after

but before

can be

represented as. Nodes inserted before

have the logical representation as a negative

number. For example, a node that comes before

can be represented as. Nodes

can't have leading zeros. For example,

is valid, but

isn't valid. To prevent

errors, insert nodes by using the

GetDescendant

method.

The

data type can be converted to other data types as follows:

Use the

ToString

method to convert the

value to the logical representation as

a

data type.

Use

Read (Database Engine) by using CSharp

and

Write

to convert

to.

To transmit

parameters through SOAP, first cast them as strings.

When a database is upgraded to a newer version of SQL Server, the new assembly and the

data type are automatically installed. Upgrade advisor rules detect any user type or

assemblies with conflicting names. The upgrade advisor advises renaming of any conflicting

assembly, and either renaming any conflicting type, or using two-part names in the code to

refer to that preexisting user type.

If a database upgrade detects a user assembly with conflicting name, it automatically renames

that assembly and put the database into suspect mode.

```sql
/
/1/
/0.3.-7/
/1/3/
/0.1/0.2/
```

```sql
/1/2/
```

```sql
/1/3/
```

```sql
/1/2.5/
```

```sql
0
```

```sql
/1/1/
```

```sql
/1/-1/
```

```sql
/1/1.1/
```

```sql
/1/1.01/
```
