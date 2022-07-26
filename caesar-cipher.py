from art import logo


def caesar(start_text, shift_amount, direction_type):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction_type == "encode":
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            elif direction_type == "decode":
                new_position = position - shift_amount
                end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction_type}d text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


print(logo)
should_encode = True

while should_encode:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    encoded_text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25
    caesar(start_text=encoded_text, direction_type=direction, shift_amount=shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if result == "no":
        should_encode = False
