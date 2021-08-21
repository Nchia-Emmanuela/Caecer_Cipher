import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z']
key = int(input("Enter your key: \n"))
dirrection = input("Type 'Encode' to Encrype or 'Decode' to Decrypt: \n")
massage = input("Enter message: \n")
alphabet_len = len(alphabet)

def caeser(start_text, shift_amount, cipher_dirrection):
    end_text = ''
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_dirrection == 'Decode':
            shift_amount *= -1
        new_position = (position + shift_amount) % 26
        end_text += alphabet[new_position]
    print(f"the {cipher_dirrection}d massage is {end_text}")
caeser(start_text = massage, shift_amount = key, cipher_dirrection = dirrection)



# def Encrypt(shift, plain_text):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = (position + key) % 26
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the Cipher text is:\n {cipher_text}\n")

# def Decrypt(shift, cipher):
#     plain_text = ''
#     for letter in cipher:
#         position = alphabet.index(letter)
#         new_position = (position - key) % 26
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"the Plain test is:\n {plain_text}\n")
# if dirrection == 'Encode':
#     Encrypt(shift = key, plain_text = massage)
# elif dirrection == 'Decode':
#     Decrypt(shift = key, cipher = massage)
