# wireshark-http-analysis
This project captures HTTP traffic using Wireshark and extracts visited URLs using a Python script with the pyshark library.

# Prerequisites
Wireshark installed on your system
Python 3.6 or later
pyshark library

# Installation
Install the pyshark library with:
**$ pip install pyshark**
       ~**geting an error: externally managed environment** 
       The error you're seeing — "externally managed environment" — typically occurs when trying to use pip install inside system-managed Python environments, such as those used by Linux distributions like Ubuntu, Debian, or even on macOS with system Python. This is a safety feature to prevent breaking system tools.
**Use $sudo apt install python3-pyshark**  
<img width="956" height="1092" alt="Screenshot 2025-07-29 141637" src="https://github.com/user-attachments/assets/5f0dca10-be20-4721-9ae9-93e8df50e131" />

      
# How to Replicate
# Capturing Traffic
Open Wireshark and select your active network interface (e.g., Wi-Fi or Ethernet).
       **$wireshark** 
Click the green "Start" button to begin capturing traffic.
Open a web browser and visit some websites to generate HTTP traffic.
<img width="958" height="1279" alt="Screenshot 2025-07-29 141714" src="https://github.com/user-attachments/assets/3761780c-1771-48e7-b730-e03006e8c253" />

# Stop Capture
After a few minutes, click the red "Stop" button to stop capturing.
# save capture
Save the capture file as http_traffic.pcap (or any name you prefer).

**Note:** You may need to run Wireshark with administrative privileges to capture traffic.

# Running the Script
Place the extract_urls.py script in the same directory as your capture file.
Open a terminal and navigate to that directory.
<img width="964" height="1278" alt="Screenshot 2025-07-29 155640" src="https://github.com/user-attachments/assets/d5c9d80e-6d2a-4ce1-92b5-f2bea66a078c" />

**Run the script with**:

python extract_urls.py http_traffic.pcap

The script will generate a urls.txt file containing the extracted URLs.

Note: This repository does not include a capture file. You need to capture your own HTTP traffic as described above.
**Example Output**

**After running the script, urls.txt will contain something like:**

Extracted URLs:
1. http://example.com/
2. http://wikipedia.org/wiki/Main_Page
3. http://google.com/search?q=wireshark


# How It Works

The Python script uses the pyshark library to read the capture file and filter for HTTP packets. It extracts the host and request URI from each HTTP request packet to construct the full URL. The URLs are then deduplicated and written to urls.txt.

# Disclaimer

**This project is for educational purposes only. Ensure you have permission to capture and analyze traffic on your network. Do not capture sensitive or personal data without consent.**

# Daniel Yewenu
