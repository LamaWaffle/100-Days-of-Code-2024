
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


encrypt(plain_text=text, shift_amount=shift)        # Adding 'Keyword' arguments for the function.
