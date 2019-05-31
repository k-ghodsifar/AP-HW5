import random
import sys

def IsInCircle(x,y):
    if( (x**2 + y**2) <= 1) :
        return True
    else:
        return False

def find():
    counter=counterC=pi=randNumber=0
    while (pi != 3.14):
        counter += 1
        a = random.uniform(0,1)
        b =random.uniform(0,1)
        if IsInCircle(a,b) is True:
            counterC += 1
        pi = round( ((counterC*4) /counter) , 2)
    return counter

a=[]
print('You must enter x and y')
for i in range(2):
    a.append(eval(input()))
if IsInCircle(a[0],a[1]) is True:
    print("In Circle.\n")
else:
    print("Not in circle.\n")
b=a=0
m = eval(input('How many times to try?'))
for i in range (m):
    a = find()
    b += a
    print(a)

print( f'avarage was { round((b/m),5)}')
