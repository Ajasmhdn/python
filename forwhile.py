#sentinel value
""""number=int(input("Enter a number(-1 to quit):"))
while number!=-1:
    square=number**2
    print(square)
    number=int(input("Enter a number(-1 to quit):"))
else:
    print("in else block")
print("Good bye")"""
num=int(input("Enter the numbers to be added(0 to quit):"))
sum=0
while num!=0:
    sum+=num
    print(f"the sum till now is : {sum}")
    num=int(input("Enter the numbers to be added(0 to quit):"))
else:
    print(f"The Sum is : {sum}")
    print("You have choosen to quit")