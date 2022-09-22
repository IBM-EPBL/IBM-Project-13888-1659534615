
temp=int(input("enter the temprature in celsius:"))
humi=int(input("enter the humidity in percentage:"))
if(temp>150):
    print("the temprature is high")
elif(temp<20):
    print("the temprature is low")
else:
    print("the temprature is moderate")
if(humi>60):
    print("the humidity is high")
elif(humi<40):
    print("the humidity is low")
else:
    print("the humidity is moderate")
