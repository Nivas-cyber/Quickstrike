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



### 🧠 Learning Purpose

QuickStrike is designed to help learners:

* Understand how port scanners work internally

* Learn multi-threading in Python

* Practice real bug bounty recon techniques

* Build confidence before advanced tools (nmap, masscan)

### 👨‍💻 Author

cyber_specterz https://www.instagram.com/cyber_specterz?igsh=bThuNzd4ZjQ1M3B1

Cybersecurity Education & Ethical Hacking
📍 India

“Learn how tools work — don’t just run tools.”

### ⭐ Support

If you like this project:

* ⭐ Star the repository

* 🍴 Fork it

* 🛠️ Improve it

* 📢 Share with learners

### 🏁 Final Note

QuickStrike v2 is not a replacement for nmap.
It is a learning-focused recon engine that teaches you how real tools are built.
