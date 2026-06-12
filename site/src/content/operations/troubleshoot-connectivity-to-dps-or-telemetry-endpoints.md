---
title: "Troubleshoot connectivity to DPS or telemetry endpoints"
topic: "azure-synapse"
description: |
  06/30/2025

  Applies to:

  SQL Server

  In addition to the usual endpoints, the Azure Arc extension for SQL Server connects to two

  other endpoints:

  Data processing service (DPS) endpoint

  The collected
tags:
  - "azure-synapse"
  - "troubleshoot-connectivity-to-dps-or-telemetry-endpoints"
pubDate: 2025-12-01
---

06/30/2025

SQL Server

In addition to the usual endpoints, the Azure Arc extension for SQL Server connects to two

other endpoints:

Data processing service (DPS) endpoint

The collected inventory information about SQL Server instances, databases, availability

groups, and usage data for billing purposes is sent to this endpoint.

Telemetry endpoint

The Azure Connected Machine agent logs, the Azure extension for SQL Server logs, and

the Dynamic Management Views (DMV) data is sent to this endpoint.

Communication to these endpoints uses HTTPS with SSL/TLS and port TCP/443 for encrypted

secure connections. The agent initiates communication to

send

the data

to

Azure. Azure never

initiates communication. Connectivity to these endpoints is therefore only one way.

When communication to these endpoints is blocked, the service has the following symptoms:

You don't see SQL Server instances in the Azure portal. DPS endpoint is blocked.

You don't see data in the SQL Server instance performance dashboards view. If DPS

endpoint is unblocked but the telemetry endpoint is blocked.

You see an error in the Azure extension for SQL Server status in the Azure portal. Review

Check the Azure Extension for SQL Server status in the Azure portal.

You see an error in the Azure extension for SQL Server log. Review

Check the Azure

Extension for SQL Server logs.

You can view the current state of the Azure extension for SQL Server in the portal. The status is

refreshed every 15 minutes.

Healthy state:
