list=[[1,1,1],[1,1,1],[1,1,1]]
print(list[0],"\n")
print(list[1],"\n")
print(list[2],"\n")
row=int(input("input the row in 3x3 matrix"))
column=int(input("input the column in 3x3 matrix"))
if(list[row-1][column-1]==1):
    list[row-1][column-1]="X"
print(list[0],"\n")
print(list[1],"\n")
print(list[2],"\n")