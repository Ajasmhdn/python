import random

a=random.randint(1,56)
print(a)
b=random.randrange(1,3)
print(b)
c=random.random()
print(c)
d=random.uniform(1,3)
print(d)
#list=[1,2,3,4,5,6,7,8,9,10]
#e=random.choice(list)
#random.shuffle(list)
#print(e)
#print(list)
l = list(range(1, 57))
random.shuffle(l)
print(l)