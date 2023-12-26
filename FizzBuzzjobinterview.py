#print num 1 to n which is divisible by 4 and 5 as Fizz Buzz and common Fizzbuzz
n=int(input("Enter the number upto be print: "))
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0):
        print("Fizz")
    else:
        print(i)