# Python Keylogger Monitoring Lab with Email Reporting

Educational cybersecurity project demonstrating keyboard event monitoring and automated email reporting using Python.

## ⚠️ Disclaimer

This project is intended strictly for:

- Educational purposes
- Authorized penetration testing
- Defensive cybersecurity research
- Controlled lab environments
- Security awareness demonstrations

Do NOT use this software on devices, networks, or systems without explicit written authorization.

The author assumes no responsibility for misuse or damage caused by this project.

---

# Features

- Keyboard event monitoring
- Local keystroke logging
- Automated email reporting
- Multi-threaded background processing
- File logging support
- Python SMTP integration
- Security research demonstration

---

# Technologies Used

- Python 3
- pynput
- smtplib
- threading

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/keyboard-monitor-lab.git
```

## Navigate Into the Project

```bash
cd keyboard-monitor-lab
```

## Install Dependencies

pip install -r requirements.txt

---

# Requirements

Create a `requirements.txt` file:

pynput

---

# Email Configuration

Update the following variables in the script:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TARGET_EMAIL = "receiver@gmail.com"
```

## Gmail App Password Setup

Google blocks normal passwords for SMTP access.

Use a Gmail App Password instead:

1. Enable 2-Step Verification
2. Go to Google Account Settings
3. Generate an App Password
4. Use the generated password in the script

---

# Running the Program

python keylogger.py


Press `ESC` to stop the program safely.

---

# Educational Objectives

This project demonstrates:

- Keyboard input monitoring concepts
- Email automation using SMTP
- Event listeners in Python
- File handling
- Multi-threading
- Security awareness concepts

---

# Ethical Usage

This project should only be used:

- In virtual labs
- In sandbox environments
- During authorized penetration tests
- For cybersecurity education

Unauthorized deployment may violate:
- Privacy laws
- Computer crime legislation
- Institutional policies

---

# Future Improvements

- Encrypted logging
- Secure credential storage
- Detection engineering module
- SIEM integration
- Docker deployment
- Linux persistence simulation (lab only)

---

# Screenshots

Add screenshots here showing:
- Program execution
- Log file generation
- Email reporting
- Test lab setup

---



