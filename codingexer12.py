import random
names=input("Enter the names seprated by comma :")
name=names.split(",")
print(name)
a=random.choice(name)
print(a)
b=random.randint(0,len(name)-1)
c=name[b]
print(c)

