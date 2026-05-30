---
name: "DML)"
title: "DML)"
category: "statements"
description: "Azure SQL Managed Instance"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

### xml

### insert

### delete

### replace value of

### xml

### xml

### modify()

### xml,

### xmlns

### xmlns:\*

### xml:base

### xml

### xsi:nil

### xsi:type

### xml

### xml:base

### xml

### xsi:nil

### xml

### xml

### xs:type

### xml

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The XML Data Modification Language (XML DML) is an extension of the XQuery language. As

defined by W3C, the XQuery language lacks the Data Manipulation (DML) part. The XML DML

introduced in this topic, and also the XQuery language, provides a fully functional query and

data-modification language that you can use against the

data type.

The XML DML adds the following case-sensitive keywords to XQuery:

As described in

XML Data Type and Columns (SQL Server)

, you can create variables and

columns of the

type and assign XML documents or fragments to them. To modify or

update these XML instances, do the following:

Use the

modify() Method xml Data Type)

of the

data type.

Specify the appropriate XML DML statements inside the

method.

Note that there are some attributes that cannot be inserted, deleted, or have their value

modified. For example:

For typed or untyped

the attributes are

,

, and

.

For typed

only, the attributes are

, and

.

Other restrictions include the following:

For typed or untyped

, inserting the attribute

will fail.

For typed

, deleting and modifying the

attribute will fail. For untyped

, you

can delete the attribute or modify its value.

For typed

, modifying the value of the

attribute will fail. For untyped

, you

can modify the attribute value.

When you modify a typed XML instance, the final format must be a valid instance of that type.

Otherwise, a validation error is returned.

insert (XML DML)

delete (XML DML)

replace value of (XML DML)

Compare Typed XML to Untyped XML

Create Instances of XML Data

xml Data Type Methods

See Also
