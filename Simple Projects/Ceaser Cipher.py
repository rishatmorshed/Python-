Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Encryption(plain_text, shift_key, message):
    cipher_text = ""
    for char in plain_text:
        if char in Alphabet:
            position = Alphabet.index(char)
            new_position = (position + shift_key) % 26  # No need to change shift_key
            cipher_text += Alphabet[new_position]
        else:
            cipher_text += char  # Keep spaces and special characters unchanged
    print(f"After performing {message} operation, result is: {cipher_text}")

wanna_end = False
while not wanna_end:
    what_to_do = input("For 'Encryption' type encrypt and for 'Decryption' type decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Enter shift value:\n"))

    if what_to_do == "encrypt":
        Encryption(plain_text=text, shift_key=shift, message=what_to_do)
    elif what_to_do == "decrypt":
        Encryption(plain_text=text, shift_key=-shift, message=what_to_do)  # Pass negative shift for decryption

    play_again = input("Type 'yes' to continue or type 'no' to exit:\n").lower()
    if play_again == "no":
        wanna_end = True
        print("Have a good day! Bye...")
