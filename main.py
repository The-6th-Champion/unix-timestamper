#importing time. duh
import time

#hours offset: change this to go forwards (positive0 or backwards (negative)
offset = 0 

#quick maths with offset
timezone = 60*60*offset

#get time stamp
utc_ts = int(time.time() + timezone)

#give timestamp to you
print(utc_ts)






#Comments are fun
