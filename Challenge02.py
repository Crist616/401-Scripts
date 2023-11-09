#ping
import os
import time
from datetime import datetime

import ping3


DEST_IP = "8.8.8.8"

while True:
    response = ping3.ping(DEST_IP)
    status = "success" if response.is_alive else "failure"
    
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{timestamp} {DEST_IP}: {status}")
    
    time.sleep(2)