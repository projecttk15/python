import time;
import calendar; #use for python

localtime = time.localtime(time.time())
print ("Thoi gian hien tai la :", localtime)

localtime2 = time.asctime( time.localtime(time.time()) )
print ("Thoi gian da duoc dinh dang la :", localtime2)

print ("Thang hien tai la:")
cal = calendar.month(2020, 6)
print (cal)
