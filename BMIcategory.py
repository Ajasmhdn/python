w=int(input("Enter your weight :"))
h=int(input("Enter your height :"))
bmi=w/(h*h)
if bmi<16.0:
    print("severe thinness")
elif bmi>=16.0 and bmi<17.0:
    print("moderate thinness")
elif bmi>=17.0 and bmi<18.5:
    print("mild thinness")
elif bmi>=18.5 and bmi<25.0:
    print("normal")
elif bmi>=25.0 and bmi<30.0:
    print("overweight")
elif bmi>=30.0 and bmi<35.0:
    print("obese class I")
elif bmi>=35.0 and bmi<=40.0:
    print("obese class II")
else:
    print("obese class III")