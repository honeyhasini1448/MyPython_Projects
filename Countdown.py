# Simple TimeCountdown , import time to use inbuilt { time.sleep() }

import time 
My_time = int(input("Enter time in seconds to countdown:  "))  
                                                                          
for i in range(My_time,0,-1):
    seconds = i % 60 
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up!")