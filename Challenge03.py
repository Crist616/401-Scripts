#!/usr/bin/python3
import ping3
import datetime
import time
import smtplib
from email.mime.text import MIMEText

def send_email(sender, password, recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()

email = input("Enter your email: ")
password = input("Enter your password: ")

DEST_IP = "192.168.1.100" #any ip (without multiping)
prev_status = None

while True:
    response = ping3.ping(DEST_IP)
    status = "down" if response is None else "up"
    print(f"Current status: {status}")  # print the current status

    if prev_status is not None and status != prev_status:
        timestamp = datetime.datetime.now()
        subject = f"Host status changed: {DEST_IP}"
        body = f"Previous status: {prev_status}\nNew status: {status}\nTimestamp: {timestamp}"
        send_email(email, password, 'burneronetwoone11@gmail.com', subject, body)
        print("Email sent")  # print a message when an email is sent

    prev_status = status
    time.sleep(1)
