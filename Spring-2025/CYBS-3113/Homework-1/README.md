# Homework-1

## Due Date: February 8, 2025

## Overview
This assignment focuses on analyzing CPU scheduling policies by running `process-run.py` and observing the impact on process execution order, completion time, and CPU utilization.

## Objectives
1. Run `process-run.py` with different scheduling policies.
2. Evaluate CPU utilization.
3. Compare completion times across policies.
4. Analyze process execution order.
5. Understand the effect of I/O completion and context switching.

For each numbered question (found in CYBS_3113_H1.docx), provide:

A numeric or yes/no answer (brief).
A 1–2 sentence justification referring to the trace details (-c or -p).

## Repository Structure
```
📁 Homework-1
├── 📄 CYBS_3113_H1.docx        # Word document containing assignment instructions
├── 📄 README.md                # This document
├── 📄 process-run.py           # Script for simulating CPU scheduling
└── 📄 results.txt              # Recorded results of the assignment
```

## Implementation Details
### `process-run.py`
- Simulates CPU scheduling for a list of processes.
- Supports multiple scheduling policies including FCFS, RR, SJF, and MLFQ.
- Outputs execution trace for analysis.

### `results.txt`
- Records results of the assignment

## References
1. ChatGPT. (2025). *Content partially generated using OpenAI's ChatGPT-4o*. Retrieved from OpenAI API.
2. Course Materials: CYBS 3113 Operating Systems Fundamentals, University of Oklahoma.