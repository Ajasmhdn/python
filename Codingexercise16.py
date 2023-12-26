#Calculate the sum of even from 1 to n, including 1 and n
n=int(input("Enter the number upto sumbof even number should be find :"))
sum=0
for i in range(0,n+1,2):
    sum+=i
print(f"Sum of first {n} even natural number is : {sum}")
sumodd=0
for i in range(1,n+1,2):
    sumodd+=i
print(f"Sum of first {n} Odd natural number is : {sumodd}")
total=sum+sumodd
print(f"Sum of first {n} natural number is : {total}")