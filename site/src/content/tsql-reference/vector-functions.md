---
name: "Vector functions"
title: "Vector functions"
category: "statements"
description: "SQL Server 2025 (17.x)"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

### vector

#### Function

### Always-up-to-date

### update policy

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed

Instance

SQL database in Microsoft Fabric

The following scalar functions perform operations on

vectors

in binary format, allowing

applications to store and manipulate vectors in the SQL Database Engine.

All vector functions support the

data type

.

## Description

VECTOR_DISTANCE

Calculates the distance between two vectors using a specified distance metric.

VECTOR_SEARCH

(preview)

Return the closest vectors to a given query vector and distance metric using an

approximate vector search algorithm.

VECTOR_NORM

Takes a vector as an input and returns the norm of the vector (which is a

measure of its length or magnitude) in a given

norm type

.

VECTOR_NORMALIZE

Takes a vector as an input and returns the normalized vector, which is a vector

scaled to have a length of 1 in a given

norm type

. Adjusts a vector so that its

length is normalized following the rules of specified norm type.

VECTORPROPERTY

## Returns specific properties of a given vector.

Vector data type

Vector search and vector indexes in the SQL Database Engine

Intelligent applications and AI

Last updated on 01/07/2026

７

Note

Vector features are available in Azure SQL Managed Instance with the

SQL Server 2025

or

.



Expand table

Related content
