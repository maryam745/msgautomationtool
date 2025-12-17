"""
twilio
datetime module
time

"""

"""
1. Twilio client setup
2. User input
3. scheduling logic
4. send message
"""


# Setp 1: Required libraries
from twilio.rest import Client
from datetime import datetime,timedelta
import time

# Step 2: Twilio Credentials
account_sid='dummy accountSID'
auth_token='dummy auth token'

client=Client(account_sid, auth_token)

#step 3: message send function
def send_msg_whattsapp(recipient_number,msg_body):
    try:
        msg= client.messages.create(
            from_='whatsapp:+1111111111',
            body=msg_body,
            to=f"whatsapp:{recipient_number}"
        )
        print(f"Message sent sucessfully!! MEssage_SID:{msg.sid}")

    except Exception as e:
        print("An error Occured ")

# Step 4:USer input
name=input("Enter the recipent name: ")
recipient_number=input("Enter the recipient whatsapp number with country code e.g(+923.......):  ")
msg_body=input(f"Enter the message you want to end to {name}: ")

# Step 5: Datetime and Calculate Delay
date_str=input("Enter the date in {YYYY-MM-DD} : ")
time_str=input("Enter for sending message{HH:MM in 24 hours}: ")

#datetime

schedule_datetime = datetime.strptime(
    f"{date_str},{time_str}",
    "%Y-%m-%d,%H:%M"
)

current_datetime=datetime.now()

#calculaer difference
time_difference=schedule_datetime-current_datetime
delay_sec=time_difference.total_seconds()

if delay_sec <= 0:
    print("The specified time is in the past")
else:
    print(f'Message scheduled to be sent to {name}, at {schedule_datetime }')
    
    #wait until scheduled time
    time.sleep(delay_sec)

    #send the message
    send_msg_whattsapp(recipient_number,msg_body)