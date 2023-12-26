#program to find the max number from a list of numbers with no max()
input1=input("Enter the numbers you want in the list seprated by space :")
list1=input1.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
print(list1)
max=list1[0]
for num in list1:
    if num+1>max:
        max=num
print(max)
