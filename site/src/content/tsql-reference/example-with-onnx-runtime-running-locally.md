---
name: "Example with ONNX Runtime running locally"
title: "Example with ONNX Runtime running locally"
category: "queries"
description: ""
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

## Security considerations

This example creates an external model of the

type using the OpenAI

and HTTP header based credentials for authentication.

ONNX Runtime

is an open-source inference engine that allows you to run machine learning

models locally, making it ideal for integrating AI capabilities into SQL Server environments.

This example guides you through setting up SQL Server 2025 (17.x) with ONNX Runtime to

enable local AI-powered text embedding generation. It only applies on Windows.

）

Important

This feature requires that

Machine Learning Services

is installed.

### Implement strong access controls

### Monitor and audit access

### Conduct regular security assessments

## Step 1: Enable developer preview features on SQL Server 2025

## Step 2: Enable the local AI runtime on SQL Server 2025

You can use the AI Runtime Host feature to configure and use your own LLMs and ONNX

libraries with SQL Server. Because Microsoft does not validate or monitor third-party models

and libraries, you are responsible for selecting appropriate models and libraries, filtering

content, securing the runtime, and ensuring compliance with any applicable policies and

regulations.

To mitigate these risks, consider the following security best practices:

: Ensure that only authorized users have access to

sensitive data and ONNX Runtime models. Validate all models before loading them into

SQL Server. Use the

principle of least privilege

, as well as database roles and privileges.

: Regularly monitor and audit access to the database and

function calls to detect suspicious activity.

: Perform vulnerability scans and security reviews to

identify and mitigate potential risks.

Run the following Transact-SQL (T-SQL) command to enable SQL Server 2025 (17.x) preview

features in the database you would like use for this example:

Enable external AI runtimes by running the following T-SQL query:

Ｕ

Caution

A malicious or compromised ONNX model could exfiltrate data or execute unauthorized

code. Only use models from trusted, verified sources.

#### PowerShell

#### PowerShell

## Step 3: Set up the ONNX Runtime library

## Step 4: Set up the tokenization library

### tokenizers_cpp.dll

## Step 5: Download the ONNX model

Create a directory on the SQL Server instance to hold the ONNX Runtime library files. In this

example,

is used.

You can use the following commands to create the directory:

Next, download a version of

ONNX Runtime

(1.19 or greater) that's appropriate for your

operating system. After unzipping the download, copy the

(located in the lib

directory) to the

directory that was created.

Download and build

the tokenizers-cpp library

from GitHub. Once the dll is created, place

the tokenizer in the

directory.

Start by creating the

directory in.

This example uses the

model, which can be downloaded from

Hugging

Face.

Clone the repository into the

directory with the following

git

command:

７

Note

Ensure the created dll is named

#### Console

#### PowerShell

### The 'PARAMETERS' value used here is a placeholder needed for SQL Server 2025 (17.x).

## Step 6: Set directory permissions

## Step 7: Create the external model

If not installed, you can download git from the following

download link

or via winget (winget

install Microsoft.Git)

Use the following PowerShell script to provide the MSSQLLaunchpad user access to the ONNX

Runtime directory:

Run the following query to register your ONNX model as an external model object:

should point to the directory containing

and

files.

should point to directory containing

and

files.

#### Output

## Step 8: Generate embeddings

## Enable XEvent system logging

Use the

function to test the model by running the following query:

This command launches the

, load the required DLLs, and processes the input

text.

The result from the previous query is an array of embeddings:

Run the following query to enable system logging for troubleshooting.

Next, use this query see the captured system logs:

#### PowerShell

## Clean up

To remove the external model object, run the following T-SQL statement:

To remove the directory permissions, run the following PowerShell commands:

Finally, delete the

directory.

ALTER EXTERNAL MODEL (Transact-SQL)

DROP EXTERNAL MODEL (Transact-SQL)

AI_GENERATE_EMBEDDINGS (Transact-SQL)

AI_GENERATE_CHUNKS (Transact-SQL)

sys.external_models

Create and deploy an Azure OpenAI in Azure AI Foundry Models resource
