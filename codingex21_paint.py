import math
def calculate_no_of_cans(h, w, c):
    no = (h * w) / c
    cans=math.ceil(no)
    print(f"You need {cans} cans of paint")
print("Enter values in meters")
h=int(input("Enter the height of the wall:"))
w=int(input("Enter the width of the wall:"))
c=int(input("Enter the coverage of the paint:"))
calculate_no_of_cans(h, w, c)
