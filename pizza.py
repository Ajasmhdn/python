small_pizza=100
medium_pizza=200
large_pizza=300
print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S,M or L: ")
add_pepperoni=input("Do you want pepperoni? Y or N: ")
extra_cheese=input("Do you want extra cheese? Y or N: ")
bill=0
if(size=="S" or size =="s" ):
    bill+=small_pizza
    if(add_pepperoni=="Y"or add_pepperoni=="y"):
        bill+=30
        if(extra_cheese=="Y" or extra_cheese=="y"):
            bill+=20
elif(size=="M" or size =="m"):
    bill+=medium_pizza
    if(add_pepperoni=="Y"or add_pepperoni=="y"):
        bill+=50
        if(extra_cheese=="Y" or extra_cheese=="y"):
            bill+=20
elif(size=='L'or size=='l'):
    bill+=large_pizza
    if(add_pepperoni=="Y"or add_pepperoni=="y"):
        bill+=50
        if(extra_cheese=="Y" or extra_cheese=="y"):
            bill+=20
if bill > 0:
    print(f"the bill amount is : {bill}")
else:
    print("Invalid input")