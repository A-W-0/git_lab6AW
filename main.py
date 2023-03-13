"""
Lab 6: GitHub
Authors: Aidan Wood - Encode & Main
Ismael Maura - Decode
Created: 9 March 2023
"""


def encode(decoded_password_str):
    encoded_password = ""
    for digit in decoded_password_str:
        num = int(digit) + 3
        num -= 10 if num > 9 else 0
        encoded_password += str(num)
    return encoded_password


def decode(encoded_password_str):
    decoded_password = ""
    for digit in encoded_password_str:
        num = int(digit) - 3
        num += 10 if num < 0 else 0
        decoded_password += str(num)
    return decoded_password



if __name__ == "__main__":
    while True:
        print("1. Encode\n"
              "2. Decode\n"
              "q Quit\n"
              "Would you like to encode or decode? ")
        choice = input()
        if choice == "1":
            password_in = input("Enter password to encode: ")
            password_out = encode(password_in)
            print(password_out)
        elif choice == "2":

            password_in = input("Enter password to decode: ")
            password_out = decode(password_in)
            print(password_out)
        elif choice == "q":
            break
        else:
            print("Invalid input!")
            continue
