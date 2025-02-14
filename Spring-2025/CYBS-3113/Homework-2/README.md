# Homework-2

## Due Date: February 15, 2025

## Overview
This assignment focuses on analyzing CPU scheduling policies (FIFO, SJF, and RR) through manual calculations and verifying results using a Python-based scheduler simulation.

## Objectives
1. Predict execution order based on different scheduling policies.
2. Compute Response Time, Turnaround Time, and Wait Time for each job.
3. Compare the efficiency of different scheduling algorithms.
4. Verify manual calculations against simulation results.
5. Analyze the impact of time quantum on Round Robin scheduling.

For each part (FIFO, SJF, RR), provide:
- Manually calculated Response Time, Turnaround Time, and Wait Time.
- Execution order prediction.
- Comparison of manual results with simulation output.
- Explanation of any discrepancies.

## Repository Structure
```
📁 Homework-2
├── 📁 calculations             # Folder containing scanned/manual calculations
|   └── ...
├── 📄 CYBS_3113_H2.docx        # Word document containing assignment instructions
├── 📄 README.md                # This document
├── 📄 scheduler.py             # Python script for scheduling simulation
└── 📄 results.txt              # Recorded results and reflections
```

## Implementation Details
### `scheduler.py`
- Simulates FIFO, SJF, and RR scheduling for a set of 4 jobs.
- Outputs execution trace, response time, turnaround time, and wait time.
- Supports the `-c` flag for verifying manual results.

### `results.txt`
- Records manual calculations and comparisons with simulation results.
- Includes explanations for any discrepancies.

### `calculations/`
- Contains photos or scanned copies of handwritten calculations.
- Clearly labeled for FIFO, SJF, and RR scheduling.

## Commands to Run
```bash
# FIFO Scheduling
type ./scheduler.py -p FIFO -j 4 -s 99

# SJF Scheduling
type ./scheduler.py -p SJF -j 4 -s 99

# Round Robin Scheduling
type ./scheduler.py -p RR -j 4 -s 99 -q 3
```

## References
1. ChatGPT. (2025). *Content partially generated using OpenAI's ChatGPT-4o*. Retrieved from OpenAI API.
2. Course Materials: CYBS 3113 Operating Systems Fundamentals, University of Oklahoma.
