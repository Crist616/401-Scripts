import ping3
import datetime
import time

DEST_IP = "8.8.8.8" 

while True:
    response = ping3.ping(DEST_IP)
    
    if response is None:
        status = "failure"
    else:
        status = "success" if response else "failure"

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{timestamp} {DEST_IP}: {status}")
    
    time.sleep(2)
