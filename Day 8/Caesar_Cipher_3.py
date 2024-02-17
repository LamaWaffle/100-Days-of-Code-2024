
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def caesar(start_text, shift_amount, cipher_direction):
#     if direction == "encode":
#         cipher_text = ""
#         for letter in text:
#             position = alphabet.index(letter)           # Finding the index value for the specific letter that was inputted.
#             new_position = position + shift             # From that index, adding shift value to the index integer.
#             encrypted_letter = alphabet[new_position]   # From that new index, pulling out a letter from the list.
#             cipher_text += encrypted_letter             # Adding it into the cipher text string.
#         print(f"The encoded text is {cipher_text}")


#     elif direction == "decode":
#         plain_text = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position - shift             # minus the shift amount.
#             decrypted_letter = alphabet[new_position]
#             plain_text += decrypted_letter
#         print(f"The decoded text is {plain_text}")


# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1                               # Minus 1, else it will default to a positive in the next step.             
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {cipher_direction}d result: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)