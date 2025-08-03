## Electricity bill generator
units=int(input())
total_units=0
if(units<=100):
    total_units+=(100*1.5)
elif(units>100 and units<=200):
    total_units+=(150+(units-100)*2.5)
elif(units>200 and units<=500):
    total_units+=(400+(units-200)*4)
elif(units>500):
    total_units+=(1600+(units-500)*6)
print(total_units)