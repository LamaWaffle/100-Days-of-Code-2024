
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)           # Finding the index value for the specific letter that was inputted.
        new_position = position + shift_amount      # From that index, adding shift value to the index integer.
        encrypted_letter = alphabet[new_position]   # From that new index, pulling out a letter from the list.
        cipher_text += encrypted_letter             # Adding it into the cipher text string.
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount      # minus the shift amount.
        decrypted_letter = alphabet[new_position]
        plain_text += decrypted_letter
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Please enter a valid option, encode or decode.. Try again.\n")
