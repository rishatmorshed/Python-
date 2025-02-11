Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in Alphabet:
            position = Alphabet.index(char)
            new_position = (position+shift_key) % 26
            cipher_text = cipher_text + Alphabet[new_position]
        else:
            cipher_text += char
    print(f"After perform encryption operation cipher text is: {cipher_text}")

def Decryption(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char in Alphabet:
            position = Alphabet.index(char)
            new_position = position-shift
            plain_text = plain_text + Alphabet[new_position]
        else:
            plain_text += char
    print(f"After perform decryption operation plain text is: {plain_text}")

wanna_end = False
while not wanna_end:
    what_to_do = input("For 'Encryption' type encrypt and for 'Decryption' type decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Enter shift value:\n"))
    if what_to_do == "encrypt":
        Encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        Decryption(text, shift)
    print("Type 'yes' to continue or type 'no' to exit: ")
    play_again = input()
    if play_again == "no":
        wanna_end = True
        print("Have a good day! Bye...")
        break
