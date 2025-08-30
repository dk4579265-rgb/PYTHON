import time


waite_time =1
max_retries =5
attempts =0


while attempts < max_retries:
    print("Attempt",attempts +1, "-wait time",waite_time,)
    time.sleep(waite_time)
    waite_time *=2
    attempts +=1
    
            #########output=Attempt 1 -wait time 1
Attempt 2 -wait time 2
Attempt 3 -wait time 4
Attempt 4 -wait time 8
Attempt 5 -wait time 16