#Kerem YAGAN
#https://github.com/keremyagan
import random
from time import sleep
numbers=[]
length=[]

while len(numbers)<6:
    number=random.randint(0,10)
    if numbers.count(number)!=2 and len(numbers)<5 :
        numbers.append(number)
        print(number,end=" ")
        sleep(2)
        
    if len(numbers)==5:
        for n in numbers:
            length.append(numbers.count(n))
        if max(length)<2:
            last_number=random.choice(numbers)
            print(last_number)  
            numbers.append(last_number)   
        elif max(length)==2:
            number=random.randint(0,10)
            if not number in numbers: 
                print(number,end=" ")
                numbers.append(number) 
