
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        shifted_position = position + shift
        cipher_text += alphabet[shifted_position]
    
    print(f"\nThe encoded text is {cipher_text}")


encypt(text, shift)
