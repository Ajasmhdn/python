import string

alpha = string.ascii_lowercase
alphabet=list(alpha)
def encrypt(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            pos=alphabet.index(char)
            new_pos=(pos+shift_key)%26
            cipher_text+=alphabet[new_pos]
        else:
            cipher_text+=char
    print(f"The encrypted text is: {cipher_text}")
def decrypt(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            pos=alphabet.index(char)
            new_pos=(pos-shift_key)%26
            plain_text+=alphabet[new_pos]
        else:
            plain_text+=char
    print(f"The decrypted text is: {plain_text}")
End=False
while not End:
    what_to_do=input("Enter 'e' for encryption and 'd' for decryption: ")
    text=input("Enter the text: ")
    shift=int(input("Enter the shift value: "))
    if (what_to_do=='e'):
        encrypt(text,shift)
    elif (what_to_do=='d'):
        decrypt(text,shift)
    play_again=input("Do you want to play again? (yes/no): ")
    if play_again=='no':
        End=True
        print("Goodbye!")
    else:
        End=False



