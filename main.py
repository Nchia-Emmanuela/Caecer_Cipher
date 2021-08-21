alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z']
key = int(input("Enter your key: \n"))
dirrection = input("Type 'Encode' to Encrype or 'Decode' to Decrypt: \n")
massage = input("Enter message: \n")
alphabet_len = len(alphabet)


def Encrypt(shift, text):
    cipher_text = ''
    for letter in massage:
        position = alphabet.index(letter)
        new_position = (position + key) % 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"the Encoded text is:\n {cipher_text}")

def Decrypt(shift, text)

Encrypt(shift = key, text = massage)
