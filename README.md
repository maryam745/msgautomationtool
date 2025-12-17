# WhatsApp Message Scheduler README

## 📌 Project Overview
Python-based WhatsApp message scheduler using Twilio API. Users input recipient details, message, and future date/time; program calculates delay, waits, then auto-sends the message.

## 🎯 Key Features
- Schedule WhatsApp messages for specific future datetime
- User-friendly console input with validation
- Automatic delay calculation using `time.sleep()`
- Error handling for past dates and API issues
- Real-world automation for reminders/birthdays

## 🛠️ Technologies
- Python 3.x
- Twilio API (`pip install twilio`)
- `datetime` for scheduling
- `time` for delays

## ⚙️ Prerequisites & Setup
1. Create free Twilio account at twilio.com/console
2. Enable WhatsApp Sandbox: Messaging > Try it out > WhatsApp
3. Note your Account SID, Auth Token, and Sandbox number (whatsapp:+14155238886)
4. Join Sandbox: Text "join [code]" (e.g., "join calm-lizard") from your WhatsApp to sandbox number
5. Install: `pip install twilio`

## 📝 Configuration
Edit `msgautomation.py`:
```python
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
from_ = 'whatsapp:+14155238886'  # Sandbox number
```

## 🚀 Usage
```bash
python msgautomation.py
```
Enter:
- Recipient name
- WhatsApp number (+country code, e.g., +923001234567)
- Message text
- Date (YYYY-MM-DD, e.g., 2025-12-17)
- Time (HH:MM 24hr, e.g., 14:30)

Program validates future time, shows countdown, sends automatically.

## ⏰ Example
```
Recipient: Alice
Number: +923001234567
Message: Happy Birthday! 🎉
Date: 2025-12-25
Time: 09:00
```
Waits ~1 week, then delivers.

## ⚠️ Limitations
- Blocks terminal (use `nohup` or screen for long delays)
- Single message only
- Sandbox expires (24hr join required)
- Internet required

## 🔧 Troubleshooting
- **Past time error**: Use future datetime only
- **API fail**: Check credentials, sandbox join
- **Number format**: Must be E.164 (+923001234567)
- **No delivery**: Verify recipient joined sandbox

## 🚀 Enhancements
- GUI with Flet
- Multiple schedules (threading/APScheduler)
- Database logging
- FastAPI web interface
- Android integration (Kotlin bridge)

## 📄 License
MIT License - Free to use/modify.

👨‍💻 Author: Maryam Nazar  
Computer Science Student | Python Automation Enthusiast  
17 Dec 2025
