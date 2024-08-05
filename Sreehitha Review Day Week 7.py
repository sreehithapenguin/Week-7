#a="hello"
#b="world"
#print(a+b)

'''a=8
b="hello"
print(str(a)+b)
c=4
d="8"
print(int(d)+c)
print(c+int(d))'''

import random
num=random.randint(0,100)
if num<10:
    type="the worst"
elif num<20:
    type="bad"
elif num<40:
    type="mid"
elif num<60:
    type="okay"
elif num<80:
    type="good"
elif num<=100:
    type="amazing"

print("You got",type,"in the lottery")

