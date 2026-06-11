---
name: "sys.remote_service_bindings"
title: "sys.remote_service_bindings"
category: "compatibility"
description: "This catalog view contains a row per remote service binding."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

This catalog view contains a row per remote service binding. Name of this remote service binding. Not NULLABLE. ID of this remote service binding. Not NULLABLE. ID of the database principal that owns this remote service Name of the remote service that this binding applies to. ID of the contract that this binding applies to. A value of 0 is a wildcard that means this binding applies to all contracts for the service. Not NULLABLE.

## Permissions

Article • 02/28/2023 Applies to: SQL Server This catalog view contains a row per remote service binding. Description Name of this remote service binding. Not NULLABLE. ID of this remote service binding. Not NULLABLE. ID of the database principal that owns this remote service binding. NULLABLE. Name of the remote service that this binding applies to. NULLABLE. ID of the contract that this binding applies to. A value of 0 is a wildcard that means this binding applies to all contracts for the service. Not NULLABLE. ID for the user specified in the remote service binding. Service Broker uses a certificate owned by this user for communicating with the specified service on the specified contracts. NULLABLE. This remote service binding uses ANONYMOUS security. The identity of the user that begins the conversation is not provided to the target service. Not NULLABLE. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . ﾉ Expand table
