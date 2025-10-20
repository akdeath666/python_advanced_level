import time
t=time.strftime("%H:%M:%S")
print(t)
hour=int(time.strftime("%H"))
min=int(time.strftime("%M"))
sec=int(time.strftime("%S"))
print(hour)
print(min)
print(sec)

if(hour>=0 and hour<12):
    print("GOOD MORNING SIR")
elif(hour>=12 and hour<17):
    print("GOOD AFTERNOON SIR")
elif(hour>17 and hour<=24):
    print("GOOD EVENING SIR")
    