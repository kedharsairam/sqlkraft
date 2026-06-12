---
title: "Configure a Firewall"
topic: "filestream"
description: "To use FILESTREAM in a firewall-protected environment, both the client and server must be able to resolve DNS names to the server that contains the FI"
tags: ["filestream","configure-a-firewall"]
pubDate: 2025-12-01
---

To use FILESTREAM in a firewall-protected environment, both the client and server must be

able to resolve DNS names to the server that contains the FILESTREAM files. FILESTREAM

requires the Windows file-sharing ports 139 and 445 to be open.

1. In Control Panel, open.

2. In the left pane, click. If you're prompted for an administrator

password or confirmation, type the password or provide confirmation.

3. In the

dialog box, in the left pane, click

, and then, in the right pane, click.

4. Follow the instructions in the New Inbound Rule wizard to add TCP port 139.

5. Repeat the previous step to add TCP port 445.

6. Close the

dialog box.
