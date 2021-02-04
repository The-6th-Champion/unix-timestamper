#importing time. duh
import time

#hours offset: change this to go forwards (positive) or backwards (negative)
offset = int(input("Offset from your current time in hours (put 0 if none, negative number if back in time, etc): ")) 
#offset = 0   old line of code

#quick maths with offset
timezone = 60*60*offset

#get time stamp
utc_ts = int(time.time() + timezone)

#give timestamp to you
print(utc_ts)






#Comments are fun
#comment in the comment section if you think so too
