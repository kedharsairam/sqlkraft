---
name: 'sys.sp_describe_undeclared_parameters'
title: 'sp_describe_undeclared_parameters'
category: 'general'
description: 'For internal use. Not nullable. always returns status of zero. The most common use is when an application is given a Transact-SQL statement that might contain parameters and must process them in some way. An example is a user interface (such ) where the user provides a query with ODBC parameter syntax. The application must dynamically discover the number of parameters and prompt the user for Anoth'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_describe_undeclared_parameters
  [ @tsql = ]
  'Transact-SQL_batch'
  [ , [ @params = ]
  N
  '@parameter_name data_type [ , ... n ]'
  ]
---

## Description

For internal use. Not nullable. always returns status of zero. The most common use is when an application is given a Transact-SQL statement that might contain parameters and must process them in some way. An example is a user interface (such ) where the user provides a query with ODBC parameter syntax. The application must dynamically discover the number of parameters and prompt the user for Another example is when without user input, an application must loop over the parameters and obtain the data for them from some other location (such as a table). In this case, the application doesn't have to pass all the parameter information at once. Instead, the application can get all the parameters information from the provider and obtain the data itself from the table. Code using is more generic and is less likely to For internal use. Not nullable.

## Syntax

```sql
sp_describe_undeclared_parameters
[ @tsql = ]
'Transact-SQL_batch'
[ , [ @params = ]
N
'@parameter_name data_type [ , ... n ]'
]
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Returns only metadata to the client. Can be used to test the format of the response without actually running the query. Transact-SQL syntax conventions syntaxsql When is , a rowset is returned with the column names, but without any data rows. has no effect when the Transact-SQL batch is parsed. The effect occurs during execution run time. The default value is . Requires membership in the public role. ７ Note Do not use this feature. This feature has been replaced by the following items:

## Remarks

Description

For internal use. Not nullable.

always returns status of zero.

The most common use is when an application is given a Transact-SQL statement that might

contain parameters and must process them in some way. An example is a user interface (such

) where the user provides a query with ODBC parameter syntax.

The application must dynamically discover the number of parameters and prompt the user for

Another example is when without user input, an application must loop over the parameters

and obtain the data for them from some other location (such as a table). In this case, the

application doesn't have to pass all the parameter information at once. Instead, the application

can get all the parameters information from the provider and obtain the data itself from the

table. Code using

is more generic and is less likely to

require modification if the data structure changes later.

returns an error in any of the following cases.

isn't a valid Transact-SQL batch. Validity is determined by parsing and

analyzing the Transact-SQL batch. Any errors caused by the batch during query

optimization or during execution aren't considered when determining whether the

Transact-SQL batch is valid.

and contains a string that isn't a syntactically valid declaration string

for parameters, or if it contains a string that declares any parameter more than one time.

The input Transact-SQL batch declares a local variable of the same name as a parameter

declared in

The statement references temporary tables.

The query includes the creation of a permanent table that is then queried.

has no parameters, other than parameters declared in

, the procedure returns

an empty result set.

Description

For internal use. Not nullable.

always returns status of zero.

The most common use is when an application is given a Transact-SQL statement that might

contain parameters and must process them in some way. An example is a user interface (such

) where the user provides a query with ODBC parameter syntax.

The application must dynamically discover the number of parameters and prompt the user for

Another example is when without user input, an application must loop over the parameters

and obtain the data for them from some other location (such as a table). In this case, the

application doesn't have to pass all the parameter information at once. Instead, the application

can get all the parameters information from the provider and obtain the data itself from the

table. Code using

is more generic and is less likely to

require modification if the data structure changes later.

returns an error in any of the following cases.

isn't a valid Transact-SQL batch. Validity is determined by parsing and

analyzing the Transact-SQL batch. Any errors caused by the batch during query

optimization or during execution aren't considered when determining whether the

Transact-SQL batch is valid.

and contains a string that isn't a syntactically valid declaration string

for parameters, or if it contains a string that declares any parameter more than one time.

The input Transact-SQL batch declares a local variable of the same name as a parameter

declared in

The statement references temporary tables.

The query includes the creation of a permanent table that is then queried.

has no parameters, other than parameters declared in

, the procedure returns

an empty result set.
