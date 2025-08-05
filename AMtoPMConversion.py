t = input()
hour = int(t[:2])
minutes = int(t[3:5])
seconds = int(t[6:8])
ampm = t[8:10]

if ampm = "AM" and hour == 12:
    hour = 0 
elif ampm = "PM" and hour !=12:
     hour +=12 
     
print(f{hour:02d}:{minutes:02d}:{seconds:02d})

    
    



   
