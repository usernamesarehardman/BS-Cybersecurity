import re
import os
import random
from datetime import datetime

def generate_private_ip():
    return f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"

def process_file(filename, log_file):
    ipv4_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    mac_pattern = re.compile(r'96:49:18:8A:D6:B9', re.IGNORECASE)
    
    with open(filename, 'r') as file:
        content = file.read()
    
    original_ips = ipv4_pattern.findall(content)
    modified_content = ipv4_pattern.sub(lambda _: generate_private_ip(), content)
    mac_found = bool(mac_pattern.search(content))
    
    with open(filename, 'w') as file:
        file.write(modified_content)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] Processed {filename}\n"
    for orig_ip in original_ips:
        log_entry += f"Replaced {orig_ip} -> {generate_private_ip()}\n"
    if mac_found:
        log_entry += "MAC address found in file!\n"
    log_entry += "\n"
    
    with open(log_file, 'a') as log:
        log.write(log_entry)
    
    return modified_content

def main():
    config_dir = "./h0data"  # Directory containing configuration files
    log_file = "./transaction_log.txt"
    
    if not os.path.exists(config_dir):
        print("Configuration directory not found!")
        return
    
    for filename in os.listdir(config_dir):
        if filename.endswith(".txt") or filename.endswith(".conf"):
            filepath = os.path.join(config_dir, filename)
            process_file(filepath, log_file)
    
    print("Processing complete. Check transaction_log.txt for details.")

if __name__ == "__main__":
    main()