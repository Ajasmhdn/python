a=input("enter a two digit number")
num1=int(a)
sum=0
while num1>0:
    digit = num1%10
    sum+=digit
    num1=num1//10
print(sum)


