# Network Traffic Sniffer (Python + Scapy)

## Overview
A lightweight network traffic sniffer built using Python and Scapy. The tool captures live network packets from the system and saves them into a PCAP file for later analysis.

This tool captures live network packets for analysis and saves them in PCAP format for forensic inspection.

## Features
- Captures live network traffic using Scapy
- Stores captured packets in `.pcap` format
- Lightweight and easy to run in Visual Studio Code
- Useful for learning basic network monitoring and packet capture

## Tech Stack
- Python 3.x
- Scapy

## Installation

Install dependencies using:

```bash id="inst2"
pip install -r requirements.txt
Usage
Run the script in Visual Studio Code terminal or any command line:
python sniffer.py
Then generate network activity (browse websites, use apps, etc.).
Stop the script when done.
## Project Structure
- captured_traffic.pcap
- README.md
- requirements.txt
- sniffer.py
Output
•	captured_traffic.pcap → contains captured network packets 
•	Can be opened using any network packet analysis tool for inspection
Packet Analysis Insight
The generated .pcap file contains raw network traffic data that can be used for analysis of:
•	Source and destination IP addresses 
•	Protocol types (TCP, UDP, etc.) 
•	Packet sizes and timing information 
•	Network communication patterns 
This helps demonstrate how live network traffic can be captured and studied for cybersecurity learning and basic forensic understanding.
Use Cases
•	Network traffic monitoring 
•	Cybersecurity learning 
•	Basic packet capture and analysis 
•	Introductory digital forensics concepts
Disclaimer
This tool is intended for educational and ethical use only. Do not run it on networks without proper authorization.
Author
CodeAlpha Cyber security Internship task using Python and Scapy.
