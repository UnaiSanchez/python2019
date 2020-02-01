from datetime import datetime
from random import randint

name= "unai"
age=randint(0,20)
birthday = 3
birthmonth = 8
birthyear = (datetime.now().year -age)%100 
print("My name is "+str(name)+", and I am "+str(age)+" years old, and I was born on the "+str(birthday)+"/"+str(birthmonth)+"/"+str(birthyear))
print("my name is %s, and I am %d years old, and I was born on the %d/%d/%d" %(name,age,birthday,birthmonth,birthyear))
print("My name is {}, and I am {} years old, and I was born on the {:02}/{:02}/{:02}".format(name,age,birthday,birthmonth,birthyear))
print(f"My name is {name}, and I am {age} years old, and I was born on the {birthday:02}/{birthmonth:02}/{birthyear:02}")