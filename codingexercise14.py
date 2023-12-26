#calculate avg height from list without using sum and len function
#also take it as input from user
#and print the list of heights that are above avg height
heights=input("Enter the all heights(cm) seperated by space: ")
list1=heights.split()
sum=0
count=0
for i in list1:
    sum+=int(i)
    count+=1
avg=sum/count
print("the avg height from list is : ",avg)
print("the length of the list : ",count)