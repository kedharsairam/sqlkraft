---
name: "sys.database_mirroring_endpoints"
title: "sys.database_mirroring_endpoints"
category: "compatibility"
description: "Returns one row for the database mirroring endpoint of an instance of SQL Server. Note: This value is relevant only for database mirroring. Description of mirroring role, one of: Note: This value is relevant only for database mirroring. The database mirroring endpoint supports both sessions between database mirroring partners and with witnesses and sessions between the primary replica of an Always"
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  <witness_option>
      ::=
      WITNESS
      { =
      'witness_server'
      |
      OFF
      }
---

## Description

Returns one row for the database mirroring endpoint of an instance of SQL Server. Note: This value is relevant only for database mirroring. Description of mirroring role, one of: Note: This value is relevant only for database mirroring. The database mirroring endpoint supports both sessions between database mirroring partners and with witnesses and sessions between the primary replica of an Always On

## Syntax

```sql
<witness_option>
::=
WITNESS
{ =
'witness_server'
|
OFF
}
```

## Arguments

database_name

Is the name of the database to be modified.

PARTNER <partner_option> Controls the database properties that define the failover partners

of a database mirroring session and their behavior. Some SET PARTNER options can be set on

either partner; others are restricted to the principal server or to the mirror server. For more

information, see the individual PARTNER options that follow. A SET PARTNER clause affects

both copies of the database, regardless of the partner on which it is specified.

To execute a SET PARTNER statement, the STATE of the endpoints of both partners must be set

to STARTED. Note, also, that the ROLE of the database mirroring endpoint of each partner

server instance must be set to either PARTNER or ALL. For information about how to specify an

endpoint, see

Create a Database Mirroring Endpoint for Windows Authentication. To learn the

role and state of the database mirroring endpoint of a server instance, on that instance, use the

following Transact-SQL statement:

A SET PARTNER or SET WITNESS command can complete successfully when entered, but

fail later.

ALTER DATABASE database mirroring options are not available for a contained database.

For more information, see

Possible Failures During Database Mirroring

WITNESS <witness_option> Controls the database properties that define a database mirroring

witness. A SET WITNESS clause affects both copies of the database, but you can specify SET

WITNESS only on the principal server. If a witness is set for a session, quorum is required to

serve the database, regardless of the SAFETY setting; for more information, see

Quorum: How a

Witness Affects Database Availability - Database Mirroring

We recommend that the witness and failover partners reside on separate computers. For

information about the witness, see

Database Mirroring Witness

To execute a SET WITNESS statement, the STATE of the endpoints of both the principal and

witness server instances must be set to STARTED. Note, also, that the ROLE of the database

mirroring endpoint of a witness server instance must be set to either WITNESS or ALL. For

information about specifying an endpoint, see

The Database Mirroring Endpoint

To learn the role and state of the database mirroring endpoint of a server instance, on that

instance, use the following Transact-SQL statement:

witness_server

Specifies an instance of the Database Engine to act as the witness server for a

database mirroring session. You can specify SET WITNESS statements only on the principal

In a SET WITNESS

witness_server

statement, the syntax of

witness_server

is the same as the

partner_server

OFF Removes the witness from a database mirroring session. Setting the witness to OFF

disables automatic failover. If the database is set to FULL SAFETY and the witness is set to OFF,

Database properties cannot be set on the witness.

Only one <witness_option> is permitted per SET WITNESS clause.
