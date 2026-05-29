---
title: "Coding"
topic: "clr-integration"
description: |
  Article
  
  •
  
  12/30/2024
  
  Applies to:
  
  SQL Server
  
  When coding your user-defined type (UDT) definition, you must implement various features,
  
  depending on whether you're implementing the UDT as a class 
tags:
  - "clr-integration"
  - "coding"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

When coding your user-defined type (UDT) definition, you must implement various features,

depending on whether you're implementing the UDT as a class or a structure, and on the

format and serialization options you choose.

The example in this section illustrates implementing a

UDT as a

(or

in

Visual Basic). The

UDT consists of X and Y coordinates implemented as property

procedures.

The following namespaces are required when defining a UDT:

C#

The

namespace contains the objects required for various

attributes of your UDT, and the

namespace contains the classes that

represent SQL Server native data types available to the assembly. There might be other

namespaces that your assembly requires in order to function correctly. The

UDT also

uses the

namespace for working with strings.

Attributes determine how serialization is used to construct the storage representation of UDTs

and to transmit UDTs by value to the client.

C#

７

Note

Visual C++ database objects, such as UDTs, compiled with

aren't supported for

execution.

```sql
Point
struct
Structure
Point
Microsoft.SqlServer.Server
System.Data.SqlTypes
Point
System.Text
using
System;
using
System.Data.SqlTypes;
using
Microsoft.SqlServer.Server;
/clr:pure
```