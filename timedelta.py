from datetime import datetime,timezone,timedelta 

t = int(input()) 

def parse_timezone(tz_str):
    if tz_str[0]=='+':
       sign =1  
    else:
       sign = -1 
    hours = int(tz_str[1:3])
    minutes = int(tz_str[3:5])
    return timezone(timedelta(hours=sign*hours, minutes=sign*minutes)) 
months = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
for _ in range(t):
    t1 = input().split()
    t2 = input().split()
    day1 = t1[1]
    hour1 = t1[4][0:2]
    minute1 = t1[4][3:5]
    second1 = t1[4][6:8]
    month1 = months[t1[2]]
    year1  = t1[3]
    offset1 = parse_timezone(str(t1[5]))
    dt1 = datetime(int(year1),int(month1),int(day1),int(hour1),int(minute1),int(second1),tzinfo=offset1)
    
    day2 = t2[1]
    hour2 = t2[4][0:2]
    minute2 = t2[4][3:5]
    second2 = t2[4][6:8]
    month2 = months[t2[2]]
    year2 = t2[3]
    offset2 = parse_timezone(t2[5])
    dt2 = datetime(int(year2),int(month2),int(day2),int(hour2),int(minute2),int(second2),tzinfo=offset2)
    difference = int(abs((dt1 - dt2).total_seconds()))
    print(difference) 
    
    
    
