import art
#  or we could import the logo by saying:
#  form art import logo then we print logo
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z']


# def caeser(start_text, shift_amount, cipher_dirrection):
#     end_text = ''
#     for letter in start_text:
#         position = alphabet.index(letter)
#         if cipher_dirrection == 'Decode':
#             shift_amount *= -1
#         new_position = (position + shift_amount) % 26
#         end_text += alphabet[new_position]
#     print(f"the {cipher_dirrection}d massage is {end_text}")
# caeser(start_text = massage, shift_amount = key, cipher_dirrection = dirrection)



def Encrypt(shift, plain_text):
    cipher_text = ''
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + key) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    print(f"the Cipher text is:\n {cipher_text}\n")

def Decrypt(shift, cipher):
    plain_text = ''
    for char in cipher:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - key) % 26
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += char
    print(f"the Plain test is:\n {plain_text}\n")
should_end = False
while not should_end:
    key = int(input("Enter your key: \n"))
    dirrection = input("Type 'Encode' to Encrype or 'Decode' to Decrypt: \n")
    massage = input("Enter message: \n")

    if dirrection == 'Encode':
        Encrypt(shift = key, plain_text = massage)
    elif dirrection == 'Decode':
        Decrypt(shift = key, cipher = massage)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")