# 🚀 QuickStrike v2 – Fast Recon & Port Scanner

QuickStrike v2 is a lightweight, fast, multi-threaded reconnaissance tool built for ethical hackers, bug bounty hunters, and cybersecurity learners.
It focuses on speed, simplicity, and clean output while providing essential recon features used in real-world assessments.

⚠️ Use only on systems you own or have explicit permission to test.

## ✨ Features

⚡ Multi-threaded port scanning (very fast)

🎯 Custom port range scanning

🧠 Automatic service detection

📄 Save scan results to file

🐧 Works on Linux / Kali Linux / Termux


### 🚀 Installation
```
git clone https://github.com/Nivas-cyber/Quickstrike.git
```
```
cd quickstrike
```
```
chmod +x quickstrike_v2.py
```

### ▶ Usage
```
python3 quickstrike_v2.py <target> <start_port> <end_port>
```
### Example
```
python3 quickstrike_v2.py example.com 1 1000
```

### 🧠 How It Works

* Resolves domain to IP address

* Performs multi-threaded TCP port scanning

* Identifies common services

* Attempts banner grabbing for fingerprinting

* Saves results in a timestamped report file

### 🔐 Legal Disclaimer

* This tool is created strictly for educational and ethical security testing.

* You are responsible for your actions.
* Unauthorized scanning or attacking systems without permission is illegal.
