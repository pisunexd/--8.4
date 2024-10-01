import datetime as dt

start_moment = dt.datetime(2019, 11, 16, 12, 0)  
current_moment = dt.datetime(2019, 11, 21, 14, 50)  

total_time = current_moment - start_moment 

print(total_time)