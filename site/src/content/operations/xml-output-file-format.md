---
title: "XML Output File Format"
topic: "ssb-diagnose"
description: |
  Applies to:

  SQL Server

  The

  utility delivers its output as an XML file when you run it with the

  switch.

  The XML output file lists header information and the errors that it found in the Service Bro
tags:
  - "ssb-diagnose"
  - "xml-output-file-format"
pubDate: 2025-12-01
---

SQL Server

The

utility delivers its output as an XML file when you run it with the

switch.

The XML output file lists header information and the errors that it found in the Service Broker

configuration or conversation that was analyzed. You can write an application to analyze or

report on the errors listed in the file. Or, you can view the XML file in a general XML editor,

such as XML Notepad.

An

output file contains a

root element with two child

types:

A

element with header information.

An

element for each issue that is reported by.

DiagnosticInformation element (ssbdiagnose)

Banner element (ssbdiagnose)

Issue element (ssbdiagnose)

ssbdiagnose Utility (Service Broker)

```cmd
-XML
DiagnosticInformation
Banner
Issue
```
