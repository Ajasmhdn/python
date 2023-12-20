boy=input("Enter the lover name(boy) :")
girl=input("Enter the lover name(girl) :")
name=boy+girl
lowercase_name=name.lower()
one=lowercase_name.count('t'or 'r' or 'u' or 'e' )
two=lowercase_name.count('l'or 'o' or 'v' or 'e' )
per=int(str(one)+str(two))
print(f"The love percentage is {per}% ")
if(per<10 or per>90):
    print(f"Your score is {per},you are blast")
elif(per>40 and per<50):
    print(f"Your score is {per},you are alright together")
else:
    print(f"Your score is {per}")