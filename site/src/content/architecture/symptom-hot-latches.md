---
title: "Symptom: Hot latches"
topic: "latch-contention"
description: "The following diagram details the hardware used to test the point of sales system:"
tags: ["latch-contention","architecture"]
pubDate: "2026-05-29"
---

The following diagram details the hardware used to test the point of sales system:

In this case, we observed high waits for

where we typically define high as an

average of more than 1 ms. In this case, we consistently observed waits exceeding 20 ms.

`PAGELATCH_EX`
