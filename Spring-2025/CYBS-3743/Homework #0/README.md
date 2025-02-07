# Regular Expression Assignment - CYBS 3743

## Due Date: February 6, 2025

## Overview
This assignment focuses on utilizing regular expressions in Python to process configuration files by identifying and replacing IPv4 addresses, logging transactions, and detecting specific MAC addresses.

## Objectives
1. Read all configuration files
2. Find all IPv4 addresses in each configuration file
3. Replace it with Class C private IP address
4. Create a log file for each transaction with a time stamp
5. <Extra> find a configuration file, which contains MAC address 96:49:18:8A:D6:B9
Please submit your script file, log file, and running result (screen shot on your environment) with
a brief explanation.

## Repository Structure
```
📁 CYBS_3743_Regex_Assignment
├── 📁 h0data                   # Folder containing configuration files
│   ├── ⚙️ <Number>.conf        # Assortment of configuration files
│   └── ...
├── 📄 CYBS_3743_H0.docx        # Word document containing assignment instructions
├── 📄 find_replace_ip_log.py   # Python script for processing files
├── 📄 README.md                # This document
└── 📄 transaction_log.txt      # Log file recording modifications
```

## Implementation Details
### `find_replace_ip_log.py`
- Reads all text-based configuration files (`.txt`, `.conf`) from `h0data/`.
- Uses regular expressions to:
  - Identify IPv4 addresses and replace them with `192.168.x.x`.
  - Detect occurrences of the MAC address `96:49:18:8A:D6:B9`.
- Creates or appends logs to `transaction_log.txt`.
- Outputs logs with timestamps and records replaced IP addresses.

### `transaction_log.txt`
- Records processed files.
- Lists each replaced IP address.
- Logs the timestamp of each transaction.
- Flags files containing the specified MAC address.

## How to Run the Script
1. Ensure Python is installed on your system.
2. Place configuration files inside the `h0data/` directory.
3. Run the script using:
   ```bash
   python find_replace_ip_log.py
   ```
4. Check `transaction_log.txt` for results.

## Example Output (Log File)
```
[2025-02-06 10:15:30] Processed h0data/config1.txt
Replaced 203.0.113.45 -> 192.168.25.78
Replaced 198.51.100.12 -> 192.168.10.34
MAC address found in file!
```

## References  
1. GeeksforGeeks. (12 Apr, 2024). *Regex Tutorial – How to Write Regular Expressions*. Retrieved from [https://www.geeksforgeeks.org/write-regular-expressions/](https://www.geeksforgeeks.org/write-regular-expressions/)  
2. YouTube. (Jul 25, 2023). *Regular Expression Methods in Python*. Retrieved from [https://www.youtube.com/watch?v=EzeeypMKx7o](https://www.youtube.com/watch?v=EzeeypMKx7o)  
3. ChatGPT. (2025). *Content partially generated using OpenAI's ChatGPT-4o. Retrieved from OpenAI API.