---
title: "Ownership Chains & Context Switching"
topic: "configuration"
description: |
  Article

  •

  08/10/2023

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This tutorial uses a scenario to illustrate SQL Server security concepts involving ownership

  chains and user context switc
tags:
  - "configuration"
  - "ownership-chains-context-switching"
pubDate: 2025-12-01
---

Article

•

08/10/2023

SQL Server

Azure SQL Managed Instance

This tutorial uses a scenario to illustrate SQL Server security concepts involving ownership

chains and user context switching.

In this scenario, two users need accounts to access purchase order data stored in the

database. The requirements are as follows:

The first account (TestManagerUser) must be able to see all details in every purchase

order.

The second account (TestEmployeeUser) must be able to see the purchase order number,

order date, shipping date, product ID numbers, and the ordered and received items per

purchase order, by purchase order number, for items where partial shipments have been

received.

All other accounts must retain their current permissions.

To fulfill the requirements of this scenario, the example is broken into four parts that

demonstrate the concepts of ownership chains and context switching:

1. Configuring the environment.

2. Creating a stored procedure to access data by purchase order.

3. Accessing the data through the stored procedure.

4. Resetting the environment.

Each code block in this example is explained in line. To copy the complete example, see

Complete Example

at the end of this tutorial.

７

Note

To run the code in this tutorial you must have both Mixed Mode security configured and

the

database installed. For more information about Mixed Mode

security, see.

```cmd
AdventureWorks2022
AdventureWorks2022
```
