alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(original_text,shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter.isalpha():
            lower_letter = letter.lower()
            shifted_index = (alphabet.index(lower_letter) + shift_amount) % 26
            new_letter = alphabet[shifted_index]
            
            cipher_text += new_letter.upper() if letter.isupper() else new_letter
        else:
            cipher_text += letter  
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text,shift_amount):
    output_text = ""
    for letter in original_text:
        if letter.isalpha():
            lower_letter = letter.lower()
            shifted_index = (alphabet.index(lower_letter) - shift_amount) % 26
            new_letter = alphabet[shifted_index]
            output_text += new_letter.upper() if letter.isupper() else new_letter
        else:
            output_text += letter
    print(f"Here is the decoded result: {output_text}")



run = "Y"
while run.upper() == "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid direction!")

    run = input("Do you want to convert more...? Y/N: ").upper()
