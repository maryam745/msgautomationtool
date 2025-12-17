WhatsApp Message Scheduler (Python + Twilio)
📌 Project Overview

This project is a Python-based WhatsApp message scheduler.
It allows a user to send a WhatsApp message at a specific future date and time using the Twilio API.

Conceptually, the program:

Takes user input → calculates delay → waits → sends message automatically.

🎯 Key Features

Send WhatsApp messages programmatically

Schedule messages for a future date & time

User-friendly input system

Error handling for invalid time or API issues

Real-world automation use case

🧠 Core Concept

Computers cannot “wait for a date” directly.
So this program:

Converts date & time into seconds

Calculates how many seconds remain

Pauses execution using sleep()

Sends the message at the exact moment

This is the foundation of task scheduling.

🛠 Technologies Used

Python

Twilio API

datetime module (date & time handling)

time module (execution delay)

📂 Project Structure
msgautomation.py
README.md

⚙️ Prerequisites

Before running the project, make sure you have:

Python 3.x installed

A Twilio account

WhatsApp Sandbox enabled in Twilio

Required library installed:

pip install twilio

🔐 Twilio Configuration

Update the following credentials in the code:

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
from_ = 'whatsapp:+14155238886'  # Twilio sandbox number

▶️ How to Run the Program

Open terminal / command prompt

Run the script:

python msgautomation.py


Enter:

Recipient name

WhatsApp number with country code

Message text

Date (YYYY-MM-DD)

Time (HH:MM, 24-hour format)

⏰ Correct Time Format

✅ Correct:

2025-12-17
12:36


❌ Incorrect:

12-36


Reason:
Python strictly follows the format %H:%M.

🚫 Validation Rule

If the scheduled time is in the past → message will NOT be sent.

This prevents logical errors.

📌 Example Use Case

Birthday wishes

Exam reminders

Meeting notifications

Automated alerts

⚠️ Limitations

Uses blocking sleep() (program must stay running)

Sends one message at a time

Requires active internet connection

🚀 Future Improvements

Multiple message scheduling

Background scheduling (cron / task scheduler)

GUI or web interface

Message logs & history

👨‍💻 Author

 Maryam Nazar
Computer Science Student
Python Automation Enthusiast
