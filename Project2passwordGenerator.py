import random
import string
letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list(string.punctuation)
print("Welcome to Password Generators :")
letters_size=int(input("How many Letters would you like in your Password :"))
symbols_size=int(input("How many Symbols would you like in your Password :"))
numbers_size=int(input("How many Numbers would you like in your Password :"))
password=''
for i in range(1,letters_size+1):
    password+=random.choice(letters)
for i in range(1,symbols_size+1):
    password+=random.choice(special_characters)
for i in range(1,numbers_size+1):
    password+=random.choice(numbers)
password=list(password)
random.shuffle(password)
password_new="".join(password)
print(password_new)